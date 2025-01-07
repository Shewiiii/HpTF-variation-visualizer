import numpy as np
from scipy.interpolate import interp1d
from typing import Tuple

from app.config import NORMALIZATION_FREQUENCY


def normalize(
    freq_db: Tuple[np.ndarray, np.ndarray],
    reference_freq: int = NORMALIZATION_FREQUENCY
) -> Tuple[np.ndarray, np.ndarray]:
    frequencies, dbs = freq_db

    # Create an interpolation function to find the dB at the reference frequency
    # fill_value="extrapolate" allows interpolation even if reference_freq is
    # outside the min-max range of 'frequencies'
    interpolation_function = interp1d(
        frequencies,
        dbs,
        kind='linear',
        bounds_error=False,
        fill_value="extrapolate"
    )

    # Get the dB at the reference frequency
    ref_db = interpolation_function(reference_freq)

    # Subtract this reference dB from the entire dB array
    normalized_dbs = dbs - ref_db

    return frequencies, normalized_dbs
