# SmartClean

> An intelligent Python library for automated data cleaning with profiling, preprocessing, and detailed reporting.

SmartClean simplifies the data cleaning process by automatically identifying and handling common data quality issues such as missing values, duplicate records, and outliers. It generates comprehensive profiling reports before and after cleaning, making datasets ready for analysis and machine learning.

---

## Features

- Automated missing value detection and handling
- Duplicate row detection and removal
- Outlier detection using the IQR method
- Automatic data profiling
- Before and after cleaning reports
- Configurable cleaning pipeline
- Modular and extensible architecture
- Simple and intuitive API
- Open-source and developer friendly

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/SmartClean.git

cd SmartClean
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Quick Start

```python
import pandas as pd
from smartclean import Cleaner

# Load dataset
df = pd.read_csv("data/raw/Kaggle/1.csv")

# Initialize SmartClean
cleaner = Cleaner()

# Clean dataset
result = cleaner.clean(df)

print(result.cleaned_df.head())
print(result.report)
```

---

## Example Output

```
========== Missing Value Cleaning ==========

✓ Column: Age              | Missing: 177 | Strategy: mean
✓ Column: Cabin            | Missing: 687 | Strategy: most_frequent
✓ Column: Embarked         | Missing: 2   | Strategy: most_frequent

========== Duplicate Cleaning ==========

✓ No duplicate rows found.

========== Outlier Cleaning ==========

✓ Outlier Values Capped : 441

CleaningResult(rows=891, columns=12)
```

---

## Project Structure

```
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
└── requirements.txt
```

---

## Cleaning Pipeline

```
Dataset
    │
    ▼
Data Profiling
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
Updated Profiling
    │
    ▼
Cleaning Report
    │
    ▼
Clean Dataset
```

---

## Current Cleaning Capabilities

### Missing Values

- Mean imputation
- Median imputation
- Most frequent value imputation
- Drop columns with excessive missing values

### Duplicates

- Detect duplicate rows
- Remove duplicate records

### Outliers

- IQR-based outlier detection
- Outlier capping
- Outlier removal

---

## Output

SmartClean returns a `CleaningResult` object.

```python
result = Cleaner().clean(df)

result.cleaned_df
result.before_profile
result.after_profile
result.report
```

---

## Roadmap

### Version 1.0

- Data profiling
- Missing value handling
- Duplicate removal
- Outlier detection
- Cleaning reports