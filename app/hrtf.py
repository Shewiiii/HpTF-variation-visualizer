from typing import Tuple
import numpy as np


def compensate(
    dfhrtf_baseline: Tuple[np.ndarray, np.ndarray],
    phone: Tuple[np.ndarray, np.ndarray]
) -> Tuple[np.ndarray, np.ndarray]:
    """Compensates a frequency response from a dfhrtf baseline to filter HRTF features from it.
    Useful to compare HpTF variation between gears."""
    baseline_freq = dfhrtf_baseline[0]
    baseline_db = dfhrtf_baseline[1]
    phone_db = phone[1]
    return (
        baseline_freq,
        phone_db-baseline_db
    )
