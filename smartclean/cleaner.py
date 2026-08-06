from .core.pipeline import CleaningPipeline
from .result import CleaningResult


class Cleaner:

    def __init__(self, config=None):
        self.config = config

    def clean(self, data):

        pipeline = CleaningPipeline(data, self.config)

        cleaned_df, before_profile, after_profile, report = pipeline.run()

        return CleaningResult(
            cleaned_df=cleaned_df,
            before_profile=before_profile,
            after_profile=after_profile,
            report=report
        )