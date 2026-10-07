from ..utils.outliers import calculate_iqr_bounds


class OutlierHandler:

    def __init__(self, df, profile):
        self.df = df.copy()
        self.profile = profile

    def has_outliers(self):
        return len(self.find_outliers()) > 0

    def find_outliers(self):
        outliers = {}

        for column, data_type in self.profile["data_types"].items():

            if data_type in ["int64", "float64"]:

                # lower_bound, upper_bound = calculate_iqr_bounds(column)
                lower_bound, upper_bound = calculate_iqr_bounds(
                    self.df,
                    column
                )

                outlier_df = self.df[
                    (self.df[column] < lower_bound)
                    | (self.df[column] > upper_bound)
                ]

                if not outlier_df.empty:
                    outliers[column] = outlier_df

        return outliers

    def remove_outliers(self):

        outliers = self.find_outliers()
        outlier_indices = set()

        for outlier_df in outliers.values():
            outlier_indices.update(outlier_df.index)

        self.df = self.df.drop(
            index=list(outlier_indices)
        )

        return self.df, len(outlier_indices)

    def cap_outliers(self):

        capped_count = 0

        for column, data_type in self.profile["data_types"].items():

            if data_type in ["int64", "float64"]:

                # lower_bound, upper_bound = calculate_iqr_bounds(column)
                lower_bound, upper_bound = calculate_iqr_bounds(
                    self.df,
                    column
                )

                # Fix for integer columns
                if data_type == "int64":
                    lower_bound = round(lower_bound)
                    upper_bound = round(upper_bound)

                lower_mask = self.df[column] < lower_bound
                upper_mask = self.df[column] > upper_bound

                capped_count += lower_mask.sum()
                capped_count += upper_mask.sum()

                self.df.loc[
                    lower_mask,
                    column
                ] = lower_bound

                self.df.loc[
                    upper_mask,
                    column
                ] = upper_bound

        return self.df, capped_count

    def handle_outliers(self, method):

        print("\n========== Outlier Cleaning ==========\n")

        outliers = self.find_outliers()

        report = {
            "outlier_columns": len(outliers),
            "outliers_handled": 0,
            "method": method
        }

        if not self.has_outliers():
            print("[OK] No outliers found.\n")
            return self.df, report

        if method == "remove":

            self.df, removed_count = self.remove_outliers()

            report["outliers_handled"] = int(removed_count)

            print(
                f"[OK] Outlier Rows Removed : {removed_count}"
            )

        elif method == "cap":

            self.df, capped_count = self.cap_outliers()

            report["outliers_handled"] = int(capped_count)

            print(
                f"[OK] Outlier Values Capped : {capped_count}"
            )

        else:
            raise ValueError(
                "Invalid method for handling outliers."
            )

        print("\n[OK] Outlier cleaning completed.\n")

        return self.df, report