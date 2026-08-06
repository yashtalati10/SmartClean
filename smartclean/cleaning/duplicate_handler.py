class DuplicateHandler:
    def __init__(self, df, profile):
        self.df = df.copy()
        self.profile = profile

    def has_duplicates(self):
        return self.profile["duplicates"] > 0

    def find_duplicates(self):
        return self.df[self.df.duplicated()]

    def remove_duplicates(self):
        self.df = self.df.drop_duplicates()
        return self.df

    def handle_duplicates(self):

        print("\n========== Duplicate Cleaning ==========\n")

        report = {
            "duplicates_found": self.profile["duplicates"],
            "duplicates_removed": 0
        }

        if not self.has_duplicates():
            print("✓ No duplicate rows found.\n")
            return self.df, report

        report["duplicates_removed"] = self.profile["duplicates"]

        print(
            f"✓ Duplicate Rows Found   : {report['duplicates_found']}"
        )
        print(
            f"✓ Duplicate Rows Removed : {report['duplicates_removed']}"
        )

        self.remove_duplicates()

        print("\n✅ Duplicate cleaning completed.\n")

        return self.df, report