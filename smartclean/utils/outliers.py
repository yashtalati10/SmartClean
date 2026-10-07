import pandas as pd


def calculate_iqr_bounds(df, column):
    """
    Calculate IQR lower and upper bounds.
    """

    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)

    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    return lower_bound, upper_bound


def is_identifier(column_name):
    """
    Returns True if the column looks like an ID column.
    """

    column_name = column_name.lower()

    keywords = [
        "id",
        "_id",
        "patientid",
        "appointmentid",
        "employeeid",
        "customerid",
        "userid"
    ]

    return any(keyword in column_name for keyword in keywords)


def is_binary(series):
    """
    Returns True if the numeric column contains only
    two unique values.
    """

    unique_values = series.dropna().unique()

    return len(unique_values) <= 2


def is_low_cardinality(series, threshold=5):
    """
    Returns True if the numeric column has only a few
    unique values.
    """

    unique_count = series.dropna().nunique()

    return unique_count <= threshold


def is_continuous(series, threshold=10):
    """
    Returns True if the column has many unique values.
    """

    unique_count = series.dropna().nunique()

    return unique_count > threshold