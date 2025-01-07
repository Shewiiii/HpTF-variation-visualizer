import pandas as pd
from pandas.core.frame import DataFrame
from pathlib import Path
from typing import Union

from app.config import SEPARATOR


def read_frequency_response_file(path: Union[Path, str]) -> DataFrame:
    return pd.read_csv(
        path,
        sep=SEPARATOR,
        header=None,
        names=['frequency', 'dB'],
    )
