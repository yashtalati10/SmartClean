class CleaningResult:
    """
    Stores the cleaned dataset and SmartClean reports.

    Provides:
    - Access to the cleaned DataFrame
    - Before/after dataset profiles
    - Cleaning report
    - Formatted cleaning summary
    - CSV export functionality
    """

    def __init__(
        self,
        cleaned_df,
        before_profile,
        after_profile,
        report
    ):
        self.cleaned_df = cleaned_df
        self.before_profile = before_profile
        self.after_profile = after_profile
        self.report = report

    def display_report(self):
        """
        Display a professional, human-readable cleaning report.
        """

        print("\n" + "=" * 60)
        print("                    SMARTCLEAN-AI")
        print("                  CLEANING REPORT")
        print("=" * 60)

        # -------------------------
        # Missing Value Cleaning
        # -------------------------
        missing = self.report.get("missing", {})

        missing_before = missing.get("missing_values_before", 0)
        missing_filled = missing.get("missing_values_filled", 0)
        skipped_columns = missing.get("skipped_columns", [])

        print("\n[MISSING VALUE CLEANING]")
        print(f"  Missing Values Before : {missing_before:,}")
        print(f"  Missing Values Filled : {missing_filled:,}")
        print(f"  Columns Skipped       : {len(skipped_columns):,}")
        print("  Status                : Completed")

        # -------------------------
        # Duplicate Cleaning
        # -------------------------
        duplicates = self.report.get("duplicates", {})

        duplicates_found = duplicates.get("duplicates_found", 0)
        duplicates_removed = duplicates.get("duplicates_removed", 0)

        print("\n[DUPLICATE CLEANING]")
        print(f"  Duplicate Rows Found  : {duplicates_found:,}")
        print(f"  Duplicate Rows Removed: {duplicates_removed:,}")
        print("  Status                : Completed")

        # -------------------------
        # Outlier Cleaning
        # -------------------------
        outliers = self.report.get("outliers", {})

        outlier_columns = outliers.get("outlier_columns", 0)
        outliers_handled = outliers.get("outliers_handled", 0)
        method = outliers.get("method", "N/A")

        method_display = {
            "cap": "IQR Capping",
            "remove": "IQR Removal"
        }.get(str(method).lower(), str(method).upper())

        print("\n[OUTLIER CLEANING]")
        print(f"  Outlier Columns       : {outlier_columns:,}")
        print(f"  Outlier Values Handled: {outliers_handled:,}")
        print(f"  Method                : {method_display}")
        print("  Status                : Completed")

        # -------------------------
        # Final Dataset
        # -------------------------
        rows = self.cleaned_df.shape[0]
        columns = self.cleaned_df.shape[1]

        print("\n[FINAL DATASET]")
        print(f"  Rows                  : {rows:,}")
        print(f"  Columns               : {columns:,}")

        print("\n" + "=" * 60)
        print("          CLEANING PROCESS COMPLETED")
        print("=" * 60)

    def save_csv(self, file_path="cleaned_data.csv"):
        """
        Save the cleaned dataset as a CSV file.

        Parameters
        ----------
        file_path : str, optional
            Output path/name of the CSV file.
            Default is 'cleaned_data.csv'.

        Returns
        -------
        str
            The path of the saved CSV file.
        """

        try:
            self.cleaned_df.to_csv(file_path, index=False)

            print("\n[OK] Cleaned dataset saved successfully.")
            print(f"[OK] File    : {file_path}")
            print(f"[OK] Rows    : {self.cleaned_df.shape[0]:,}")
            print(f"[OK] Columns : {self.cleaned_df.shape[1]:,}")

            return file_path

        except Exception as e:
            raise RuntimeError(
                f"Failed to save cleaned dataset: {e}"
            ) from e

    def __repr__(self):
        return (
            f"CleaningResult("
            f"rows={self.cleaned_df.shape[0]}, "
            f"columns={self.cleaned_df.shape[1]})"
        )