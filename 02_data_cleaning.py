"""
02_data_cleaning.py

Nettoyage et structuration des données de restaurants chinois à Paris.
"""

from pathlib import Path
import re
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "paris_chinese_restaurants_sample.csv"
OUTPUT_PATH = BASE_DIR / "outputs" / "cleaned_restaurants.csv"


def clean_text(text: object) -> str:
    if pd.isna(text):
        return ""
    text = str(text).lower()
    text = re.sub(r"[^a-zA-ZÀ-ÿ\s']", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def main() -> None:
    df = pd.read_csv(DATA_PATH)

    df = df.drop_duplicates(subset=["restaurant_name", "address"])

    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df["review_count"] = pd.to_numeric(df["review_count"], errors="coerce")
    df["arrondissement"] = pd.to_numeric(df["arrondissement"], errors="coerce")

    df["rating"] = df["rating"].fillna(df["rating"].median())
    df["review_count"] = df["review_count"].fillna(0)
    df["arrondissement"] = df["arrondissement"].fillna(-1).astype(int)

    df["clean_review"] = df["review_text"].apply(clean_text)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Données nettoyées sauvegardées : {OUTPUT_PATH}")
    print(df.head())


if __name__ == "__main__":
    main()
