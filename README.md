# SmartClean

> An intelligent Python library for automated data cleaning with profiling, preprocessing, reporting, and CSV export.

**SmartClean** is a Python library designed to automate common data-cleaning tasks such as missing-value handling, duplicate removal, and outlier detection.

The library takes a Pandas DataFrame as input, processes it through a modular cleaning pipeline, generates before-and-after profiles, produces a cleaning report, and allows the cleaned dataset to be exported as a CSV file.

---

## Features

- Automated missing-value detection and handling
- Duplicate-row detection and removal
- Outlier detection using the IQR method
- Outlier capping
- Automatic data profiling
- Before and after cleaning profiles
- Detailed cleaning report
- Professional console cleaning summary
- Export cleaned dataset to CSV
- Configurable cleaning pipeline
- Modular and extensible architecture
- Simple and intuitive API
- Open-source and developer friendly

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yashtalati10/SmartClean.git
cd SmartClean
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Quick Start

The basic SmartClean workflow requires only a few lines of Python.

```python
import pandas as pd
from smartclean import Cleaner

# Load your dataset
df = pd.read_csv("your_file.csv")

# Initialize SmartClean
cleaner = Cleaner()

# Run the cleaning pipeline
result = cleaner.clean(df)

# Display the cleaning report
result.display_report()

# Access the cleaned dataset
print(result.cleaned_df.head())

# Save the cleaned dataset
result.save_csv("cleaned_data.csv")
```

---

# How SmartClean Works

SmartClean follows a modular automated cleaning pipeline.

```text
                     INPUT DATASET
                           │
                           ▼
                  Cleaner().clean(df)
                           │
                           ▼
                   CleaningPipeline
                           │
                           ▼
                  Before Profiling
                           │
                           ▼
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
       Missing Value   Duplicate      Outlier
         Handling      Removal       Detection
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                   After Profiling
                           │
                           ▼
                    Cleaning Report
                           │
                           ▼
                    CleaningResult
                    /      |       \
                   /       |        \
                  ▼        ▼         ▼
          cleaned_df  display_report()  save_csv()
```

---

# Built-in Functions and Their Roles

SmartClean provides a simple public API while internally using a modular cleaning pipeline.

## 1. `Cleaner()`

```python
cleaner = Cleaner()
```

### Purpose

Creates the main SmartClean cleaning object.

### What happens?

The `Cleaner` object stores the optional configuration and prepares the cleaning process.

---

## 2. `Cleaner.clean(df)`

```python
result = cleaner.clean(df)
```

This is the **main function that starts the cleaning process**.

Internally, it creates the `CleaningPipeline` and runs:

```python
pipeline = CleaningPipeline(data, config)
```

followed by:

```python
pipeline.run()
```

The pipeline performs the actual cleaning operations and returns:

```python
CleaningResult
```

### Internal Flow

```text
Cleaner.clean(df)
       │
       ▼
CleaningPipeline
       │
       ├── Before Profiling
       │
       ├── Missing Value Cleaning
       │
       ├── Duplicate Cleaning
       │
       ├── Outlier Cleaning
       │
       └── After Profiling
       │
       ▼
CleaningResult
```

---

# Cleaning Modules

## 3. Missing Value Cleaning

The missing-value module identifies missing values in the dataset and applies the configured strategy.

Supported strategies include:

- Mean imputation
- Median imputation
- Most frequent value imputation
- Dropping columns with excessive missing values

The cleaning report records:

```text
Missing Values Before
Missing Values Filled
Skipped Columns
Strategies Used
```

Example:

```text
[MISSING VALUE CLEANING]
  Missing Values Before : 177
  Missing Values Filled : 177
  Columns Skipped       : 0
  Status                : Completed
```

---

## 4. Duplicate Cleaning

The duplicate-cleaning module checks the dataset for duplicate rows.

It records:

```text
Duplicate Rows Found
Duplicate Rows Removed
```

Example:

```text
[DUPLICATE CLEANING]
  Duplicate Rows Found  : 12
  Duplicate Rows Removed: 12
  Status                : Completed
```

---

## 5. Outlier Cleaning

SmartClean uses the **Interquartile Range (IQR)** method for numerical outlier detection.

The calculation is:

```text
IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

Values outside these boundaries are considered potential outliers.

SmartClean supports:

- IQR-based outlier detection
- Outlier capping
- Outlier removal

The report records:

```text
Outlier Columns
Outliers Handled
Method
```

Example:

```text
[OUTLIER CLEANING]
  Outlier Columns       : 6
  Outlier Values Handled: 13,376
  Method                : IQR Capping
  Status                : Completed
```

---

# CleaningResult

After the cleaning pipeline finishes, SmartClean returns a `CleaningResult` object.

```python
result = cleaner.clean(df)
```

The object stores the main outputs of the cleaning process.

---

## 6. `result.cleaned_df`

```python
result.cleaned_df
```

Provides the final cleaned Pandas DataFrame.

Example:

```python
cleaned_data = result.cleaned_df

print(cleaned_data.head())
```

---

## 7. `result.before_profile`

```python
result.before_profile
```

Provides the dataset profile **before cleaning**.

It can be used to understand the original data quality.

---

## 8. `result.after_profile`

```python
result.after_profile
```

Provides the dataset profile **after cleaning**.

It can be compared with `before_profile` to evaluate the effect of the cleaning process.

---

## 9. `result.report`

```python
result.report
```

Provides the structured machine-readable cleaning report.

Example:

```python
{
    "missing": {
        "missing_values_before": 0,
        "missing_values_filled": 0,
        "skipped_columns": [],
        "strategies": {}
    },

    "duplicates": {
        "duplicates_found": 12,
        "duplicates_removed": 12
    },

    "outliers": {
        "outlier_columns": 6,
        "outliers_handled": 13376,
        "method": "cap"
    }
}
```

This format is useful when another Python program needs to process or analyze the cleaning results.

---

# Reporting Functions

## 10. `result.display_report()`

```python
result.display_report()
```

Displays the cleaning report in a human-readable format.

Instead of displaying a raw Python dictionary, SmartClean generates a structured summary:

```text
============================================================
                    SMARTCLEAN-AI
                  CLEANING REPORT
============================================================

[MISSING VALUE CLEANING]
  Missing Values Before : 0
  Missing Values Filled : 0
  Columns Skipped       : 0
  Status                : Completed

[DUPLICATE CLEANING]
  Duplicate Rows Found  : 12
  Duplicate Rows Removed: 12
  Status                : Completed

[OUTLIER CLEANING]
  Outlier Columns       : 6
  Outlier Values Handled: 13,376
  Method                : IQR Capping
  Status                : Completed

[FINAL DATASET]
  Rows                  : 41,176
  Columns               : 21

============================================================
          CLEANING PROCESS COMPLETED
============================================================
```

This function is useful for:

- Users
- Demonstrations
- Debugging
- Examiner verification

---

# CSV Export

## 11. `result.save_csv()`

SmartClean provides a built-in function to export the cleaned dataset.

### Default filename

```python
result.save_csv()
```

This creates:

```text
cleaned_data.csv
```

### Custom filename

```python
result.save_csv("my_cleaned_dataset.csv")
```

The function exports the cleaned DataFrame without writing the Pandas index as an additional column.

Internally:

```python
self.cleaned_df.to_csv(file_path, index=False)
```

Example output:

```text
[OK] Cleaned dataset saved successfully.
[OK] File    : cleaned_data.csv
[OK] Rows    : 41,176
[OK] Columns : 21
```

---

# Complete API Flow

The complete SmartClean workflow is:

```python
import pandas as pd
from smartclean import Cleaner

# 1. Load data
df = pd.read_csv("your_file.csv")

# 2. Initialize SmartClean
cleaner = Cleaner()

# 3. Run automated cleaning
result = cleaner.clean(df)

# 4. Display cleaning summary
result.display_report()

# 5. Access cleaned data
cleaned_df = result.cleaned_df

# 6. Access before/after profiles
before = result.before_profile
after = result.after_profile

# 7. Access structured report
report = result.report

# 8. Save cleaned dataset
result.save_csv("cleaned_data.csv")
```

---

# Function Summary

| Property / Function | Syntax | Purpose |
|---|---|---|
| `Cleaner()` | `cleaner = Cleaner()` | Creates and initializes the SmartClean cleaning object. |
| `Cleaner.clean()` | `result = cleaner.clean(df)` | Starts the complete automated cleaning pipeline. |
| `result.cleaned_df` | `result.cleaned_df` | Provides the final cleaned Pandas DataFrame. |
| `result.before_profile` | `result.before_profile` | Provides the dataset profile before cleaning. |
| `result.after_profile` | `result.after_profile` | Provides the dataset profile after cleaning. |
| `result.report` | `result.report` | Provides the structured machine-readable cleaning report. |
| `result.display_report()` | `result.display_report()` | Displays a formatted, human-readable cleaning summary. |
| `result.save_csv()` | `result.save_csv()` | Saves the cleaned dataset as `cleaned_data.csv`. |
| `result.save_csv(path)` | `result.save_csv("output.csv")` | Saves the cleaned dataset using a custom CSV filename or path. |

---

# Verification

The results produced by SmartClean can be independently cross-verified using standard Pandas operations.

## Check Missing Values

```python
print(df.isnull().sum())

print(
    "Total Null Values:",
    df.isnull().sum().sum()
)
```

## Check Duplicate Rows

```python
print(
    "Duplicate Rows:",
    df.duplicated().sum()
)
```

## Check Outliers Using IQR

```python
numeric_cols = df.select_dtypes(include="number").columns

total_outliers = 0

for col in numeric_cols:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = (
        (df[col] < lower_bound) |
        (df[col] > upper_bound)
    ).sum()

    print(f"{col}: {outliers} outliers")

    total_outliers += outliers

print("Total Outlier Values:", total_outliers)
```

> **Note:** Outlier verification should be performed on the original dataset before outlier cleaning if you want to compare the result with the number of outliers detected by SmartClean.

---

# Project Structure

```text
SmartClean/
│
├── smartclean/
│   ├── cleaning/
│   ├── config/
│   ├── core/
│   ├── handlers/
│   ├── utils/
│   ├── cleaner.py
│   ├── result.py
│   └── __init__.py
│
├── example/
│   └── demo.py
│
├── data/
│
├── reports/
│
├── README.md
├── requirements.txt
└── pyproject.toml
```

---

# Cleaning Pipeline

```text
                    Dataset
                       │
                       ▼
                Before Profiling
                       │
                       ▼
             Missing Value Handling
                       │
                       ▼
                Duplicate Removal
                       │
                       ▼
                Outlier Detection
                       │
                       ▼
                After Profiling
                       │
                       ▼
                Cleaning Report
                       │
                       ▼
                 CleaningResult
                       │
              ┌────────┴────────┐
              ▼                 ▼
       Display Report       CSV Export
              │                 │
              ▼                 ▼
       Human-readable      cleaned_data.csv
          summary
```

---

# Roadmap

## Version 1.0

- Data profiling
- Missing value handling
- Duplicate removal
- Outlier detection
- Cleaning reports

## Version 1.0.2

- Improved cleaning summary
- Human-readable reporting
- CSV export functionality
- Improved result handling
- Better user experience

## Future Versions

- Automatic data type detection
- Advanced categorical encoding
- Intelligent preprocessing recommendations
- Cleaning-result visualizations
- Image cleaning integration
- Machine-learning-assisted cleaning
- Web-based interface

---

# License

This project is open-source and intended for educational, research, and development purposes.