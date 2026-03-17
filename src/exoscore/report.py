"""Rich-formatted report rendering for habitability assessments."""

from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from exoscore.models import HabitabilityReport


def _score_color(score: float) -> str:
    """Return a Rich color name based on score value."""
    if score >= 0.8:
        return "bright_green"
    if score >= 0.6:
        return "green"
    if score >= 0.4:
        return "yellow"
    if score >= 0.2:
        return "dark_orange"
    return "red"


def _bar(score: float, width: int = 20) -> Text:
    """Create a colored bar representing a 0-1 score."""
    filled = int(round(score * width))
    color = _score_color(score)
    bar_text = Text()
    bar_text.append("█" * filled, style=color)
    bar_text.append("░" * (width - filled), style="dim")
    bar_text.append(f" {score:.2f}", style="bold " + color)
    return bar_text


def render_report(report: HabitabilityReport, console: Console | None = None) -> None:
    """Print a rich-formatted habitability report to the console."""
    if console is None:
        console = Console()

    # Header
    color = _score_color(report.overall_score)
    title = Text(f"  {report.planet.name}  ", style=f"bold white on {color}")
    console.print()
    console.print(Panel(title, expand=False, border_style=color))

    # Planet info table
    info = Table(show_header=False, box=None, padding=(0, 2))
    info.add_column("Property", style="bold cyan")
    info.add_column("Value")
    info.add_row("Host Star", report.planet.host_star)
    if report.star:
        info.add_row(
            "Spectral Type",
            f"{report.star.spectral_type.value} ({report.star.temperature} K)",
        )
    if report.planet.mass is not None:
        info.add_row("Mass", f"{report.planet.mass:.2f} Earth masses")
    if report.planet.radius is not None:
        info.add_row("Radius", f"{report.planet.radius:.2f} Earth radii")
    info.add_row("Semi-major Axis", f"{report.planet.semi_major_axis} AU")
    if report.planet.eccentricity > 0:
        info.add_row("Eccentricity", f"{report.planet.eccentricity}")
    if report.planet.equilibrium_temp is not None:
        info.add_row("Eq. Temperature", f"{report.planet.equilibrium_temp} K")
    if report.planet.orbital_period is not None:
        info.add_row("Orbital Period", f"{report.planet.orbital_period:.1f} days")
    if report.planet.discovery_year is not None:
        info.add_row("Discovered", f"{report.planet.discovery_year} ({report.planet.discovery_method})")
    console.print(info)
    console.print()

    # Habitable zone
    if report.habitable_zone:
        hz = report.habitable_zone
        hz_text = Text()
        hz_text.append("Optimistic HZ: ", style="bold")
        hz_text.append(f"{hz.inner_boundary_au:.4f} - {hz.outer_boundary_au:.4f} AU")
        hz_text.append("  |  Conservative HZ: ", style="bold")
        hz_text.append(
            f"{hz.conservative_inner_au:.4f} - {hz.conservative_outer_au:.4f} AU"
        )
        console.print(hz_text)
        status = (
            "[bold green]IN habitable zone[/]"
            if report.in_habitable_zone
            else "[bold red]OUTSIDE habitable zone[/]"
        )
        console.print(f"Planet at {report.planet.semi_major_axis} AU => {status}")
        console.print()

    # Factor scores table
    table = Table(title="Factor Scores", border_style="blue")
    table.add_column("Factor", style="bold")
    table.add_column("Score", justify="center")
    table.add_column("Weight", justify="center")
    table.add_column("Detail")

    for fs in report.factor_scores:
        table.add_row(
            fs.name.replace("_", " ").title(),
            _bar(fs.score),
            f"{fs.weight:.2f}",
            fs.description,
        )
    console.print(table)
    console.print()

    # Overall score
    overall_text = Text()
    overall_text.append("Overall Habitability: ", style="bold")
    overall_text.append_text(_bar(report.overall_score, width=30))
    overall_text.append(f"  [{report.classification}]", style="bold italic")
    console.print(Panel(overall_text, border_style=color))

    # Summary
    console.print(f"\n[dim]{report.summary}[/dim]\n")


def render_ranking(
    reports: list[HabitabilityReport], console: Console | None = None, top_n: int = 20
) -> None:
    """Print a ranked table of planets by habitability score."""
    if console is None:
        console = Console()

    sorted_reports = sorted(reports, key=lambda r: r.overall_score, reverse=True)
    if top_n > 0:
        sorted_reports = sorted_reports[:top_n]

    table = Table(title="Exoplanet Habitability Ranking", border_style="bright_blue")
    table.add_column("#", justify="right", style="dim")
    table.add_column("Planet", style="bold")
    table.add_column("Host Star")
    table.add_column("Score", justify="center")
    table.add_column("Classification")
    table.add_column("In HZ", justify="center")
    table.add_column("Eq. Temp (K)", justify="right")

    for i, r in enumerate(sorted_reports, 1):
        hz_marker = "[green]Yes[/]" if r.in_habitable_zone else "[red]No[/]"
        temp = str(r.planet.equilibrium_temp) if r.planet.equilibrium_temp else "?"
        table.add_row(
            str(i),
            r.planet.name,
            r.planet.host_star,
            _bar(r.overall_score, width=15),
            r.classification,
            hz_marker,
            temp,
        )

    console.print()
    console.print(table)
    console.print()
