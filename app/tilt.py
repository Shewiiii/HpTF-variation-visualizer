from typing import Tuple
import numpy as np


def tilt_phone(
    phone: Tuple[np.ndarray, np.ndarray],
    tilt: float = -1.,
    freq=20.
) -> Tuple[np.ndarray, np.ndarray]:
    """
    The “tilt” is computed as:
        tilt_adjustment(f) = tilt_db_per_octave * log2(f / f_ref).
    """
    frequencies = np.asarray(phone[0], dtype=float)
    dbs = np.asarray(phone[1], dtype=float)
    octaves = np.log2(frequencies / freq)
    tilt_adjustment = tilt * octaves
    tilted_phone = (frequencies, dbs + tilt_adjustment)
    return tilted_phone
