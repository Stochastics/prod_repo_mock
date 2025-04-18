"""
main.py

This script is the entry point for the data pipeline. It loads raw data, applies cleaning functions,
and performs basic analysis. Configurable parameters such as input file paths, country name mappings,
and other settings are defined in the config.yaml file for easy maintenance and modification.

Ensure that the `config.yaml` file is properly configured before running this pipeline.
"""

import pandas as pd
import yaml
from constants import COUNTRY_NAME_MAP
from utils.cleaning import clean_country, clean_text, clean_text_extra

# Load the config.yaml file
def load_config():
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config

# Load data based on the path provided in config
def load_data(path):
    return pd.read_csv(path)

# Clean the data with various cleaning functions
def clean_data(df):
    df['country_cleaned'] = df['country'].apply(lambda x: clean_country(x, COUNTRY_NAME_MAP))
    df['comments_cleaned'] = df['comments'].apply(clean_text)
    df['comments_cleaned'] = df['comments_cleaned'].apply(clean_text_extra)
    df['comment_length'] = df['comments_cleaned'].apply(lambda x: len(x.split(" ")))
    return df

# Perform analysis on the cleaned data (average rating by country)
def analyze(df):
    return df.groupby('country_cleaned')['rating'].mean().reset_index().sort_values(by='rating', ascending=False)

def main():
    # Load the configuration file
    config = load_config()
    
    # Load the data using the path defined in the config
    df = load_data(config['paths']['raw_data'] + "input_data.csv")
    
    # Clean the data
    df = clean_data(df)
    
    # Analyze the cleaned data
    summary = analyze(df)
    
    # Print out the summary of the analysis
    print("Average rating by country:\n", summary)

    # write it to a sql datbase ()
    # sql server (sales.dbo.revenue)
    # dashboard points to the table above(quicksight)
    # everytime the table refreshed the table will show weekly revenue the past week


if __name__ == "__main__":
    main()
