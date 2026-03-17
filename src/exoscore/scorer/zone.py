"""Habitable zone calculator.

Computes inner and outer habitable zone boundaries based on stellar
luminosity using the Kopparapu et al. (2013) model.
"""

from __future__ import annotations

import numpy as np

from exoscore.models import HabitableZone, Star


class HabitableZoneCalculator:
    """Calculate habitable zone boundaries for a given star.

    Uses the effective stellar flux boundaries from Kopparapu et al. (2013).
    The optimistic HZ runs from Recent Venus to Early Mars, while the
    conservative HZ uses Runaway Greenhouse to Maximum Greenhouse.
    """

    # Effective solar flux coefficients for HZ boundaries
    # [S_eff_sun, a, b, c, d] where
    # S_eff = S_eff_sun + a*T_star + b*T_star^2 + c*T_star^3 + d*T_star^4
    # T_star = T_eff - 5780
    _RECENT_VENUS = (1.7763, 1.4335e-4, 3.3954e-9, -7.6364e-12, -1.1950e-15)
    _RUNAWAY_GREENHOUSE = (1.0385, 1.2456e-4, 1.4612e-8, -7.6345e-12, -1.7511e-15)
    _MAXIMUM_GREENHOUSE = (0.3507, 5.9578e-5, 1.6707e-9, -3.0058e-12, -5.1925e-16)
    _EARLY_MARS = (0.3207, 5.4471e-5, 1.5275e-9, -2.1709e-12, -3.8282e-16)

    @staticmethod
    def _effective_flux(
        coeffs: tuple[float, float, float, float, float],
        t_star: float,
    ) -> float:
        """Compute effective stellar flux at a HZ boundary."""
        s0, a, b, c, d = coeffs
        dt = t_star - 5780.0
        return s0 + a * dt + b * dt**2 + c * dt**3 + d * dt**4

    @classmethod
    def _boundary_au(cls, luminosity: float, s_eff: float) -> float:
        """Convert effective flux to orbital distance in AU."""
        return float(np.sqrt(luminosity / s_eff))

    @classmethod
    def compute(cls, star: Star) -> HabitableZone:
        """Compute habitable zone boundaries for a star.

        Parameters
        ----------
        star:
            Star model with luminosity and effective temperature.

        Returns
        -------
        HabitableZone with inner/outer and conservative inner/outer edges.
        """
        t = star.temperature
        lum = star.luminosity

        s_rv = cls._effective_flux(cls._RECENT_VENUS, t)
        s_rg = cls._effective_flux(cls._RUNAWAY_GREENHOUSE, t)
        s_mg = cls._effective_flux(cls._MAXIMUM_GREENHOUSE, t)
        s_em = cls._effective_flux(cls._EARLY_MARS, t)

        return HabitableZone(
            star_name=star.name,
            inner_boundary_au=cls._boundary_au(lum, s_rv),
            outer_boundary_au=cls._boundary_au(lum, s_em),
            conservative_inner_au=cls._boundary_au(lum, s_rg),
            conservative_outer_au=cls._boundary_au(lum, s_mg),
        )

    @classmethod
    def is_in_hz(cls, star: Star, semi_major_axis: float) -> bool:
        """Check whether an orbital distance falls within the optimistic HZ."""
        hz = cls.compute(star)
        return hz.inner_boundary_au <= semi_major_axis <= hz.outer_boundary_au

    @classmethod
    def is_in_conservative_hz(cls, star: Star, semi_major_axis: float) -> bool:
        """Check whether an orbital distance falls within the conservative HZ."""
        hz = cls.compute(star)
        return hz.conservative_inner_au <= semi_major_axis <= hz.conservative_outer_au
