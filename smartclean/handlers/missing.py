class MissingHandler:
    def __init__(self,df,decisions):
        self.df=df.copy()
        self.decisions=decisions
    def apply(self):
        for column,strategy in self.decisions["missing"].items():
            if strategy=="drop":
                self.df=self.df.drop(columns=[column])
            elif strategy=="mean":
                self.df[column]=self.df[column].fillna(
                    self.df[column].mean()
                )
            elif strategy=="median":
                self.df[column]=self.df[column].fillna(
                    self.df[column].median()
                )
            elif strategy=="most_frequent":
                self.df[column]=self.df[column].fillna(
                    self.df[column].mode()[0]
                )
        return self.df