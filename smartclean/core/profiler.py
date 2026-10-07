from ..utils.outliers import (
    calculate_iqr_bounds,
    is_identifier,
    is_binary,
    is_low_cardinality
)


class DataProfiler:
    """
    Generates a profile containing useful information
    about the dataset.
    """

    def __init__(self, dataframe):
        self.df = dataframe

    def profile(self):
        """
        Returns a complete dataset profile.
        """

        # Handle completely empty DataFrame
        if self.df.empty and self.df.shape[1] == 0:
            return {
                "shape": self.df.shape,
                "columns": [],
                "data_types": {},
                "missing_values": {},
                "duplicates": 0,
                "memory_usage": 0,
                "statistics": {},
                "outlier_summary": {}
            }

        return {
            "shape": self.get_shape(),
            "columns": self.get_columns(),
            "data_types": self.get_data_types(),
            "missing_values": self.get_missing_values(),
            "duplicates": self.get_duplicates(),
            "memory_usage": self.get_memory_usage(),
            "statistics": self.get_statistics(),
            "outlier_summary": self.get_outlier_summary()
        }

    def get_shape(self):
        return self.df.shape

    def get_columns(self):
        return list(self.df.columns)

    def get_data_types(self):
        return self.df.dtypes.astype(str).to_dict()

    def get_missing_values(self):
        return self.df.isnull().sum().to_dict()

    def get_duplicates(self):
        return int(self.df.duplicated().sum())

    def get_memory_usage(self):
        return int(self.df.memory_usage(deep=True).sum())

    def get_statistics(self):

        if self.df.empty or self.df.shape[1] == 0:
            return {}

        return (
            self.df
            .describe(include="all")
            .fillna("")
            .to_dict()
        )

    def get_outlier_summary(self):

        numeric_df = self.df.select_dtypes(include=["number"])

        outlier_summary = {}

        total_rows = self.df.shape[0]

        if total_rows == 0:
            return {}

        for column in numeric_df.columns:

            # Ignore ID columns
            if is_identifier(column):
                continue

            # Ignore binary numeric columns
            if is_binary(self.df[column]):
                continue

            # Ignore low-cardinality numeric columns
            if is_low_cardinality(self.df[column]):
                continue

            outlier_df = self.find_outliers(column)

            count = len(outlier_df)

            if count == 0:
                continue

            percentage = (count / total_rows) * 100

            outlier_summary[column] = {
                "count": count,
                "percentage": percentage,
            }

        return outlier_summary

    def find_outliers(self, column):

        lower_bound, upper_bound = calculate_iqr_bounds(
            self.df,
            column
        )

        outlier_df = self.df[
            (self.df[column] < lower_bound)
            | (self.df[column] > upper_bound)
        ]

        return outlier_df