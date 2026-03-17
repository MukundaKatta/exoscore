"""Pydantic models for exoplanet habitability scoring."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class SpectralType(str, Enum):
    """Stellar spectral classification."""

    O = "O"
    B = "B"
    A = "A"
    F = "F"
    G = "G"
    K = "K"
    M = "M"


class Star(BaseModel):
    """Properties of a host star."""

    name: str = Field(description="Star designation")
    spectral_type: SpectralType = Field(description="Spectral classification")
    luminosity: float = Field(description="Luminosity in solar luminosities (L_sun)")
    mass: float = Field(description="Mass in solar masses (M_sun)")
    temperature: float = Field(description="Effective temperature in Kelvin")
    radius: float = Field(description="Radius in solar radii (R_sun)")
    age: Optional[float] = Field(
        default=None, description="Estimated age in billion years"
    )
    variability: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Stellar variability index 0 (stable) to 1 (highly variable)",
    )


class Exoplanet(BaseModel):
    """Properties of an exoplanet."""

    name: str = Field(description="Planet designation")
    host_star: str = Field(description="Name of the host star")
    mass: Optional[float] = Field(
        default=None, description="Mass in Earth masses (M_earth)"
    )
    radius: Optional[float] = Field(
        default=None, description="Radius in Earth radii (R_earth)"
    )
    semi_major_axis: float = Field(
        description="Orbital semi-major axis in AU"
    )
    eccentricity: float = Field(
        default=0.0, ge=0.0, le=1.0, description="Orbital eccentricity"
    )
    orbital_period: Optional[float] = Field(
        default=None, description="Orbital period in Earth days"
    )
    equilibrium_temp: Optional[float] = Field(
        default=None, description="Equilibrium temperature in Kelvin"
    )
    has_atmosphere: Optional[bool] = Field(
        default=None, description="Whether atmosphere is detected/likely"
    )
    atmosphere_density: Optional[float] = Field(
        default=None,
        ge=0.0,
        le=1.0,
        description="Estimated atmosphere density 0 (none) to 1 (very thick)",
    )
    has_magnetic_field: Optional[bool] = Field(
        default=None, description="Whether magnetic field is detected/likely"
    )
    water_likelihood: Optional[float] = Field(
        default=None,
        ge=0.0,
        le=1.0,
        description="Likelihood of surface liquid water 0-1",
    )
    discovery_year: Optional[int] = Field(
        default=None, description="Year of discovery"
    )
    discovery_method: Optional[str] = Field(
        default=None, description="Method of discovery"
    )


class FactorScore(BaseModel):
    """Score for an individual habitability factor."""

    name: str
    score: float = Field(ge=0.0, le=1.0)
    weight: float = Field(ge=0.0, le=1.0)
    description: str = ""


class HabitableZone(BaseModel):
    """Habitable zone boundaries for a star."""

    star_name: str
    inner_boundary_au: float = Field(description="Inner HZ edge in AU")
    outer_boundary_au: float = Field(description="Outer HZ edge in AU")
    conservative_inner_au: float = Field(
        description="Conservative inner HZ edge in AU"
    )
    conservative_outer_au: float = Field(
        description="Conservative outer HZ edge in AU"
    )


class HabitabilityReport(BaseModel):
    """Complete habitability assessment for an exoplanet."""

    planet: Exoplanet
    star: Optional[Star] = None
    habitable_zone: Optional[HabitableZone] = None
    overall_score: float = Field(
        ge=0.0, le=1.0, description="Composite habitability index 0-1"
    )
    factor_scores: list[FactorScore] = Field(default_factory=list)
    in_habitable_zone: bool = False
    classification: str = Field(
        default="Unknown",
        description="Habitability classification label",
    )
    summary: str = Field(default="", description="Human-readable summary")
