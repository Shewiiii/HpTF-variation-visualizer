import numpy as np
from scipy.interpolate import interp1d
from typing import Tuple, Union
import pandas as pd
from pathlib import Path


from app.read_fr import read_frequency_response_file
from app.config import NUM_VALUES


def interpolate(
    df: pd.DataFrame,
    num_values: int = NUM_VALUES
) -> Tuple[np.ndarray, np.ndarray]:
    """Interpolates frequency-dB pairs from a DataFrame."""
    # Extract the values
    frequencies = df['frequency'].values
    dbs = df['dB'].values

    # Sort the frequencies
    sorted_i = np.argsort(frequencies)
    frequencies_sorted = frequencies[sorted_i]
    dbs_sorted = dbs[sorted_i]

    # Create the interpolating function
    interpolation_function = interp1d(
        frequencies_sorted,
        dbs_sorted,
        kind='linear',
        fill_value="extrapolate"
    )

    # Create a list of homogeneously separated frequency values
    interpolated_frequencies = np.linspace(
        frequencies_sorted.min(),
        frequencies_sorted.max(),
        num_values
    )

    # Calculate interpolated dB values
    interpolated_dbs = interpolation_function(interpolated_frequencies)

    return interpolated_frequencies, interpolated_dbs


def interpolate_from_file(
    path: Union[Path, str],
    num_values: int = NUM_VALUES
) -> Tuple[np.ndarray, np.ndarray]:
    return interpolate(
        read_frequency_response_file(path),
        num_values
    )
