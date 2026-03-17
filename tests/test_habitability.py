"""Tests for the composite habitability scorer."""

import pytest

from exoscore.models import Exoplanet, SpectralType, Star
from exoscore.scorer.habitability import HabitabilityScorer


@pytest.fixture
def scorer():
    return HabitabilityScorer()


@pytest.fixture
def earth_like_planet():
    return Exoplanet(
        name="Earth-like",
        host_star="Sun-like",
        mass=1.0,
        radius=1.0,
        semi_major_axis=1.0,
        eccentricity=0.017,
        equilibrium_temp=255,
        has_atmosphere=True,
        atmosphere_density=0.5,
        has_magnetic_field=True,
        water_likelihood=0.9,
    )


@pytest.fixture
def sun_like_star():
    return Star(
        name="Sun-like",
        spectral_type=SpectralType.G,
        luminosity=1.0,
        mass=1.0,
        temperature=5778,
        radius=1.0,
        variability=0.02,
    )


@pytest.fixture
def hot_jupiter():
    return Exoplanet(
        name="Hot Jupiter",
        host_star="Sun-like",
        mass=300.0,
        radius=11.0,
        semi_major_axis=0.05,
        eccentricity=0.0,
        equilibrium_temp=1500,
        has_atmosphere=True,
        atmosphere_density=0.95,
        has_magnetic_field=True,
        water_likelihood=0.0,
    )


class TestHabitabilityScorer:
    def test_earth_like_scores_high(self, scorer, earth_like_planet, sun_like_star):
        report = scorer.score(earth_like_planet, sun_like_star)
        assert report.overall_score > 0.7
        assert report.classification in ("Highly Promising", "Promising")
        assert report.in_habitable_zone is True

    def test_hot_jupiter_scores_low(self, scorer, hot_jupiter, sun_like_star):
        report = scorer.score(hot_jupiter, sun_like_star)
        assert report.overall_score < 0.3
        assert report.in_habitable_zone is False

    def test_report_has_all_factors(self, scorer, earth_like_planet, sun_like_star):
        report = scorer.score(earth_like_planet, sun_like_star)
        factor_names = {fs.name for fs in report.factor_scores}
        expected = {"temperature", "atmosphere", "water", "magnetic_field", "star_stability", "orbit"}
        assert factor_names == expected

    def test_score_between_0_and_1(self, scorer, earth_like_planet):
        report = scorer.score(earth_like_planet)
        assert 0.0 <= report.overall_score <= 1.0

    def test_without_star(self, scorer, earth_like_planet):
        report = scorer.score(earth_like_planet, star=None)
        assert report.habitable_zone is None
        assert 0.0 <= report.overall_score <= 1.0

    def test_custom_weights(self, earth_like_planet, sun_like_star):
        # Weight everything on temperature
        scorer = HabitabilityScorer(weights={"temperature": 1.0, "atmosphere": 0.0,
                                              "water": 0.0, "magnetic_field": 0.0,
                                              "star_stability": 0.0, "orbit": 0.0})
        report = scorer.score(earth_like_planet, sun_like_star)
        # Should be very close to the temperature factor alone
        temp_fs = next(fs for fs in report.factor_scores if fs.name == "temperature")
        assert abs(report.overall_score - temp_fs.score) < 0.01

    def test_classification_tiers(self, scorer):
        assert scorer._classify(0.85) == "Highly Promising"
        assert scorer._classify(0.65) == "Promising"
        assert scorer._classify(0.45) == "Moderate Potential"
        assert scorer._classify(0.25) == "Low Potential"
        assert scorer._classify(0.10) == "Unlikely Habitable"

    def test_summary_not_empty(self, scorer, earth_like_planet, sun_like_star):
        report = scorer.score(earth_like_planet, sun_like_star)
        assert len(report.summary) > 0
        assert "Earth-like" in report.summary
