"""
    Utility functions to simplify and enhance interactions with DataFrames.
"""

import unicodedata
import pandas as pd
from numpy import vectorize


def vector(f):
    def wrapper(*arg, **kwargs):
        return vectorize(f)(*arg, **kwargs)
    return wrapper

@vector
def normalize_string(string: str) -> str:
    return (
        "".join(
            [
                s
                for s in unicodedata.normalize("NFD", string)
                if unicodedata.category(s) != "Mn"
            ]
        )
        .lower()
        .strip()
        .replace(" ", "_")
    )


def get_formula(df: pd.DataFrame, endog: str) -> str:

    exog = " + ".join([col for col in df.columns if col != endog])

    return (endog + " ~ " + exog)