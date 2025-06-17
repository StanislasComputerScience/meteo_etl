import psycopg2

# Connexion à PostgreSQL
conn = psycopg2.connect(
    dbname="meteo", user="meteo_user", password="meteo123", host="localhost"
)
cur = conn.cursor()

# Drop + Create tables
cur.execute(
    """
DROP TABLE IF EXISTS weather_data;
DROP TABLE IF EXISTS stations;

CREATE TABLE stations (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    region TEXT
);

CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    station_id INT REFERENCES stations(id) ON DELETE CASCADE,
    timestamp TIMESTAMP NOT NULL,
    temperature FLOAT,
    humidity FLOAT,
    pressure FLOAT,
    wind_speed FLOAT
);

ALTER TABLE stations ADD CONSTRAINT unique_station_name UNIQUE(name);
"""
)

# Exécution et commit
conn.commit()
cur.close()
conn.close()

print("✅ Tables créées avec succès.")
