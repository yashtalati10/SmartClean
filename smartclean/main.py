from .core.loader import DataLoader

from .core.pipeline import CleaningPipeline

from .utils.display_manager import DisplayManager
from .utils.profiling_utils import generate_profile


def main():

    DisplayManager.show_banner()

    loader = DataLoader("data/raw/employee_master_dataset.csv")
    df = loader.load_data()

    print("✅ File Loaded Successfully.\n")

    pipeline=CleaningPipeline(df)
    cleaned_df,old_profile,profile,reports=pipeline.run()
    DisplayManager.show_profile(old_profile)
    DisplayManager.show_summary(old_profile, profile)
    DisplayManager.show_cleaning_report(
        reports['missing'],
        reports['duplicates'],
        reports['outliers']
    )

if __name__ == "__main__":
    cleaned_df = main()