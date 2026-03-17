# EXOSCORE - Exoplanet Habitability Scorer

A Python tool that computes a multi-factor habitability index (0-1) for known exoplanets using data from the NASA Exoplanet Archive.

## Features

- **Multi-factor scoring** -- combines temperature, atmosphere, water likelihood, magnetic field, stellar stability, and orbital properties into a single habitability index
- **Habitable zone calculator** -- computes inner/outer HZ boundaries using the Kopparapu et al. (2013) model based on stellar luminosity and temperature
- **Built-in catalog** -- 50+ real exoplanets (Proxima Centauri b, TRAPPIST-1 system, Kepler candidates, and more) with their known physical properties
- **Star database** -- host stars with spectral types, luminosity, mass, temperature, and variability data
- **Rich CLI output** -- color-coded reports, factor breakdowns, and ranked tables

## Installation

```bash
pip install -e .
```

Or with dev dependencies:

```bash
pip install -e ".[dev]"
```

## Usage

### Score a single planet

```bash
exoscore score "TRAPPIST-1 e"
exoscore score "Kepler-442 b"
exoscore score "Proxima Centauri b"
```

### Rank all planets

```bash
exoscore rank
exoscore rank --top 10
```

### List catalog contents

```bash
exoscore list
exoscore list --stars
```

### Show habitable zone for a star

```bash
exoscore hz "TRAPPIST-1"
exoscore hz "Kepler-452"
```

## Scoring Factors

| Factor           | Weight | Description                                       |
|------------------|--------|---------------------------------------------------|
| Temperature      | 0.25   | Gaussian around 255 K optimal equilibrium temp     |
| Atmosphere       | 0.20   | Moderate density preferred; none or too thick penalised |
| Water            | 0.20   | Likelihood of surface liquid water                 |
| Magnetic Field   | 0.10   | Shields atmosphere from stellar wind               |
| Star Stability   | 0.10   | Low stellar variability / flare activity           |
| Orbit            | 0.15   | HZ position and eccentricity                       |

## Running Tests

```bash
pytest
pytest --cov=exoscore
```

## Project Structure

```
exoscore/
  src/exoscore/
    cli.py              # Click CLI commands
    models.py           # Pydantic models (Star, Exoplanet, HabitabilityReport)
    report.py           # Rich-formatted report rendering
    scorer/
      habitability.py   # HabitabilityScorer (composite index)
      factors.py        # Individual factor scorers
      zone.py           # HabitableZoneCalculator
    catalog/
      exoplanets.py     # ExoplanetCatalog (50+ real planets)
      stars.py          # StarDatabase (spectral types and properties)
  tests/
```

## Author

Mukunda Katta
