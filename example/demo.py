import pandas as pd
from smartclean import Cleaner

df = pd.read_csv("data/raw/Kaggle/1.csv")

result = Cleaner().clean(df)

print(result)

print("\n===== Cleaned Data =====")
print(result.cleaned_df.head())

print("\n===== Cleaning Report =====")
print(result.report)