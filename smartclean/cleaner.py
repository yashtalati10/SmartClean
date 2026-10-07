from .core.pipeline import CleaningPipeline
from .result import CleaningResult


class Cleaner:
    """
    Main interface for SmartClean-AI data cleaning.

    The Cleaner creates and runs the cleaning pipeline and
    returns a CleaningResult containing the cleaned dataset,
    profiles, and cleaning report.
    """

    def __init__(self, config=None):
        """
        Initialize the SmartClean-AI cleaner.

        Parameters
        ----------
        config : dict, optional
            Configuration options for the cleaning pipeline.
        """
        self.config = config

    def clean(self, data):
        """
        Clean the input dataset.

        Parameters
        ----------
        data : pandas.DataFrame
            Input dataset to be cleaned.

        Returns
        -------
        CleaningResult
            Contains the cleaned DataFrame, before/after profiles,
            and cleaning report.
        """

        pipeline = CleaningPipeline(data, self.config)

        cleaned_df, before_profile, after_profile, report = pipeline.run()

        return CleaningResult(
            cleaned_df=cleaned_df,
            before_profile=before_profile,
            after_profile=after_profile,
            report=report
        )