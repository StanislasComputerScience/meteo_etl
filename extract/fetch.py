# extract/fetch_data.py

import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# On charge le .env situé dans le dossier parent /config/
env_path = Path(__file__).resolve().parent.parent / "config" / ".env"
load_dotenv(dotenv_path=env_path)

API_TOKEN = os.getenv("API_TOKEN")

INSEE_CODE = os.getenv("INSEE_CODE", "75056")  # Paris par défaut

BASE_URL = "https://api.meteo-concept.com/api/forecast/nextHours"


def get_forecast(insee=INSEE_CODE):
    params = {"token": API_TOKEN, "insee": insee}

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("forecast", [])
    except requests.RequestException as e:
        print(f"Erreur lors de la requête API : {e}")
        return []


if __name__ == "__main__":
    forecast = get_forecast()
    print(f"Prévisions récupérées ({len(forecast)} éléments) :")
    for entry in forecast[:3]:  # Aperçu des 3 premières heures
        print(entry)
