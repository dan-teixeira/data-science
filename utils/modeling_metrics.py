"""
    Functions to evaluate model performance
"""

import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.api import add_constant



def vif_tolerance(df: pd.DataFrame, endog: str, drop_columns: list = []):

    df = add_constant(df.drop(drop_columns + [endog], axis=1))

    df_metrics = pd.DataFrame(
        zip(
            df.columns[1:],
            [
                variance_inflation_factor(exog=df.values, exog_idx=idx)
                for idx in range(1, df.shape[1])
            ],
        ),
        columns=["variables", "vif"],
    )

    df_metrics["tolerance"] = df_metrics["vif"] ** (-1)

    return df_metrics.sort_values("vif", ascending=False).reset_index(drop=True)