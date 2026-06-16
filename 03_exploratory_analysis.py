"""
03_exploratory_analysis.py

Analyse exploratoire :
- nombre de restaurants par arrondissement ;
- note moyenne par type de cuisine ;
- relation entre note et nombre d'avis.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_PATH = BASE_DIR / "outputs" / "cleaned_restaurants.csv"
OUTPUT_DIR = BASE_DIR / "outputs"


def main() -> None:
    df = pd.read_csv(INPUT_PATH)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Restaurants par arrondissement
    arr_counts = df["arrondissement"].value_counts().sort_index()
    plt.figure(figsize=(8, 5))
    arr_counts.plot(kind="bar")
    plt.xlabel("Arrondissement")
    plt.ylabel("Nombre de restaurants")
    plt.title("Répartition des restaurants chinois par arrondissement")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "restaurants_by_arrondissement.png", dpi=300)

    # Note moyenne par type de cuisine
    cuisine_rating = df.groupby("cuisine_type")["rating"].mean().sort_values()
    plt.figure(figsize=(8, 5))
    cuisine_rating.plot(kind="barh")
    plt.xlabel("Note moyenne")
    plt.title("Note moyenne par type de cuisine")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "average_rating_by_cuisine.png", dpi=300)

    # Note vs nombre d'avis
    plt.figure(figsize=(7, 5))
    plt.scatter(df["review_count"], df["rating"])
    plt.xlabel("Nombre d'avis")
    plt.ylabel("Note moyenne")
    plt.title("Relation entre popularité et note")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "rating_vs_reviews.png", dpi=300)

    print("Graphiques exploratoires sauvegardés dans outputs/")


if __name__ == "__main__":
    main()
