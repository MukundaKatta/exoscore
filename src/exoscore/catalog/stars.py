"""Star database with spectral types and properties.

Data sourced from NASA Exoplanet Archive and stellar catalogs.
"""

from __future__ import annotations

from exoscore.models import SpectralType, Star

# fmt: off
_STAR_DATA: list[Star] = [
    Star(name="Proxima Centauri", spectral_type=SpectralType.M, luminosity=0.0017, mass=0.122, temperature=3042, radius=0.154, age=4.85, variability=0.6),
    Star(name="TRAPPIST-1", spectral_type=SpectralType.M, luminosity=0.000524, mass=0.089, temperature=2566, radius=0.121, age=7.6, variability=0.3),
    Star(name="Kepler-442", spectral_type=SpectralType.K, luminosity=0.212, mass=0.61, temperature=4402, radius=0.598, age=2.9, variability=0.1),
    Star(name="Kepler-452", spectral_type=SpectralType.G, luminosity=1.2, mass=1.037, temperature=5757, radius=1.11, age=6.0, variability=0.05),
    Star(name="Kepler-186", spectral_type=SpectralType.M, luminosity=0.041, mass=0.544, temperature=3788, radius=0.523, age=4.0, variability=0.15),
    Star(name="Kepler-22", spectral_type=SpectralType.G, luminosity=0.79, mass=0.97, temperature=5518, radius=0.979, age=4.0, variability=0.05),
    Star(name="Kepler-62", spectral_type=SpectralType.K, luminosity=0.21, mass=0.69, temperature=4925, radius=0.64, age=7.0, variability=0.08),
    Star(name="Kepler-438", spectral_type=SpectralType.M, luminosity=0.044, mass=0.544, temperature=3748, radius=0.520, age=4.4, variability=0.7),
    Star(name="Kepler-296", spectral_type=SpectralType.M, luminosity=0.026, mass=0.498, temperature=3572, radius=0.480, age=5.0, variability=0.2),
    Star(name="Kepler-1229", spectral_type=SpectralType.M, luminosity=0.025, mass=0.46, temperature=3724, radius=0.450, age=5.0, variability=0.15),
    Star(name="Kepler-1649", spectral_type=SpectralType.M, luminosity=0.0026, mass=0.198, temperature=3240, radius=0.230, age=5.0, variability=0.25),
    Star(name="Kepler-283", spectral_type=SpectralType.K, luminosity=0.11, mass=0.596, temperature=4351, radius=0.556, age=6.0, variability=0.1),
    Star(name="Kepler-440", spectral_type=SpectralType.K, luminosity=0.132, mass=0.578, temperature=4134, radius=0.560, age=5.0, variability=0.12),
    Star(name="Kepler-443", spectral_type=SpectralType.K, luminosity=0.17, mass=0.74, temperature=4723, radius=0.710, age=5.5, variability=0.1),
    Star(name="Kepler-1544", spectral_type=SpectralType.K, luminosity=0.22, mass=0.81, temperature=4977, radius=0.780, age=5.0, variability=0.08),
    Star(name="Ross 128", spectral_type=SpectralType.M, luminosity=0.00362, mass=0.168, temperature=3192, radius=0.197, age=9.45, variability=0.05),
    Star(name="LHS 1140", spectral_type=SpectralType.M, luminosity=0.00441, mass=0.179, temperature=3216, radius=0.206, age=5.0, variability=0.1),
    Star(name="GJ 667 C", spectral_type=SpectralType.M, luminosity=0.0137, mass=0.33, temperature=3350, radius=0.337, age=2.0, variability=0.15),
    Star(name="GJ 357", spectral_type=SpectralType.M, luminosity=0.016, mass=0.342, temperature=3505, radius=0.337, age=5.0, variability=0.1),
    Star(name="GJ 273", spectral_type=SpectralType.M, luminosity=0.00882, mass=0.29, temperature=3382, radius=0.293, age=5.0, variability=0.1),
    Star(name="Tau Ceti", spectral_type=SpectralType.G, luminosity=0.488, mass=0.783, temperature=5344, radius=0.793, age=5.8, variability=0.03),
    Star(name="Teegarden's Star", spectral_type=SpectralType.M, luminosity=0.00073, mass=0.089, temperature=2904, radius=0.107, age=8.0, variability=0.2),
    Star(name="TOI-700", spectral_type=SpectralType.M, luminosity=0.0233, mass=0.415, temperature=3480, radius=0.420, age=1.5, variability=0.08),
    Star(name="TOI-1452", spectral_type=SpectralType.M, luminosity=0.012, mass=0.275, temperature=3185, radius=0.275, age=5.0, variability=0.1),
    Star(name="K2-18", spectral_type=SpectralType.M, luminosity=0.00328, mass=0.359, temperature=3457, radius=0.411, age=5.0, variability=0.12),
    Star(name="HD 40307", spectral_type=SpectralType.K, luminosity=0.23, mass=0.77, temperature=4977, radius=0.716, age=1.2, variability=0.05),
    Star(name="Wolf 1061", spectral_type=SpectralType.M, luminosity=0.00958, mass=0.294, temperature=3342, radius=0.305, age=5.0, variability=0.1),
    Star(name="Gliese 581", spectral_type=SpectralType.M, luminosity=0.013, mass=0.31, temperature=3498, radius=0.299, age=8.0, variability=0.15),
    Star(name="Gliese 163", spectral_type=SpectralType.M, luminosity=0.022, mass=0.40, temperature=3500, radius=0.400, age=5.0, variability=0.1),
    Star(name="Gliese 832", spectral_type=SpectralType.M, luminosity=0.026, mass=0.45, temperature=3620, radius=0.480, age=9.24, variability=0.1),
    Star(name="HD 85512", spectral_type=SpectralType.K, luminosity=0.126, mass=0.69, temperature=4715, radius=0.533, age=5.61, variability=0.05),
    Star(name="Kepler-69", spectral_type=SpectralType.G, luminosity=0.80, mass=0.81, temperature=5638, radius=0.930, age=4.0, variability=0.06),
    Star(name="Kepler-90", spectral_type=SpectralType.G, luminosity=1.2, mass=1.13, temperature=6080, radius=1.20, age=2.0, variability=0.05),
    Star(name="Kepler-10", spectral_type=SpectralType.G, luminosity=1.003, mass=0.91, temperature=5708, radius=1.065, age=10.6, variability=0.04),
    Star(name="Kepler-20", spectral_type=SpectralType.G, luminosity=0.93, mass=0.912, temperature=5495, radius=0.944, age=8.8, variability=0.05),
    Star(name="55 Cancri", spectral_type=SpectralType.G, luminosity=0.582, mass=0.905, temperature=5196, radius=0.943, age=10.2, variability=0.04),
    Star(name="HD 219134", spectral_type=SpectralType.K, luminosity=0.265, mass=0.81, temperature=4699, radius=0.778, age=11.0, variability=0.04),
    Star(name="Kepler-37", spectral_type=SpectralType.G, luminosity=0.87, mass=0.803, temperature=5417, radius=0.770, age=6.0, variability=0.04),
    Star(name="Kepler-11", spectral_type=SpectralType.G, luminosity=1.05, mass=0.961, temperature=5680, radius=1.065, age=8.0, variability=0.05),
    Star(name="GJ 1002", spectral_type=SpectralType.M, luminosity=0.00095, mass=0.12, temperature=3024, radius=0.137, age=5.0, variability=0.15),
    Star(name="GJ 1061", spectral_type=SpectralType.M, luminosity=0.00165, mass=0.120, temperature=2953, radius=0.156, age=7.0, variability=0.12),
    Star(name="LP 890-9", spectral_type=SpectralType.M, luminosity=0.00143, mass=0.118, temperature=2871, radius=0.150, age=5.0, variability=0.15),
    Star(name="Kepler-1638", spectral_type=SpectralType.G, luminosity=1.15, mass=1.03, temperature=5773, radius=1.05, age=4.5, variability=0.04),
    Star(name="Kepler-1606", spectral_type=SpectralType.G, luminosity=0.96, mass=0.95, temperature=5600, radius=0.96, age=5.0, variability=0.05),
    Star(name="Kepler-560", spectral_type=SpectralType.M, luminosity=0.018, mass=0.46, temperature=3697, radius=0.440, age=5.0, variability=0.15),
]
# fmt: on


class StarDatabase:
    """Database of host stars with their physical properties."""

    def __init__(self) -> None:
        self._stars: dict[str, Star] = {s.name: s for s in _STAR_DATA}

    @property
    def count(self) -> int:
        return len(self._stars)

    def get(self, name: str) -> Star | None:
        """Look up a star by name."""
        return self._stars.get(name)

    def list_names(self) -> list[str]:
        """Return all star names sorted alphabetically."""
        return sorted(self._stars.keys())

    def by_spectral_type(self, spectral_type: SpectralType) -> list[Star]:
        """Return stars of a given spectral type."""
        return [s for s in self._stars.values() if s.spectral_type == spectral_type]

    def all(self) -> list[Star]:
        """Return all stars."""
        return list(self._stars.values())
