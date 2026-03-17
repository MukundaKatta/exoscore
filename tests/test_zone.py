"""Tests for habitable zone calculator."""

import pytest

from exoscore.models import SpectralType, Star
from exoscore.scorer.zone import HabitableZoneCalculator


@pytest.fixture
def sun_like_star():
    return Star(
        name="Sun-like",
        spectral_type=SpectralType.G,
        luminosity=1.0,
        mass=1.0,
        temperature=5780,
        radius=1.0,
    )


@pytest.fixture
def m_dwarf():
    return Star(
        name="M-dwarf",
        spectral_type=SpectralType.M,
        luminosity=0.001,
        mass=0.1,
        temperature=3000,
        radius=0.15,
    )


class TestHabitableZoneCalculator:
    def test_sun_like_hz_boundaries(self, sun_like_star):
        hz = HabitableZoneCalculator.compute(sun_like_star)
        # For a sun-like star, inner should be ~0.75 AU, outer ~1.77 AU
        assert 0.7 < hz.inner_boundary_au < 0.85
        assert 1.5 < hz.outer_boundary_au < 2.0
        assert hz.conservative_inner_au > hz.inner_boundary_au
        assert hz.conservative_outer_au < hz.outer_boundary_au

    def test_m_dwarf_hz_closer(self, m_dwarf):
        hz = HabitableZoneCalculator.compute(m_dwarf)
        # M-dwarf HZ should be much closer to the star
        assert hz.inner_boundary_au < 0.1
        assert hz.outer_boundary_au < 0.2

    def test_boundary_ordering(self, sun_like_star):
        hz = HabitableZoneCalculator.compute(sun_like_star)
        assert hz.inner_boundary_au < hz.conservative_inner_au
        assert hz.conservative_inner_au < hz.conservative_outer_au
        assert hz.conservative_outer_au < hz.outer_boundary_au

    def test_is_in_hz(self, sun_like_star):
        assert HabitableZoneCalculator.is_in_hz(sun_like_star, 1.0)
        assert not HabitableZoneCalculator.is_in_hz(sun_like_star, 0.1)
        assert not HabitableZoneCalculator.is_in_hz(sun_like_star, 5.0)

    def test_is_in_conservative_hz(self, sun_like_star):
        assert HabitableZoneCalculator.is_in_conservative_hz(sun_like_star, 1.0)
        # Edge of optimistic but outside conservative
        hz = HabitableZoneCalculator.compute(sun_like_star)
        just_inside_optimistic = hz.inner_boundary_au + 0.001
        if just_inside_optimistic < hz.conservative_inner_au:
            assert not HabitableZoneCalculator.is_in_conservative_hz(
                sun_like_star, just_inside_optimistic
            )

    def test_luminosity_scaling(self):
        dim = Star(name="Dim", spectral_type=SpectralType.K, luminosity=0.1,
                   mass=0.5, temperature=4000, radius=0.5)
        bright = Star(name="Bright", spectral_type=SpectralType.F, luminosity=5.0,
                      mass=1.5, temperature=6500, radius=1.5)
        hz_dim = HabitableZoneCalculator.compute(dim)
        hz_bright = HabitableZoneCalculator.compute(bright)
        assert hz_dim.outer_boundary_au < hz_bright.outer_boundary_au
