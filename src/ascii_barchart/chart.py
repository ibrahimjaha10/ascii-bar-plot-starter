from rich import print

COLORS = ["green", "cyan", "yellow", "magenta"]


def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)


def render_bar_chart(values, width=40):
    print("Average value1 by type\n")

    maximum = 0
    for label, value in values:
        if value > maximum:
            maximum = value

    for i, (label, value) in enumerate(values):
        bar = "█" * scale_bar(value, maximum, width)
        color = COLORS[i % len(COLORS)]
        print(f"{label} | [{color}]{bar:<{width}}[/] {value:.2f}")
