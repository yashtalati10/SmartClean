from ..utils.outliers import calculate_iqr_bounds


class OutlierHandler:

    def __init__(self, df, decisions):
        self.df = df.copy()
        self.decisions = decisions

    def apply(self):

        outlier_decisions = self.decisions.get("outliers", {})

        for column, strategy in outlier_decisions.items():

            # Skip if column disappeared during previous cleaning
            if column not in self.df.columns:
                continue

            lower_bound, upper_bound = calculate_iqr_bounds(
                self.df,
                column
            )

            # --------------------------------------------
            # Remove extreme outlier rows
            # --------------------------------------------
            if strategy == "remove":

                self.df = self.df[
                    (self.df[column] >= lower_bound)
                    &
                    (self.df[column] <= upper_bound)
                ]

            # --------------------------------------------
            # Cap values (preferred strategy)
            # --------------------------------------------
            elif strategy == "cap":

                self.df[column] = self.df[column].clip(
                    lower=lower_bound,
                    upper=upper_bound
                )

            # --------------------------------------------
            # Ignore
            # --------------------------------------------
            elif strategy == "ignore":
                continue

            # --------------------------------------------
            # Unknown strategy
            # --------------------------------------------
            else:
                continue

        return self.df