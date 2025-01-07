from typing import Tuple
import numpy as np


def compensate_hrtf(
    dfhrtf_baseline: Tuple[np.ndarray, np.ndarray],
    frequency_response: Tuple[np.ndarray, np.ndarray]
) -> Tuple[np.ndarray, np.ndarray]:
    """Compensates a frequency response from a dfhrtf baseline to filter HRTF features from it.
    Useful to compare HpTF variation between gears."""
