"""Exoplanet catalog with 50+ real exoplanets and their properties.

Data sourced from the NASA Exoplanet Archive. Values represent best-known
estimates as of early 2025. Where properties are uncertain or unknown,
reasonable estimates or None are used.
"""

from __future__ import annotations

from exoscore.models import Exoplanet

# fmt: off
_EXOPLANET_DATA: list[Exoplanet] = [
    # --- Potentially habitable rocky worlds ---
    Exoplanet(name="Proxima Centauri b", host_star="Proxima Centauri", mass=1.07, radius=1.03, semi_major_axis=0.0485, eccentricity=0.02, orbital_period=11.186, equilibrium_temp=234, has_atmosphere=None, atmosphere_density=0.4, has_magnetic_field=None, water_likelihood=0.3, discovery_year=2016, discovery_method="Radial Velocity"),
    Exoplanet(name="Proxima Centauri d", host_star="Proxima Centauri", mass=0.26, radius=0.81, semi_major_axis=0.02885, eccentricity=0.04, orbital_period=5.122, equilibrium_temp=360, discovery_year=2022, discovery_method="Radial Velocity"),
    Exoplanet(name="TRAPPIST-1 b", host_star="TRAPPIST-1", mass=1.374, radius=1.116, semi_major_axis=0.01154, eccentricity=0.006, orbital_period=1.511, equilibrium_temp=400, has_atmosphere=False, atmosphere_density=0.0, water_likelihood=0.0, discovery_year=2016, discovery_method="Transit"),
    Exoplanet(name="TRAPPIST-1 c", host_star="TRAPPIST-1", mass=1.308, radius=1.097, semi_major_axis=0.01580, eccentricity=0.007, orbital_period=2.422, equilibrium_temp=342, has_atmosphere=False, atmosphere_density=0.0, water_likelihood=0.0, discovery_year=2016, discovery_method="Transit"),
    Exoplanet(name="TRAPPIST-1 d", host_star="TRAPPIST-1", mass=0.388, radius=0.788, semi_major_axis=0.02227, eccentricity=0.008, orbital_period=4.050, equilibrium_temp=288, has_atmosphere=None, atmosphere_density=0.3, water_likelihood=0.4, discovery_year=2016, discovery_method="Transit"),
    Exoplanet(name="TRAPPIST-1 e", host_star="TRAPPIST-1", mass=0.692, radius=0.920, semi_major_axis=0.02925, eccentricity=0.005, orbital_period=6.101, equilibrium_temp=251, has_atmosphere=None, atmosphere_density=0.5, has_magnetic_field=None, water_likelihood=0.6, discovery_year=2016, discovery_method="Transit"),
    Exoplanet(name="TRAPPIST-1 f", host_star="TRAPPIST-1", mass=1.039, radius=1.045, semi_major_axis=0.03849, eccentricity=0.010, orbital_period=9.207, equilibrium_temp=219, has_atmosphere=None, atmosphere_density=0.4, water_likelihood=0.4, discovery_year=2016, discovery_method="Transit"),
    Exoplanet(name="TRAPPIST-1 g", host_star="TRAPPIST-1", mass=1.321, radius=1.129, semi_major_axis=0.04683, eccentricity=0.002, orbital_period=12.353, equilibrium_temp=199, has_atmosphere=None, atmosphere_density=0.3, water_likelihood=0.2, discovery_year=2016, discovery_method="Transit"),
    Exoplanet(name="TRAPPIST-1 h", host_star="TRAPPIST-1", mass=0.326, radius=0.755, semi_major_axis=0.06189, eccentricity=0.006, orbital_period=18.767, equilibrium_temp=173, has_atmosphere=None, atmosphere_density=0.1, water_likelihood=0.05, discovery_year=2016, discovery_method="Transit"),
    Exoplanet(name="Kepler-442 b", host_star="Kepler-442", mass=2.36, radius=1.34, semi_major_axis=0.409, eccentricity=0.04, orbital_period=112.3, equilibrium_temp=233, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.5, discovery_year=2015, discovery_method="Transit"),
    Exoplanet(name="Kepler-452 b", host_star="Kepler-452", mass=5.0, radius=1.63, semi_major_axis=1.046, eccentricity=0.035, orbital_period=384.8, equilibrium_temp=265, has_atmosphere=None, atmosphere_density=0.6, water_likelihood=0.5, discovery_year=2015, discovery_method="Transit"),
    Exoplanet(name="Kepler-186 f", host_star="Kepler-186", mass=1.71, radius=1.17, semi_major_axis=0.432, eccentricity=0.04, orbital_period=129.9, equilibrium_temp=188, has_atmosphere=None, atmosphere_density=0.4, water_likelihood=0.4, discovery_year=2014, discovery_method="Transit"),
    Exoplanet(name="Kepler-22 b", host_star="Kepler-22", mass=9.1, radius=2.38, semi_major_axis=0.849, eccentricity=0.0, orbital_period=289.9, equilibrium_temp=262, has_atmosphere=None, atmosphere_density=0.7, water_likelihood=0.5, discovery_year=2011, discovery_method="Transit"),
    Exoplanet(name="Kepler-62 e", host_star="Kepler-62", mass=4.8, radius=1.61, semi_major_axis=0.427, eccentricity=0.0, orbital_period=122.4, equilibrium_temp=270, has_atmosphere=None, atmosphere_density=0.6, water_likelihood=0.6, discovery_year=2013, discovery_method="Transit"),
    Exoplanet(name="Kepler-62 f", host_star="Kepler-62", mass=2.8, radius=1.41, semi_major_axis=0.718, eccentricity=0.0, orbital_period=267.3, equilibrium_temp=208, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.4, discovery_year=2013, discovery_method="Transit"),
    Exoplanet(name="Kepler-438 b", host_star="Kepler-438", mass=1.46, radius=1.12, semi_major_axis=0.166, eccentricity=0.03, orbital_period=35.23, equilibrium_temp=276, has_atmosphere=None, atmosphere_density=0.3, water_likelihood=0.3, discovery_year=2015, discovery_method="Transit"),
    Exoplanet(name="Kepler-296 e", host_star="Kepler-296", mass=2.0, radius=1.48, semi_major_axis=0.169, eccentricity=0.0, orbital_period=34.14, equilibrium_temp=275, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.4, discovery_year=2014, discovery_method="Transit"),
    Exoplanet(name="Kepler-296 f", host_star="Kepler-296", mass=1.8, radius=1.79, semi_major_axis=0.255, eccentricity=0.0, orbital_period=63.34, equilibrium_temp=224, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.3, discovery_year=2014, discovery_method="Transit"),
    Exoplanet(name="Kepler-1229 b", host_star="Kepler-1229", mass=2.7, radius=1.40, semi_major_axis=0.2896, eccentricity=0.0, orbital_period=86.83, equilibrium_temp=213, has_atmosphere=None, atmosphere_density=0.4, water_likelihood=0.4, discovery_year=2016, discovery_method="Transit"),
    Exoplanet(name="Kepler-1649 c", host_star="Kepler-1649", mass=1.2, radius=1.06, semi_major_axis=0.0649, eccentricity=0.0, orbital_period=19.54, equilibrium_temp=234, has_atmosphere=None, atmosphere_density=0.4, water_likelihood=0.5, discovery_year=2020, discovery_method="Transit"),
    Exoplanet(name="Kepler-283 c", host_star="Kepler-283", mass=3.0, radius=1.82, semi_major_axis=0.341, eccentricity=0.0, orbital_period=92.74, equilibrium_temp=248, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.4, discovery_year=2014, discovery_method="Transit"),
    Exoplanet(name="Kepler-440 b", host_star="Kepler-440", mass=3.2, radius=1.86, semi_major_axis=0.242, eccentricity=0.0, orbital_period=101.1, equilibrium_temp=273, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.5, discovery_year=2015, discovery_method="Transit"),
    Exoplanet(name="Kepler-443 b", host_star="Kepler-443", mass=3.3, radius=1.64, semi_major_axis=0.495, eccentricity=0.11, orbital_period=177.7, equilibrium_temp=233, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.4, discovery_year=2015, discovery_method="Transit"),
    Exoplanet(name="Kepler-1544 b", host_star="Kepler-1544", mass=4.0, radius=1.78, semi_major_axis=0.4416, eccentricity=0.0, orbital_period=168.8, equilibrium_temp=248, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.4, discovery_year=2016, discovery_method="Transit"),
    Exoplanet(name="Ross 128 b", host_star="Ross 128", mass=1.40, radius=1.10, semi_major_axis=0.0496, eccentricity=0.036, orbital_period=9.866, equilibrium_temp=256, has_atmosphere=None, atmosphere_density=0.5, has_magnetic_field=None, water_likelihood=0.5, discovery_year=2017, discovery_method="Radial Velocity"),
    Exoplanet(name="LHS 1140 b", host_star="LHS 1140", mass=5.60, radius=1.73, semi_major_axis=0.0946, eccentricity=0.0, orbital_period=24.74, equilibrium_temp=235, has_atmosphere=True, atmosphere_density=0.6, water_likelihood=0.6, discovery_year=2017, discovery_method="Transit"),
    Exoplanet(name="GJ 667 C c", host_star="GJ 667 C", mass=3.81, radius=1.54, semi_major_axis=0.125, eccentricity=0.02, orbital_period=28.14, equilibrium_temp=277, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.5, discovery_year=2011, discovery_method="Radial Velocity"),
    Exoplanet(name="GJ 667 C f", host_star="GJ 667 C", mass=2.7, radius=1.4, semi_major_axis=0.156, eccentricity=0.03, orbital_period=39.03, equilibrium_temp=248, has_atmosphere=None, atmosphere_density=0.4, water_likelihood=0.4, discovery_year=2013, discovery_method="Radial Velocity"),
    Exoplanet(name="GJ 357 d", host_star="GJ 357", mass=6.1, radius=1.84, semi_major_axis=0.204, eccentricity=0.07, orbital_period=55.66, equilibrium_temp=220, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.4, discovery_year=2019, discovery_method="Radial Velocity"),
    Exoplanet(name="GJ 273 b", host_star="GJ 273", mass=2.89, radius=1.51, semi_major_axis=0.091, eccentricity=0.10, orbital_period=18.65, equilibrium_temp=259, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.5, discovery_year=2017, discovery_method="Radial Velocity"),
    Exoplanet(name="Tau Ceti e", host_star="Tau Ceti", mass=3.93, radius=1.59, semi_major_axis=0.538, eccentricity=0.18, orbital_period=163.0, equilibrium_temp=270, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.4, discovery_year=2012, discovery_method="Radial Velocity"),
    Exoplanet(name="Tau Ceti f", host_star="Tau Ceti", mass=3.93, radius=1.59, semi_major_axis=1.334, eccentricity=0.16, orbital_period=636.0, equilibrium_temp=171, has_atmosphere=None, atmosphere_density=0.4, water_likelihood=0.2, discovery_year=2012, discovery_method="Radial Velocity"),
    Exoplanet(name="Teegarden's Star b", host_star="Teegarden's Star", mass=1.05, radius=1.02, semi_major_axis=0.0252, eccentricity=0.0, orbital_period=4.91, equilibrium_temp=264, has_atmosphere=None, atmosphere_density=0.4, water_likelihood=0.5, discovery_year=2019, discovery_method="Radial Velocity"),
    Exoplanet(name="Teegarden's Star c", host_star="Teegarden's Star", mass=1.11, radius=1.04, semi_major_axis=0.0443, eccentricity=0.0, orbital_period=11.41, equilibrium_temp=199, has_atmosphere=None, atmosphere_density=0.3, water_likelihood=0.3, discovery_year=2019, discovery_method="Radial Velocity"),
    Exoplanet(name="TOI-700 d", host_star="TOI-700", mass=1.72, radius=1.19, semi_major_axis=0.163, eccentricity=0.0, orbital_period=37.43, equilibrium_temp=269, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.5, discovery_year=2020, discovery_method="Transit"),
    Exoplanet(name="TOI-700 e", host_star="TOI-700", mass=0.95, radius=0.953, semi_major_axis=0.134, eccentricity=0.0, orbital_period=28.43, equilibrium_temp=280, has_atmosphere=None, atmosphere_density=0.4, water_likelihood=0.5, discovery_year=2023, discovery_method="Transit"),
    Exoplanet(name="TOI-1452 b", host_star="TOI-1452", mass=4.82, radius=1.67, semi_major_axis=0.061, eccentricity=0.0, orbital_period=11.07, equilibrium_temp=326, has_atmosphere=None, atmosphere_density=0.6, water_likelihood=0.7, discovery_year=2022, discovery_method="Transit"),
    Exoplanet(name="K2-18 b", host_star="K2-18", mass=8.63, radius=2.61, semi_major_axis=0.1429, eccentricity=0.0, orbital_period=32.94, equilibrium_temp=255, has_atmosphere=True, atmosphere_density=0.7, water_likelihood=0.7, discovery_year=2015, discovery_method="Transit"),
    Exoplanet(name="HD 40307 g", host_star="HD 40307", mass=7.09, radius=1.94, semi_major_axis=0.600, eccentricity=0.22, orbital_period=197.8, equilibrium_temp=250, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.4, discovery_year=2012, discovery_method="Radial Velocity"),
    Exoplanet(name="Wolf 1061 c", host_star="Wolf 1061", mass=3.41, radius=1.55, semi_major_axis=0.084, eccentricity=0.11, orbital_period=17.87, equilibrium_temp=271, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.4, discovery_year=2015, discovery_method="Radial Velocity"),
    Exoplanet(name="Gliese 581 d", host_star="Gliese 581", mass=6.98, radius=1.92, semi_major_axis=0.218, eccentricity=0.25, orbital_period=66.87, equilibrium_temp=220, has_atmosphere=None, atmosphere_density=0.6, water_likelihood=0.3, discovery_year=2007, discovery_method="Radial Velocity"),
    Exoplanet(name="Gliese 581 g", host_star="Gliese 581", mass=3.1, radius=1.52, semi_major_axis=0.146, eccentricity=0.0, orbital_period=36.56, equilibrium_temp=254, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.5, discovery_year=2010, discovery_method="Radial Velocity"),
    Exoplanet(name="Gliese 163 c", host_star="Gliese 163", mass=6.8, radius=1.90, semi_major_axis=0.125, eccentricity=0.1, orbital_period=25.63, equilibrium_temp=277, has_atmosphere=None, atmosphere_density=0.6, water_likelihood=0.4, discovery_year=2012, discovery_method="Radial Velocity"),
    Exoplanet(name="Gliese 832 c", host_star="Gliese 832", mass=5.4, radius=1.76, semi_major_axis=0.162, eccentricity=0.18, orbital_period=35.68, equilibrium_temp=253, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.4, discovery_year=2014, discovery_method="Radial Velocity"),
    Exoplanet(name="HD 85512 b", host_star="HD 85512", mass=3.6, radius=1.58, semi_major_axis=0.26, eccentricity=0.11, orbital_period=58.43, equilibrium_temp=283, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.4, discovery_year=2011, discovery_method="Radial Velocity"),
    Exoplanet(name="Kepler-69 c", host_star="Kepler-69", mass=6.0, radius=1.71, semi_major_axis=0.64, eccentricity=0.14, orbital_period=242.5, equilibrium_temp=299, has_atmosphere=None, atmosphere_density=0.6, water_likelihood=0.3, discovery_year=2013, discovery_method="Transit"),
    Exoplanet(name="GJ 1002 b", host_star="GJ 1002", mass=1.08, radius=1.03, semi_major_axis=0.0457, eccentricity=0.0, orbital_period=10.35, equilibrium_temp=231, has_atmosphere=None, atmosphere_density=0.4, water_likelihood=0.5, discovery_year=2022, discovery_method="Radial Velocity"),
    Exoplanet(name="GJ 1002 c", host_star="GJ 1002", mass=1.36, radius=1.11, semi_major_axis=0.0738, eccentricity=0.0, orbital_period=21.20, equilibrium_temp=182, has_atmosphere=None, atmosphere_density=0.3, water_likelihood=0.3, discovery_year=2022, discovery_method="Radial Velocity"),
    Exoplanet(name="GJ 1061 c", host_star="GJ 1061", mass=1.74, radius=1.18, semi_major_axis=0.035, eccentricity=0.0, orbital_period=6.69, equilibrium_temp=275, has_atmosphere=None, atmosphere_density=0.4, water_likelihood=0.4, discovery_year=2019, discovery_method="Radial Velocity"),
    Exoplanet(name="GJ 1061 d", host_star="GJ 1061", mass=1.64, radius=1.16, semi_major_axis=0.054, eccentricity=0.0, orbital_period=13.03, equilibrium_temp=218, has_atmosphere=None, atmosphere_density=0.4, water_likelihood=0.3, discovery_year=2019, discovery_method="Radial Velocity"),
    Exoplanet(name="LP 890-9 c", host_star="LP 890-9", mass=1.3, radius=1.37, semi_major_axis=0.03984, eccentricity=0.0, orbital_period=8.46, equilibrium_temp=272, has_atmosphere=None, atmosphere_density=0.4, water_likelihood=0.5, discovery_year=2022, discovery_method="Transit"),
    Exoplanet(name="Kepler-1638 b", host_star="Kepler-1638", mass=5.0, radius=1.60, semi_major_axis=1.038, eccentricity=0.0, orbital_period=383.9, equilibrium_temp=263, has_atmosphere=None, atmosphere_density=0.6, water_likelihood=0.5, discovery_year=2016, discovery_method="Transit"),
    Exoplanet(name="Kepler-1606 b", host_star="Kepler-1606", mass=4.5, radius=1.88, semi_major_axis=0.641, eccentricity=0.0, orbital_period=196.4, equilibrium_temp=262, has_atmosphere=None, atmosphere_density=0.5, water_likelihood=0.4, discovery_year=2016, discovery_method="Transit"),
    Exoplanet(name="Kepler-560 b", host_star="Kepler-560", mass=2.0, radius=1.50, semi_major_axis=0.1085, eccentricity=0.0, orbital_period=18.48, equilibrium_temp=273, has_atmosphere=None, atmosphere_density=0.4, water_likelihood=0.4, discovery_year=2016, discovery_method="Transit"),
    # --- Notable non-habitable but famous exoplanets ---
    Exoplanet(name="Kepler-90 h", host_star="Kepler-90", mass=203.0, radius=11.32, semi_major_axis=1.01, eccentricity=0.01, orbital_period=331.6, equilibrium_temp=292, has_atmosphere=True, atmosphere_density=0.9, water_likelihood=0.0, discovery_year=2013, discovery_method="Transit"),
    Exoplanet(name="Kepler-10 b", host_star="Kepler-10", mass=4.56, radius=1.47, semi_major_axis=0.01684, eccentricity=0.0, orbital_period=0.837, equilibrium_temp=2169, has_atmosphere=False, atmosphere_density=0.0, water_likelihood=0.0, discovery_year=2011, discovery_method="Transit"),
    Exoplanet(name="Kepler-20 e", host_star="Kepler-20", mass=0.65, radius=0.87, semi_major_axis=0.0507, eccentricity=0.0, orbital_period=6.099, equilibrium_temp=1040, has_atmosphere=False, atmosphere_density=0.0, water_likelihood=0.0, discovery_year=2011, discovery_method="Transit"),
    Exoplanet(name="55 Cancri e", host_star="55 Cancri", mass=7.99, radius=1.88, semi_major_axis=0.01544, eccentricity=0.05, orbital_period=0.737, equilibrium_temp=2573, has_atmosphere=True, atmosphere_density=0.3, water_likelihood=0.0, discovery_year=2004, discovery_method="Radial Velocity"),
    Exoplanet(name="HD 219134 b", host_star="HD 219134", mass=4.74, radius=1.60, semi_major_axis=0.0388, eccentricity=0.0, orbital_period=3.093, equilibrium_temp=1015, has_atmosphere=None, atmosphere_density=0.2, water_likelihood=0.0, discovery_year=2015, discovery_method="Radial Velocity"),
    Exoplanet(name="Kepler-37 b", host_star="Kepler-37", mass=0.02, radius=0.303, semi_major_axis=0.1003, eccentricity=0.08, orbital_period=13.37, equilibrium_temp=700, has_atmosphere=False, atmosphere_density=0.0, water_likelihood=0.0, discovery_year=2013, discovery_method="Transit"),
    Exoplanet(name="Kepler-11 b", host_star="Kepler-11", mass=4.3, radius=1.97, semi_major_axis=0.091, eccentricity=0.045, orbital_period=10.30, equilibrium_temp=900, has_atmosphere=True, atmosphere_density=0.7, water_likelihood=0.0, discovery_year=2010, discovery_method="Transit"),
]
# fmt: on


class ExoplanetCatalog:
    """Catalog of known exoplanets with physical and orbital properties."""

    def __init__(self) -> None:
        self._planets: dict[str, Exoplanet] = {p.name: p for p in _EXOPLANET_DATA}

    @property
    def count(self) -> int:
        return len(self._planets)

    def get(self, name: str) -> Exoplanet | None:
        """Look up a planet by name."""
        return self._planets.get(name)

    def list_names(self) -> list[str]:
        """Return all planet names sorted alphabetically."""
        return sorted(self._planets.keys())

    def by_host_star(self, star_name: str) -> list[Exoplanet]:
        """Return all planets orbiting a given star."""
        return [p for p in self._planets.values() if p.host_star == star_name]

    def search(
        self,
        min_mass: float | None = None,
        max_mass: float | None = None,
        min_radius: float | None = None,
        max_radius: float | None = None,
        min_temp: float | None = None,
        max_temp: float | None = None,
    ) -> list[Exoplanet]:
        """Filter planets by property ranges."""
        results = list(self._planets.values())
        if min_mass is not None:
            results = [p for p in results if p.mass is not None and p.mass >= min_mass]
        if max_mass is not None:
            results = [p for p in results if p.mass is not None and p.mass <= max_mass]
        if min_radius is not None:
            results = [p for p in results if p.radius is not None and p.radius >= min_radius]
        if max_radius is not None:
            results = [p for p in results if p.radius is not None and p.radius <= max_radius]
        if min_temp is not None:
            results = [p for p in results if p.equilibrium_temp is not None and p.equilibrium_temp >= min_temp]
        if max_temp is not None:
            results = [p for p in results if p.equilibrium_temp is not None and p.equilibrium_temp <= max_temp]
        return results

    def all(self) -> list[Exoplanet]:
        """Return all planets."""
        return list(self._planets.values())
