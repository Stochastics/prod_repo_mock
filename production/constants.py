"""
constants.py

This file contains global constants used throughout the data pipeline.
Use this to define values that are reused in multiple places and unlikely to change frequently,
such as column names, file paths, thresholds, feature lists, other values and other configuration parameters.

Keeping constants here improves maintainability and reduces hardcoding across the codebase.
"""

COUNTRY_NAME_MAP = {
    "usa": "United States",
    "us": "United States",
    "u.s.a.": "United States",
    "united states": "United States",
    "uk": "United Kingdom",
    "england": "United Kingdom"
}
