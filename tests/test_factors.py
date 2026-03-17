"""Tests for individual factor scorers."""

import pytest

from exoscore.models import Exoplanet, SpectralType, Star
from exoscore.scorer.factors import (
    atmosphere_score,
    magnetic_field_score,
    orbit_score,
    star_stability_score,
    temperature_score,
    water_score,
)


def _make_planet(**kwargs) -> Exoplanet:
    defaults = {"name": "Test", "host_star": "TestStar", "semi_major_axis": 1.0}
    defaults.update(kwargs)
    return Exoplanet(**defaults)


def _make_star(**kwargs) -> Star:
    defaults = {
        "name": "TestStar",
        "spectral_type": SpectralType.G,
        "luminosity": 1.0,
        "mass": 1.0,
        "temperature": 5780,
        "radius": 1.0,
    }
    defaults.update(kwargs)
    return Star(**defaults)


class TestTemperatureScore:
    def test_optimal_temp(self):
        p = _make_planet(equilibrium_temp=255)
        assert temperature_score(p) > 0.95

    def test_too_hot(self):
        p = _make_planet(equilibrium_temp=500)
        assert temperature_score(p) < 0.1

    def test_too_cold(self):
        p = _make_planet(equilibrium_temp=50)
        assert temperature_score(p) < 0.1

    def test_unknown_temp(self):
        p = _make_planet(equilibrium_temp=None)
        assert temperature_score(p) == 0.3

    def test_score_range(self):
        for t in range(100, 600, 50):
            p = _make_planet(equilibrium_temp=t)
            s = temperature_score(p)
            assert 0.0 <= s <= 1.0


class TestAtmosphereScore:
    def test_no_atmosphere(self):
        p = _make_planet(has_atmosphere=False)
        assert atmosphere_score(p) < 0.1

    def test_moderate_density(self):
        p = _make_planet(atmosphere_density=0.5)
        assert atmosphere_score(p) > 0.9

    def test_too_thick(self):
        p = _make_planet(atmosphere_density=1.0)
        assert atmosphere_score(p) < 0.3

    def test_unknown(self):
        p = _make_planet(has_atmosphere=None, atmosphere_density=None)
        assert atmosphere_score(p) == 0.3


class TestWaterScore:
    def test_high_likelihood(self):
        p = _make_planet(water_likelihood=0.8)
        assert water_score(p) == 0.8

    def test_unknown(self):
        p = _make_planet(water_likelihood=None)
        assert water_score(p) == 0.2


class TestMagneticFieldScore:
    def test_has_field(self):
        p = _make_planet(has_magnetic_field=True)
        assert magnetic_field_score(p) == 1.0

    def test_no_field(self):
        p = _make_planet(has_magnetic_field=False)
        assert magnetic_field_score(p) == 0.15

    def test_unknown_heavy_planet(self):
        p = _make_planet(has_magnetic_field=None, mass=5.0)
        assert magnetic_field_score(p) > 0.5

    def test_unknown_light_planet(self):
        p = _make_planet(has_magnetic_field=None, mass=0.3)
        assert magnetic_field_score(p) < 0.5


class TestStarStabilityScore:
    def test_stable_star(self):
        s = _make_star(variability=0.0)
        assert star_stability_score(s) == 1.0

    def test_variable_star(self):
        s = _make_star(variability=0.8)
        assert star_stability_score(s) == pytest.approx(0.2)

    def test_no_star(self):
        assert star_stability_score(None) == 0.3


class TestOrbitScore:
    def test_in_hz(self):
        star = _make_star()
        p = _make_planet(semi_major_axis=1.0, eccentricity=0.0)
        s = orbit_score(p, star)
        assert s > 0.7

    def test_outside_hz(self):
        star = _make_star()
        p = _make_planet(semi_major_axis=0.01, eccentricity=0.0)
        s = orbit_score(p, star)
        assert s < 0.3

    def test_high_eccentricity_penalty(self):
        star = _make_star()
        p_circ = _make_planet(semi_major_axis=1.0, eccentricity=0.0)
        p_ecc = _make_planet(semi_major_axis=1.0, eccentricity=0.5)
        assert orbit_score(p_circ, star) > orbit_score(p_ecc, star)

    def test_no_star(self):
        p = _make_planet(semi_major_axis=1.0)
        s = orbit_score(p, None)
        assert 0.0 <= s <= 1.0
