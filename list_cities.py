# from pathlib import Path
# import os
# from dotenv import load_dotenv

# # ✅ Chemin corrigé vers le bon dossier
# env_path = Path(__file__).resolve().parent / "config" / ".env"
# print(f"🔍 Chargement de : {env_path}")
# load_dotenv(dotenv_path=env_path)

# API_TOKEN = os.getenv("API_TOKEN")
# print(f"TOKEN => {API_TOKEN}")
import os
import requests
from dotenv import load_dotenv
from pathlib import Path
import time
import json

# ✅ Chargement du .env depuis le dossier parent /config/
env_path = Path(__file__).resolve().parent / "config" / ".env"
print(f"🔍 Chargement de : {env_path}")
load_dotenv(dotenv_path=env_path)

API_TOKEN = os.getenv("API_TOKEN")
print(f"TOKEN => {API_TOKEN}")

if not API_TOKEN:
    raise ValueError("❌ Le token API est manquant. Vérifie ton fichier .env")


def search_cities_by_letter(letter):
    url = "https://api.meteo-concept.com/api/location/cities"
    params = {"token": API_TOKEN, "search": letter, "limit": 1000}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("cities", [])


def get_all_cities():
    all_cities = {}
    for letter in "abcdefghijklmnopqrstuvwxyz":
        print(f"🔎 Recherche pour: {letter}")
        cities = search_cities_by_letter(letter)
        for city in cities:
            insee = city["insee"]
            if insee not in all_cities:
                all_cities[insee] = city
        time.sleep(0.5)  # 💤 éviter de trop solliciter l'API
    return list(all_cities.values())


if __name__ == "__main__":
    cities = get_all_cities()
    print(f"✅ {len(cities)} villes uniques récupérées.")

    # Sauvegarde en JSON (optionnel)
    with open("cities.json", "w", encoding="utf-8") as f:
        json.dump(cities, f, ensure_ascii=False, indent=2)
    print("💾 Données enregistrées dans cities.json")
