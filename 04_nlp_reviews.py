"""
04_nlp_reviews.py

Analyse NLP simple des avis clients :
- extraction des mots-clés ;
- analyse de sentiment basée sur un lexique simple.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_PATH = BASE_DIR / "outputs" / "cleaned_restaurants.csv"
KEYWORDS_PATH = BASE_DIR / "outputs" / "review_keywords.csv"
SENTIMENT_PATH = BASE_DIR / "outputs" / "reviews_with_sentiment.csv"
FIGURE_PATH = BASE_DIR / "outputs" / "top_review_keywords.png"

POSITIVE_WORDS = {
    "bon", "bonne", "bons", "excellents", "excellent", "agréable",
    "gentil", "rapide", "authentique", "savoureuse", "frais",
    "raisonnable", "copieuses", "généreux"
}

NEGATIVE_WORDS = {
    "bruyante", "longue", "variable", "élevés", "simple", "attente"
}


def sentiment_score(text: str) -> int:
    words = set(str(text).split())
    return len(words & POSITIVE_WORDS) - len(words & NEGATIVE_WORDS)


def sentiment_label(score: int) -> str:
    if score > 0:
        return "positive"
    if score < 0:
        return "negative"
    return "neutral"


def main() -> None:
    df = pd.read_csv(INPUT_PATH)

    vectorizer = CountVectorizer(
        stop_words=["le", "la", "les", "de", "des", "du", "et", "est", "un", "une", "très", "pour"],
        ngram_range=(1, 2),
        min_df=1
    )

    matrix = vectorizer.fit_transform(df["clean_review"])
    terms = vectorizer.get_feature_names_out()
    frequencies = matrix.sum(axis=0).A1

    keywords = (
        pd.DataFrame({"term": terms, "frequency": frequencies})
        .sort_values("frequency", ascending=False)
        .head(20)
    )
    keywords.to_csv(KEYWORDS_PATH, index=False)

    plt.figure(figsize=(10, 6))
    plt.barh(keywords["term"][::-1], keywords["frequency"][::-1])
    plt.xlabel("Fréquence")
    plt.title("Mots-clés les plus fréquents dans les avis clients")
    plt.tight_layout()
    plt.savefig(FIGURE_PATH, dpi=300)

    df["sentiment_score"] = df["clean_review"].apply(sentiment_score)
    df["sentiment"] = df["sentiment_score"].apply(sentiment_label)
    df.to_csv(SENTIMENT_PATH, index=False)

    print(f"Mots-clés sauvegardés : {KEYWORDS_PATH}")
    print(f"Avis avec sentiment sauvegardés : {SENTIMENT_PATH}")


if __name__ == "__main__":
    main()
