import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from random import uniform, random
import colorsys
from typing import Tuple

from config import BACKGROUND_COLOR, Y_AXIS_SCALE


def generate_color() -> Tuple[float, float, float]:
    h = random()
    s = uniform(0.7, 1.0)
    v = uniform(0.7, 1.0)
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return (r, g, b)


def plot(
    phone_list: list[Tuple[np.ndarray, np.ndarray]],
    show_area: bool = False,
    center: bool = False,
    color=None,
    phone_names: list = [],
    phone_name: str = "",  # If only one label needed (e.g: centered delta)
    center_y_axis: bool = True
) -> None:
    """Plots a frequency-response curve."""
    # Center the phones
    if center:
        centered_data = []
        for (frequencies, dbs) in phone_list:
            shift = np.mean(dbs)  # average offset
            centered_data.append((frequencies, dbs - shift))
        phone_list = centered_data

    # Plot
    fig, ax = plt.subplots(figsize=(16, 9))

    # Background color
    ax.set_facecolor(BACKGROUND_COLOR)
    fig.patch.set_facecolor(BACKGROUND_COLOR)

    # Data
    all_dbs = []
    for i, (frequencies, dbs) in enumerate(phone_list):
        all_dbs.extend(dbs)
        if not color:
            phone_color = generate_color()

        # Label in legend
        if phone_name:
            label = phone_name if i == 0 else None
        else:
            label = phone_names[i]

        ax.plot(
            frequencies,
            dbs,
            color=color if color else phone_color,
            linewidth=2,
            label=label,
        )

        # Color delta area if wanted
        if show_area:
            ax.fill_between(
                frequencies,
                dbs,
                0,
                color=color if color else phone_color,
                alpha=0.3
            )

    # Axes
    ax.set_xscale('log')
    ax.set_xlabel('Frequency (Hz)', color='white')
    ax.set_ylabel('Sound level (dB)', color='white')
    ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=10))
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))

    # Center y-axis
    if center_y_axis:
        ax.set_ylim(-Y_AXIS_SCALE//2, Y_AXIS_SCALE//2)

    # Ticks
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Grid
    ax.grid(which='both', color='gray', linestyle='--', linewidth=0.7)

    # Legend
    ax.legend()

    plt.show()
