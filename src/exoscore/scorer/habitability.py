"""Multi-factor habitability scorer.

Combines individual factor scores into a single habitability index in [0, 1].
"""

from __future__ import annotations

from exoscore.models import Exoplanet, FactorScore, HabitabilityReport, Star
from exoscore.scorer import factors
from exoscore.scorer.zone import HabitableZoneCalculator


class HabitabilityScorer:
    """Compute a composite habitability index for an exoplanet.

    The index is a weighted combination of six factors:
      - Temperature suitability (weight 0.25)
      - Atmosphere presence/density (weight 0.20)
      - Liquid water likelihood (weight 0.20)
      - Magnetic field (weight 0.10)
      - Star stability (weight 0.10)
      - Orbital properties / HZ position (weight 0.15)

    Weights sum to 1.0.  Each factor is scored in [0, 1].
    """

    DEFAULT_WEIGHTS: dict[str, float] = {
        "temperature": 0.25,
        "atmosphere": 0.20,
        "water": 0.20,
        "magnetic_field": 0.10,
        "star_stability": 0.10,
        "orbit": 0.15,
    }

    def __init__(self, weights: dict[str, float] | None = None) -> None:
        self.weights = dict(self.DEFAULT_WEIGHTS)
        if weights:
            self.weights.update(weights)
        # Normalise so weights sum to 1
        total = sum(self.weights.values())
        if total > 0:
            self.weights = {k: v / total for k, v in self.weights.items()}

    def score(
        self, planet: Exoplanet, star: Star | None = None
    ) -> HabitabilityReport:
        """Produce a full habitability report for a planet.

        Parameters
        ----------
        planet:
            The exoplanet to assess.
        star:
            The host star (optional, improves accuracy).

        Returns
        -------
        HabitabilityReport with overall score, factor breakdown, and
        human-readable classification.
        """
        factor_scores: list[FactorScore] = []

        temp = factors.temperature_score(planet)
        factor_scores.append(FactorScore(
            name="temperature",
            score=temp,
            weight=self.weights["temperature"],
            description=self._temp_desc(planet),
        ))

        atmo = factors.atmosphere_score(planet)
        factor_scores.append(FactorScore(
            name="atmosphere",
            score=atmo,
            weight=self.weights["atmosphere"],
            description=self._atmo_desc(planet),
        ))

        water = factors.water_score(planet)
        factor_scores.append(FactorScore(
            name="water",
            score=water,
            weight=self.weights["water"],
            description=self._water_desc(planet),
        ))

        mag = factors.magnetic_field_score(planet)
        factor_scores.append(FactorScore(
            name="magnetic_field",
            score=mag,
            weight=self.weights["magnetic_field"],
            description=self._mag_desc(planet),
        ))

        stab = factors.star_stability_score(star)
        factor_scores.append(FactorScore(
            name="star_stability",
            score=stab,
            weight=self.weights["star_stability"],
            description=self._stab_desc(star),
        ))

        orb = factors.orbit_score(planet, star)
        factor_scores.append(FactorScore(
            name="orbit",
            score=orb,
            weight=self.weights["orbit"],
            description=self._orbit_desc(planet, star),
        ))

        overall = sum(fs.score * fs.weight for fs in factor_scores)
        overall = max(0.0, min(1.0, overall))

        hz = None
        in_hz = False
        if star is not None:
            hz = HabitableZoneCalculator.compute(star)
            in_hz = HabitableZoneCalculator.is_in_hz(star, planet.semi_major_axis)

        classification = self._classify(overall)
        summary = self._build_summary(planet, star, overall, classification, in_hz)

        return HabitabilityReport(
            planet=planet,
            star=star,
            habitable_zone=hz,
            overall_score=round(overall, 4),
            factor_scores=factor_scores,
            in_habitable_zone=in_hz,
            classification=classification,
            summary=summary,
        )

    @staticmethod
    def _classify(score: float) -> str:
        if score >= 0.80:
            return "Highly Promising"
        if score >= 0.60:
            return "Promising"
        if score >= 0.40:
            return "Moderate Potential"
        if score >= 0.20:
            return "Low Potential"
        return "Unlikely Habitable"

    @staticmethod
    def _temp_desc(planet: Exoplanet) -> str:
        if planet.equilibrium_temp is None:
            return "Equilibrium temperature unknown."
        return f"Equilibrium temperature {planet.equilibrium_temp} K."

    @staticmethod
    def _atmo_desc(planet: Exoplanet) -> str:
        if planet.has_atmosphere is False:
            return "No atmosphere detected."
        if planet.atmosphere_density is not None:
            return f"Estimated atmosphere density: {planet.atmosphere_density:.1f}."
        return "Atmosphere status unknown."

    @staticmethod
    def _water_desc(planet: Exoplanet) -> str:
        if planet.water_likelihood is None:
            return "Water likelihood unknown."
        return f"Surface water likelihood: {planet.water_likelihood:.0%}."

    @staticmethod
    def _mag_desc(planet: Exoplanet) -> str:
        if planet.has_magnetic_field is True:
            return "Magnetic field detected."
        if planet.has_magnetic_field is False:
            return "No magnetic field detected."
        return "Magnetic field status unknown; estimated from mass."

    @staticmethod
    def _stab_desc(star: Star | None) -> str:
        if star is None:
            return "Host star data unavailable."
        return f"Stellar variability index: {star.variability:.2f}."

    @staticmethod
    def _orbit_desc(planet: Exoplanet, star: Star | None) -> str:
        parts = [f"Semi-major axis: {planet.semi_major_axis} AU"]
        if planet.eccentricity > 0:
            parts.append(f"eccentricity: {planet.eccentricity}")
        if star is not None:
            hz = HabitableZoneCalculator.compute(star)
            if hz.inner_boundary_au <= planet.semi_major_axis <= hz.outer_boundary_au:
                parts.append("within habitable zone")
            else:
                parts.append("outside habitable zone")
        return "; ".join(parts) + "."

    @staticmethod
    def _build_summary(
        planet: Exoplanet,
        star: Star | None,
        score: float,
        classification: str,
        in_hz: bool,
    ) -> str:
        lines = [
            f"{planet.name} receives a habitability score of {score:.2f} "
            f"({classification}).",
        ]
        if in_hz:
            lines.append("The planet orbits within its star's habitable zone.")
        elif star is not None:
            lines.append("The planet orbits outside its star's habitable zone.")
        if planet.equilibrium_temp is not None:
            lines.append(
                f"Equilibrium temperature is {planet.equilibrium_temp} K."
            )
        return " ".join(lines)
