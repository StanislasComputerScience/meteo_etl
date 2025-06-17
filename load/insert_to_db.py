# load/insert_to_db.py

import sys
from pathlib import Path

# ✅ Ajouter le dossier racine au PYTHONPATH AVANT les imports locaux
sys.path.append(str(Path(__file__).resolve().parent.parent))

import os
import psycopg2
from dotenv import load_dotenv

# imports locaux
from transform.clean_data import process_forecast
from extract.fetch import get_forecast

# Charger les variables d'environnement
env_path = Path(__file__).resolve().parent.parent / "config" / ".env"
load_dotenv(dotenv_path=env_path)

DB_NAME = os.getenv("DB_NAME", "meteo")
DB_USER = os.getenv("DB_USER", "meteo_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "meteo123")
DB_HOST = os.getenv("DB_HOST", "localhost")

stations = [
    ("Station Paris", 48.8566, 2.3522, "Île-de-France"),
    ("Station Marseille", 43.2965, 5.3698, "Provence-Alpes-Côte d'Azur"),
    ("Station Lyon", 45.7640, 4.8357, "Auvergne-Rhône-Alpes"),
    ("Station Lille", 50.6292, 3.0573, "Hauts-de-France"),
    ("Station Calais", 50.9513, 1.8587, "Hauts-de-France"),
    ("Station Dunkerque", 51.0344, 2.3768, "Hauts-de-France"),
    ("Station Poitiers", 46.5802, 0.3404, "Nouvelle-Aquitaine"),
    ("Station Niort", 46.3239, -0.4583, "Nouvelle-Aquitaine"),
    ("Station Toulon", 43.1242, 5.9280, "Provence-Alpes-Côte d'Azur"),
    ("Station Toulouse", 43.6047, 1.4442, "Occitanie"),
]


# Connexion PostgreSQL
conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
)
cur = conn.cursor()


def insert_stations_if_not_exists():
    """Insère les stations si elles n'existent pas encore."""
    for station in stations:
        cur.execute(
            """
            INSERT INTO stations (name, latitude, longitude, region)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (name) DO NOTHING
            """,
            station,
        )
    conn.commit()


def get_all_stations():
    """Retourne la liste des stations (id, name) en base."""
    cur.execute("SELECT id, name FROM stations")
    return cur.fetchall()  # liste de tuples (id, name)


def insert_forecast_data_for_all_stations():
    stations_in_db = get_all_stations()
    total_inserted = 0

    for station_id, station_name in stations_in_db:
        print(f"Récupération données météo pour {station_name}...")
        raw = get_forecast(
            station_name
        )  # à adapter dans get_forecast pour passer le nom ou coords
        cleaned = process_forecast(raw)

        if not cleaned:
            print(f"⚠️ Aucune donnée pour {station_name}.")
            continue

        for entry in cleaned:
            cur.execute(
                """
                INSERT INTO weather_data (
                    station_id, timestamp, temperature, humidity, pressure, wind_speed
                ) VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING
                """,
                (
                    station_id,
                    entry["datetime"],
                    entry["temperature"],
                    entry["humidite"],
                    1013,  # à adapter si tu as la pression réelle
                    entry["vent_kmh"],
                ),
            )
        conn.commit()
        total_inserted += len(cleaned)
        print(f"✅ {len(cleaned)} entrées insérées pour {station_name}.")

    print(f"Total entrées insérées : {total_inserted}")


if __name__ == "__main__":
    insert_stations_if_not_exists()
    insert_forecast_data_for_all_stations()
    cur.close()
    conn.close()
