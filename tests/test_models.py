"""Tests for pydantic models."""

import pytest
from pydantic import ValidationError

from exoscore.models import (
    Exoplanet,
    FactorScore,
    HabitabilityReport,
    HabitableZone,
    SpectralType,
    Star,
)


class TestStar:
    def test_create_star(self):
        star = Star(
            name="Test Star",
            spectral_type=SpectralType.G,
            luminosity=1.0,
            mass=1.0,
            temperature=5778,
            radius=1.0,
        )
        assert star.name == "Test Star"
        assert star.spectral_type == SpectralType.G
        assert star.variability == 0.0

    def test_variability_bounds(self):
        with pytest.raises(ValidationError):
            Star(
                name="X",
                spectral_type=SpectralType.M,
                luminosity=0.01,
                mass=0.1,
                temperature=3000,
                radius=0.1,
                variability=1.5,
            )


class TestExoplanet:
    def test_create_planet(self):
        planet = Exoplanet(
            name="Test Planet",
            host_star="Test Star",
            semi_major_axis=1.0,
        )
        assert planet.name == "Test Planet"
        assert planet.eccentricity == 0.0

    def test_eccentricity_bounds(self):
        with pytest.raises(ValidationError):
            Exoplanet(
                name="X",
                host_star="Y",
                semi_major_axis=1.0,
                eccentricity=1.5,
            )


class TestFactorScore:
    def test_score_bounds(self):
        fs = FactorScore(name="test", score=0.5, weight=0.2)
        assert fs.score == 0.5

        with pytest.raises(ValidationError):
            FactorScore(name="test", score=1.5, weight=0.2)


class TestHabitableZone:
    def test_create(self):
        hz = HabitableZone(
            star_name="Sun",
            inner_boundary_au=0.75,
            outer_boundary_au=1.77,
            conservative_inner_au=0.95,
            conservative_outer_au=1.67,
        )
        assert hz.inner_boundary_au < hz.outer_boundary_au


class TestHabitabilityReport:
    def test_score_clamped(self):
        planet = Exoplanet(name="P", host_star="S", semi_major_axis=1.0)
        report = HabitabilityReport(
            planet=planet,
            overall_score=0.75,
            classification="Promising",
        )
        assert 0.0 <= report.overall_score <= 1.0
