import matplotlib.pyplot as plt
import numpy as np
from random import randint, uniform, random
import colorsys
from typing import Tuple


def generate_color() -> Tuple[float, float, float]:
    h = random()
    s = uniform(0.7, 1.0)
    v = uniform(0.7, 1.0)
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return (r, g, b)


def plot_frequency_response(
        freq_db_list: list[Tuple[np.ndarray, np.ndarray]]
) -> None:
    """Plots a frequency-response curve."""
    # Plot
    fig, ax = plt.subplots(figsize=(16, 9))

    # Background color
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')

    # Data
    for idx, (frequencies, dbs) in enumerate(freq_db_list):
        ax.plot(
            frequencies,
            dbs,
            color=generate_color(),
            linewidth=2,
            label=f'Phone {idx+1}'
        )

    # Axes
    ax.set_xscale('log')
    ax.set_xlabel('Frequency (Hz)', color='white')
    ax.set_ylabel('Sound level (dB)', color='white')

    # Ticks
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Grid
    ax.grid(which='both', color='gray', linestyle='--', linewidth=0.7)

    plt.show()
