class DecisionEngine:

    def __init__(self, profile, config):
        self.profile = profile
        self.config = config

    # ---------------------------------------------------
    # Missing Values
    # ---------------------------------------------------

    def generate_missing_decisions(self):

        total_rows = self.profile["shape"][0]

        decisions = {
            "missing": {}
        }

        for column, missing_count in self.profile["missing_values"].items():

            if missing_count == 0:
                continue

            missing_percentage = (missing_count / total_rows) * 100
            data_type = self.profile["data_types"][column]

            if missing_percentage <= self.config["missing"]["low_threshold"]:

                strategy = self.get_missing_strategy(
                    data_type=data_type,
                    numeric_level="low"
                )

            elif missing_percentage <= self.config["missing"]["high_threshold"]:

                strategy = self.get_missing_strategy(
                    data_type=data_type,
                    numeric_level="high"
                )

            else:

                strategy = self.config["missing"]["overflow"]

            decisions["missing"][column] = strategy

        return decisions

    def get_missing_strategy(self, data_type, numeric_level):

        if data_type in ["int64", "float64"]:
            return self.config["missing"]["numeric"][numeric_level]

        return self.config["missing"]["categorical"]

    # ---------------------------------------------------
    # Duplicates
    # ---------------------------------------------------

    def generate_duplicate_decisions(self):

        decisions = {}

        if self.profile["duplicates"] != 0:
            decisions["duplicates"] = self.config["duplicates"]["strategy"]

        return decisions

    # ---------------------------------------------------
    # Outliers
    # ---------------------------------------------------

    def generate_outlier_decisions(self):

        decisions = {
            "outliers": {}
        }

        for column, summary in self.profile["outlier_summary"].items():

            percentage = summary["percentage"]

            count = summary["count"]

            total_rows = self.profile["shape"][0]

            # -------------------------------------------------
            # Intelligent Automatic Policy
            # -------------------------------------------------

            # Very few outliers
            if percentage <= 5:

                strategy = "cap"

            # Moderate outliers
            elif percentage <= 20:

                strategy = "cap"

            # Large number of outliers
            else:

                # Only remove if almost every value is abnormal
                if count >= (0.80 * total_rows):
                    strategy = "remove"
                else:
                    strategy = "cap"

            decisions["outliers"][column] = strategy

        return decisions

    # ---------------------------------------------------
    # Generate All Decisions
    # ---------------------------------------------------

    def generate_decisions(self):

        decisions = {}

        decisions.update(self.generate_missing_decisions())

        decisions.update(self.generate_duplicate_decisions())

        decisions.update(self.generate_outlier_decisions())

        return decisions