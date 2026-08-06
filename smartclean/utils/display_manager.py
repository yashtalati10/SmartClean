class DisplayManager:

    @staticmethod
    def show_banner():
        print("=" * 60)
        print("                    SMARTCLEAN AI")
        print("         Intelligent Data Cleaning Pipeline")
        print("=" * 60)

    @staticmethod
    def show_profile(profile):

        print("\n" + "=" * 60)
        print("DATASET PROFILE")
        print("=" * 60)

        print(f"Rows            : {profile['shape'][0]}")
        print(f"Columns         : {profile['shape'][1]}")
        print(f"Duplicate Rows  : {profile['duplicates']}")
        print(f"Memory Usage    : {profile['memory_usage']} Bytes")

        print("\nColumn Data Types")
        print("-" * 60)

        for column, dtype in profile["data_types"].items():
            print(f"{column:<20} {dtype}")

        print("\nMissing Values")
        print("-" * 60)

        total_missing = 0

        for column, count in profile["missing_values"].items():
            if count > 0:
                print(f"{column:<20} {count}")
                total_missing += count

        if total_missing == 0:
            print("No Missing Values Found.")

    @staticmethod
    def show_summary(old_profile, new_profile):

        print("\n" + "=" * 60)
        print("CLEANING SUMMARY")
        print("=" * 60)

        total_before = 0
        total_after = 0

        for column in old_profile["missing_values"]:

            before = old_profile["missing_values"][column]
            after = new_profile["missing_values"][column]

            if before > 0 or after > 0:
                print(f"{column:<20} {before} -> {after} ✓")

            total_before += before
            total_after += after

        print("-" * 60)
        print(f"Total Missing Before : {total_before}")
        print(f"Total Missing After  : {total_after}")

    @staticmethod
    def show_cleaning_report(
        missing_report,
        duplicate_report,
        outlier_report
    ):

        print("\n" + "=" * 60)
        print("CLEANING REPORT")
        print("=" * 60)

        print("\nMissing Value Cleaning")
        print("-" * 60)
        print(
            f"Missing Values Filled : {missing_report['missing_values_filled']}"
        )

        if missing_report["skipped_columns"]:
            print(
                f"Skipped Columns       : {', '.join(missing_report['skipped_columns'])}"
            )

        print("\nDuplicate Cleaning")
        print("-" * 60)
        print(
            f"Duplicates Found      : {duplicate_report['duplicates_found']}"
        )
        print(
            f"Duplicates Removed    : {duplicate_report['duplicates_removed']}"
        )

        print("\nOutlier Cleaning")
        print("-" * 60)
        print(
            f"Outlier Columns       : {outlier_report['outlier_columns']}"
        )
        print(
            f"Method Used           : {outlier_report['method']}"
        )
        print(
            f"Outliers Handled      : {outlier_report['outliers_handled']}"
        )

        print("\n" + "=" * 60)
        print("Cleaning Pipeline Completed Successfully. ✅")
        print("=" * 60)