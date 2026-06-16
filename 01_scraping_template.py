"""
01_scraping_template.py

Template de web scraping pour collecter des informations sur des restaurants.

Remarque :
Ce script est volontairement générique. Avant tout scraping réel, il faut vérifier :
- les conditions d'utilisation du site ;
- le fichier robots.txt ;
- la fréquence des requêtes.
"""

import time
import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_restaurants_example(url: str) -> pd.DataFrame:
    """
    Exemple de fonction de scraping.
    À adapter selon la structure HTML réelle du site ciblé.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 educational project"
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    restaurants = []

    # Exemple générique : à modifier selon les balises du site.
    for item in soup.select(".restaurant-card"):
        name = item.select_one(".name")
        rating = item.select_one(".rating")
        address = item.select_one(".address")

        restaurants.append(
            {
                "restaurant_name": name.get_text(strip=True) if name else None,
                "rating": rating.get_text(strip=True) if rating else None,
                "address": address.get_text(strip=True) if address else None,
            }
        )

        time.sleep(1)

    return pd.DataFrame(restaurants)


if __name__ == "__main__":
    print("Template de scraping : à adapter à une source réelle.")
