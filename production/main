import pandas as pd
from config import INPUT_FILE
from constants import COUNTRY_NAME_MAP
from utils.cleaning import clean_country, clean_text, clean_text_extra

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df['country_cleaned'] = df['country'].apply(lambda x: clean_country(x, COUNTRY_NAME_MAP))
    df['comments_cleaned'] = df['comments'].apply(clean_text)
    df['comments_cleaned'] = df['comments_cleaned'].apply(clean_text_extra)
    df['comment_length'] = df['comments_cleaned'].apply(lambda x: len(x.split(" ")))
    return df

def analyze(df):
    return df.groupby('country_cleaned')['rating'].mean().reset_index().sort_values(by='rating', ascending=False)

def main():
    df = load_data(INPUT_FILE)
    df = clean_data(df)
    summary = analyze(df)
    print("Average rating by country:\n", summary)

if __name__ == "__main__":
    main()
