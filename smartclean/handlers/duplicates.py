class DuplicateHandler:

    def __init__(self, df, decisions):
        self.df = df.copy()
        self.decisions = decisions

    def apply(self):

        strategy = self.decisions.get("duplicates")

        if strategy == "drop":
            self.df = self.df.drop_duplicates()

        return self.df