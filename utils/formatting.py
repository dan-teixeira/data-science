"""
    Utility functions to simplify DataFrame handling and modeling.
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


@vector
def pascal_to_snake(string: str) -> str:

    return (
        string[0]
        + "".join([f"_{s}" if s.isupper() else s for s in string[1:].replace("_", "")])
    ).lower()


def get_formula(df: pd.DataFrame, endog: str, drop_columns: list = []) -> str:

    return (
        endog
        + " ~ "
        + " + ".join([col for col in df.drop(drop_columns).columns if col != endog])
    )
