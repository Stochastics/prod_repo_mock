
import re
import pandas as pd

def clean_country(country, name_map):
    if pd.isna(country):
        return "Unknown"
    country = country.strip().lower()
    return name_map.get(country, country.title())

def clean_text(text):
    if pd.isna(text):
        return ""
    text = re.sub(r"[^a-zA-Z0-9 ]", "", str(text))
    return text.strip().lower()

def clean_text_extra(text):
    return re.sub(r"\s{2,}", " ", text)
