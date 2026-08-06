import pandas as pd
from sklearn.impute import SimpleImputer


class MissingValueHandler:

    def __init__(self, dataframe, profile):
        self.df = dataframe.copy()
        self.profile = profile

    def handle_missing_values(self):

        print("\n========== Missing Value Cleaning ==========\n")

        total_rows = len(self.df)

        report = {
            "missing_values_before": sum(self.profile["missing_values"].values()),
            "missing_values_filled": 0,
            "skipped_columns": [],
            "strategies": {}
        }

        for column, missing_count in self.profile["missing_values"].items():

            if missing_count == 0:
                continue

            if missing_count == total_rows:
                print(
                    f"⚠ Column: {column:<16} | Missing: {missing_count:<4} | Skipped (100% Missing)"
                )
                report["skipped_columns"].append(column)
                continue

            data_type = self.profile["data_types"][column]

            if data_type in ["int64", "float64"]:
                strategy = "mean"
            else:
                strategy = "most_frequent"

            imputer = SimpleImputer(strategy=strategy)

            self.df[[column]] = imputer.fit_transform(self.df[[column]])

            report["missing_values_filled"] += missing_count
            report["strategies"][column] = strategy

            print(
                f"✓ Column: {column:<16} | Missing: {missing_count:<4} | Strategy: {strategy}"
            )

        print("\n✅ Missing value cleaning completed.\n")

        return self.df, report