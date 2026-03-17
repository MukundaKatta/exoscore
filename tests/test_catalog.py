"""Tests for the exoplanet and star catalogs."""

from exoscore.catalog.exoplanets import ExoplanetCatalog
from exoscore.catalog.stars import StarDatabase
from exoscore.models import SpectralType


class TestExoplanetCatalog:
    def test_has_50_plus_planets(self):
        catalog = ExoplanetCatalog()
        assert catalog.count >= 50

    def test_get_known_planet(self):
        catalog = ExoplanetCatalog()
        planet = catalog.get("Proxima Centauri b")
        assert planet is not None
        assert planet.host_star == "Proxima Centauri"

    def test_get_trappist1e(self):
        catalog = ExoplanetCatalog()
        planet = catalog.get("TRAPPIST-1 e")
        assert planet is not None
        assert planet.equilibrium_temp is not None

    def test_get_kepler442b(self):
        catalog = ExoplanetCatalog()
        planet = catalog.get("Kepler-442 b")
        assert planet is not None

    def test_get_nonexistent(self):
        catalog = ExoplanetCatalog()
        assert catalog.get("Imaginary Planet") is None

    def test_list_names_sorted(self):
        catalog = ExoplanetCatalog()
        names = catalog.list_names()
        assert names == sorted(names)

    def test_by_host_star(self):
        catalog = ExoplanetCatalog()
        trappist_planets = catalog.by_host_star("TRAPPIST-1")
        assert len(trappist_planets) >= 7

    def test_search_earth_like(self):
        catalog = ExoplanetCatalog()
        results = catalog.search(min_mass=0.5, max_mass=2.0, min_temp=200, max_temp=310)
        assert len(results) > 0
        for p in results:
            assert 0.5 <= p.mass <= 2.0
            assert 200 <= p.equilibrium_temp <= 310

    def test_all_planets_valid(self):
        catalog = ExoplanetCatalog()
        for planet in catalog.all():
            assert planet.name
            assert planet.host_star
            assert planet.semi_major_axis > 0
            assert 0.0 <= planet.eccentricity <= 1.0


class TestStarDatabase:
    def test_has_stars(self):
        db = StarDatabase()
        assert db.count >= 30

    def test_get_known_star(self):
        db = StarDatabase()
        star = db.get("Proxima Centauri")
        assert star is not None
        assert star.spectral_type == SpectralType.M

    def test_get_nonexistent(self):
        db = StarDatabase()
        assert db.get("Betelgeuse") is None

    def test_by_spectral_type(self):
        db = StarDatabase()
        m_stars = db.by_spectral_type(SpectralType.M)
        assert len(m_stars) > 0
        for s in m_stars:
            assert s.spectral_type == SpectralType.M

    def test_list_names_sorted(self):
        db = StarDatabase()
        names = db.list_names()
        assert names == sorted(names)

    def test_all_stars_valid(self):
        db = StarDatabase()
        for star in db.all():
            assert star.name
            assert star.luminosity > 0
            assert star.mass > 0
            assert star.temperature > 0
            assert star.radius > 0
            assert 0.0 <= star.variability <= 1.0
