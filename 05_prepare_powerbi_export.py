"""
05_prepare_powerbi_export.py

Préparation d'un fichier final pour Power BI.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_PATH = BASE_DIR / "outputs" / "reviews_with_sentiment.csv"
OUTPUT_PATH = BASE_DIR / "dashboard" / "powerbi_restaurants_dataset.csv"


def main() -> None:
    df = pd.read_csv(INPUT_PATH)

    columns = [
        "restaurant_name",
        "address",
        "arrondissement",
        "cuisine_type",
        "rating",
        "review_count",
        "sentiment",
        "sentiment_score",
        "review_text",
    ]

    export_df = df[columns].copy()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    export_df.to_csv(OUTPUT_PATH, index=False)

    print(f"Dataset pour Power BI sauvegardé : {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
