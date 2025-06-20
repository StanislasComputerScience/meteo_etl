# export_to_csv.py
# faire un pip install psycopg2-binary
import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path
import csv


# Charger les variables d'environnement
env_path = Path(__file__).resolve().parent / "config" / ".env"
load_dotenv(dotenv_path=env_path)

# Connexion PostgreSQL
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

query = """
SELECT
    s.name AS station,
    s.region,
    wd.timestamp,
    wd.temperature,
    wd.humidity,
    wd.pressure,
    wd.wind_speed
FROM weather_data wd
JOIN stations s ON wd.station_id = s.id
ORDER BY wd.timestamp DESC
"""

df = pd.read_sql(query, conn)
df.to_csv("weather_data.csv", index=False)
print("✅ Données exportées vers weather_data.csv")
