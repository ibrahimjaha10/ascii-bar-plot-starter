from rich.console import Console
from rich.text import Text

COLORS = ["green", "cyan", "yellow", "magenta", "red", "blue"]


def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)


def render_bar_chart(values, width=40, title="Average value1 by type"):
    console = Console()
    console.print(f"\n{title}\n")
    if not values:
        return
    maximum = max(value for _, value in values)
    for i, (label, value) in enumerate(values):
        bar = "█" * scale_bar(value, maximum, width)
        line = Text(f"{label} | ")
        line.append(bar.ljust(width), style=COLORS[i % len(COLORS)])
        line.append(f" {value:.2f}")
        console.print(line)


if __name__ == "__main__":
    render_bar_chart([("A", 2.16), ("B", 4.33), ("C", 6.57), ("D", 8.71)])
