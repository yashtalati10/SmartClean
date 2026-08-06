from ..utils.profiling_utils import generate_profile
from ..cleaning.missing_handler import MissingValueHandler
from ..cleaning.duplicate_handler import DuplicateHandler
from ..cleaning.outlier_handler import OutlierHandler
from ..config.cleaning_config import DEFAULT_CONFIG

class CleaningPipeline:
    def __init__(self,df,config=None):
        self.config=config or DEFAULT_CONFIG
        self.df=df.copy()
        self.old_profile=generate_profile(self.df)
        self.profile=self.old_profile
        self.reports={}
    def refresh_profile(self):
        self.profile=generate_profile(self.df)
    def run_missing(self):
        missing_handler = MissingValueHandler(self.df, self.profile)
        self.df, self.reports['missing'] = missing_handler.handle_missing_values()
        self.refresh_profile()
    def run_duplicates(self):
        duplicate_handler = DuplicateHandler(self.df, self.profile)
        self.df, self.reports['duplicates'] = duplicate_handler.handle_duplicates()
        self.refresh_profile()
    def run_outliers(self):
        outlier_handler = OutlierHandler(self.df, self.profile)
        # self.df, self.reports['outliers'] = outlier_handler.handle_outliers(method=self.config['outliers']['method'])
        # self.df, self.reports["outliers"] = outlier_handler.handle_outliers()
        # self.df, self.reports["outliers"] = outlier_handler.handle_outliers(
        #     method="cap"
        # )
        method = self.config["outliers"].get("method", "cap")
        self.df, self.reports["outliers"] = outlier_handler.handle_outliers(
            method=method
        )
        self.refresh_profile()

    def run(self):
        if self.config['missing']['enabled']:
            self.run_missing()
        if self.config['duplicates']['enabled']:
            self.run_duplicates()
        if self.config['outliers']['enabled']:
            self.run_outliers()
        return(
            self.df,
            self.old_profile,
            self.profile,
            self.reports
        )