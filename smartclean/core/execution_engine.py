from ..handlers.missing import MissingHandler
from ..handlers.duplicates import DuplicateHandler
from ..handlers.outliers import OutlierHandler


class ExecutionEngine:

    def __init__(self, dataframe, decisions):
        self.df = dataframe
        self.decisions = decisions

    def execute(self):
        handler=MissingHandler(self.df,self.decisions)
        self.df=handler.apply()
        handler=DuplicateHandler(self.df,self.decisions)
        self.df=handler.apply()
        handler=OutlierHandler(self.df,self.decisions)
        self.df=handler.apply()
        return self.df