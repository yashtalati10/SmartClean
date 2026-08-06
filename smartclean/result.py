class CleaningResult:
    """
    Stores the cleaned dataset and SmartClean reports.
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

    def __repr__(self):
        return (
            f"CleaningResult("
            f"rows={self.cleaned_df.shape[0]}, "
            f"columns={self.cleaned_df.shape[1]})"
        )