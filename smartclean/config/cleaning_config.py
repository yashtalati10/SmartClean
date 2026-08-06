DEFAULT_CONFIG = {

    "missing_normalization": {
        "enabled": True,

        "placeholders": [
            "?",
            "NA",
            "N/A",
            "null",
            "None",
            ""
        ]
    },

    "missing": {
        "enabled": True,

        "low_threshold": 10,
        "high_threshold": 50,

        "numeric": {
            "low": "mean",
            "high": "median"
        },

        "categorical": "most_frequent",

        "overflow": "drop"
    },

    "duplicates": {
        "enabled": True,
        "strategy": "drop"
    },

    "outliers": {
        "enabled": True,

        "method": "cap",

        "low_threshold": 5,
        "high_threshold": 20,

        "low": "cap",
        "high": "remove",

        "overflow": "remove"
    }
}