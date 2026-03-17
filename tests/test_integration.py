"""Integration tests: score all catalog planets end-to-end."""

from exoscore.catalog.exoplanets import ExoplanetCatalog
from exoscore.catalog.stars import StarDatabase
from exoscore.scorer.habitability import HabitabilityScorer


class TestIntegration:
    def test_score_all_planets(self):
        catalog = ExoplanetCatalog()
        stars = StarDatabase()
        scorer = HabitabilityScorer()

        reports = []
        for planet in catalog.all():
            star = stars.get(planet.host_star)
            report = scorer.score(planet, star)
            reports.append(report)
            assert 0.0 <= report.overall_score <= 1.0
            assert len(report.factor_scores) == 6
            assert report.classification in (
                "Highly Promising",
                "Promising",
                "Moderate Potential",
                "Low Potential",
                "Unlikely Habitable",
            )

        assert len(reports) >= 50

    def test_trappist1e_ranks_high(self):
        catalog = ExoplanetCatalog()
        stars = StarDatabase()
        scorer = HabitabilityScorer()

        reports = []
        for planet in catalog.all():
            star = stars.get(planet.host_star)
            reports.append(scorer.score(planet, star))

        reports.sort(key=lambda r: r.overall_score, reverse=True)
        top_names = [r.planet.name for r in reports[:15]]
        assert "TRAPPIST-1 e" in top_names

    def test_hot_planets_rank_low(self):
        catalog = ExoplanetCatalog()
        stars = StarDatabase()
        scorer = HabitabilityScorer()

        hot_planets = catalog.search(min_temp=1000)
        for planet in hot_planets:
            star = stars.get(planet.host_star)
            report = scorer.score(planet, star)
            assert report.overall_score < 0.3
