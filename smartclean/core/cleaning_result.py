class CleaningResult:
    """
    Stores the final cleaned dataset and the generated
    SmartClean report.
    """

    def __init__(self, cleaned_df, report):
        self.cleaned_df = cleaned_df
        self.report = report

    def __repr__(self):
        return (
            f"CleaningResult("
            f"rows={self.cleaned_df.shape[0]}, "
            f"columns={self.cleaned_df.shape[1]})"
        )