"""Command-line interface for EXOSCORE."""

from __future__ import annotations

import click
from rich.console import Console

from exoscore.catalog.exoplanets import ExoplanetCatalog
from exoscore.catalog.stars import StarDatabase
from exoscore.report import render_ranking, render_report
from exoscore.scorer.habitability import HabitabilityScorer


@click.group()
@click.version_option(package_name="exoscore")
def main() -> None:
    """EXOSCORE - Exoplanet Habitability Scorer.

    Computes a multi-factor habitability index (0-1) for known exoplanets
    using temperature, atmosphere, water, magnetic field, stellar stability,
    and orbital properties.
    """


@main.command()
@click.argument("planet_name")
def score(planet_name: str) -> None:
    """Score a single exoplanet by name.

    Example: exoscore score "TRAPPIST-1 e"
    """
    console = Console()
    catalog = ExoplanetCatalog()
    stars = StarDatabase()
    scorer = HabitabilityScorer()

    planet = catalog.get(planet_name)
    if planet is None:
        console.print(f"[red]Planet '{planet_name}' not found in catalog.[/]")
        console.print(f"Available planets ({catalog.count}):")
        for name in catalog.list_names():
            console.print(f"  {name}")
        raise SystemExit(1)

    star = stars.get(planet.host_star)
    report = scorer.score(planet, star)
    render_report(report, console)


@main.command()
@click.option("--top", "-n", default=20, help="Number of top planets to show.")
def rank(top: int) -> None:
    """Rank all cataloged exoplanets by habitability score."""
    catalog = ExoplanetCatalog()
    stars = StarDatabase()
    scorer = HabitabilityScorer()
    console = Console()

    reports = []
    for planet in catalog.all():
        star = stars.get(planet.host_star)
        report = scorer.score(planet, star)
        reports.append(report)

    render_ranking(reports, console, top_n=top)


@main.command(name="list")
@click.option("--stars", "show_stars", is_flag=True, help="List stars instead of planets.")
def list_cmd(show_stars: bool) -> None:
    """List all planets or stars in the catalog."""
    console = Console()
    if show_stars:
        db = StarDatabase()
        console.print(f"\n[bold]Stars in database ({db.count}):[/]\n")
        for name in db.list_names():
            star = db.get(name)
            if star:
                console.print(
                    f"  {name:25s}  {star.spectral_type.value}  "
                    f"L={star.luminosity:.4f} L_sun  T={star.temperature} K"
                )
    else:
        catalog = ExoplanetCatalog()
        console.print(f"\n[bold]Exoplanets in catalog ({catalog.count}):[/]\n")
        for name in catalog.list_names():
            planet = catalog.get(name)
            if planet:
                temp = f"{planet.equilibrium_temp} K" if planet.equilibrium_temp else "?"
                console.print(
                    f"  {name:30s}  a={planet.semi_major_axis:.4f} AU  T_eq={temp}"
                )
    console.print()


@main.command()
@click.argument("star_name")
def hz(star_name: str) -> None:
    """Show habitable zone boundaries for a star.

    Example: exoscore hz "TRAPPIST-1"
    """
    console = Console()
    stars = StarDatabase()
    star = stars.get(star_name)
    if star is None:
        console.print(f"[red]Star '{star_name}' not found.[/]")
        raise SystemExit(1)

    from exoscore.scorer.zone import HabitableZoneCalculator

    zone = HabitableZoneCalculator.compute(star)
    console.print(f"\n[bold]{star.name}[/] (spectral type {star.spectral_type.value})")
    console.print(f"  Luminosity:  {star.luminosity} L_sun")
    console.print(f"  Temperature: {star.temperature} K\n")
    console.print(f"  Optimistic HZ:    {zone.inner_boundary_au:.4f} - {zone.outer_boundary_au:.4f} AU")
    console.print(f"  Conservative HZ:  {zone.conservative_inner_au:.4f} - {zone.conservative_outer_au:.4f} AU\n")

    catalog = ExoplanetCatalog()
    planets = catalog.by_host_star(star_name)
    if planets:
        console.print("[bold]Planets in system:[/]")
        for p in planets:
            in_hz = zone.inner_boundary_au <= p.semi_major_axis <= zone.outer_boundary_au
            marker = "[green]IN HZ[/]" if in_hz else "[red]outside HZ[/]"
            console.print(f"  {p.name:30s}  a={p.semi_major_axis:.4f} AU  {marker}")
        console.print()


if __name__ == "__main__":
    main()
