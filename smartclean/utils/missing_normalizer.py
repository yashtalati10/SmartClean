import numpy as np
import pandas as pd


class MissingValueNormalizer:
    """
    Converts common missing value placeholders
    into actual NaN values before profiling.
    """

    @staticmethod
    def normalize(df: pd.DataFrame, placeholders: list) -> pd.DataFrame:
        """
        Replace configured placeholder values with NaN.

        Parameters
        ----------
        df : pandas.DataFrame
            Input dataframe.

        placeholders : list
            List of placeholder values to replace.

        Returns
        -------
        pandas.DataFrame
            Normalized dataframe.
        """

        normalized_df = df.copy()

        # Replace configured placeholder values
        normalized_df.replace(placeholders, np.nan, inplace=True)

        # Replace whitespace-only strings with NaN
        normalized_df.replace(
            r"^\s*$",
            np.nan,
            regex=True,
            inplace=True
        )

        return normalized_df