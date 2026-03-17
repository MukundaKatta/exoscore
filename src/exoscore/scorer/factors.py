"""Individual factor scorers for habitability assessment.

Each factor scorer returns a value in [0, 1] representing how favourable
a given property is for habitability.
"""

from __future__ import annotations

import numpy as np

from exoscore.models import Exoplanet, Star
from exoscore.scorer.zone import HabitableZoneCalculator


def temperature_score(planet: Exoplanet) -> float:
    """Score based on equilibrium temperature.

    Optimal range: 200-310 K (liquid water under ~1 atm).
    Gaussian falloff outside the sweet spot centred at 255 K.
    """
    if planet.equilibrium_temp is None:
        return 0.3  # unknown => mild penalty
    t = planet.equilibrium_temp
    optimal = 255.0
    sigma = 60.0
    return float(np.exp(-0.5 * ((t - optimal) / sigma) ** 2))


def atmosphere_score(planet: Exoplanet) -> float:
    """Score based on atmosphere presence and density.

    An atmosphere of moderate density is most favourable. Too thin gives
    no protection; too thick implies a Venus-like runaway greenhouse.
    """
    if planet.has_atmosphere is False:
        return 0.05
    if planet.atmosphere_density is None:
        return 0.3  # unknown
    d = planet.atmosphere_density
    # Peak at ~0.5 density
    return float(np.exp(-8.0 * (d - 0.5) ** 2))


def water_score(planet: Exoplanet) -> float:
    """Score based on likelihood of surface liquid water."""
    if planet.water_likelihood is None:
        return 0.2
    return float(planet.water_likelihood)


def magnetic_field_score(planet: Exoplanet) -> float:
    """Score based on magnetic field presence.

    A magnetic field shields the atmosphere from stellar wind stripping.
    """
    if planet.has_magnetic_field is True:
        return 1.0
    if planet.has_magnetic_field is False:
        return 0.15
    # Unknown: estimate from mass (larger rocky planets more likely to have one)
    if planet.mass is not None and planet.mass > 0:
        # Sigmoid centred at ~1.5 Earth masses
        return float(1.0 / (1.0 + np.exp(-2.0 * (planet.mass - 1.5))))
    return 0.3


def star_stability_score(star: Star | None) -> float:
    """Score based on stellar variability and flare activity.

    Low variability is better. M-dwarfs often have high flare rates.
    """
    if star is None:
        return 0.3
    return float(1.0 - star.variability)


def orbit_score(planet: Exoplanet, star: Star | None) -> float:
    """Score based on orbital properties.

    Considers:
    - Whether the planet is in the habitable zone
    - Orbital eccentricity (lower is better for stable climate)
    """
    hz_score = 0.3  # default if star unknown
    if star is not None:
        hz = HabitableZoneCalculator.compute(star)
        a = planet.semi_major_axis
        if hz.conservative_inner_au <= a <= hz.conservative_outer_au:
            hz_score = 1.0
        elif hz.inner_boundary_au <= a <= hz.outer_boundary_au:
            hz_score = 0.75
        else:
            # Distance from nearest HZ edge, penalised
            inner_dist = abs(a - hz.inner_boundary_au)
            outer_dist = abs(a - hz.outer_boundary_au)
            min_dist = min(inner_dist, outer_dist)
            hz_width = hz.outer_boundary_au - hz.inner_boundary_au
            if hz_width > 0:
                hz_score = float(max(0.0, 0.5 * np.exp(-3.0 * min_dist / hz_width)))
            else:
                hz_score = 0.1

    # Eccentricity penalty
    ecc_factor = float(1.0 - 0.7 * planet.eccentricity)

    return hz_score * ecc_factor
