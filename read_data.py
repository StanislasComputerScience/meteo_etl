import sys
import os
import psycopg2  # <== IMPORT MANQUANT AJOUTÉ

DB_NAME = os.getenv("DB_NAME", "meteo")
DB_USER = os.getenv("DB_USER", "meteo_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "meteo123")
DB_HOST = os.getenv("DB_HOST", "localhost")

# Connexion PostgreSQL
conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
)
cur = conn.cursor()


def get_values():
    """Retourne les données des stations en base."""
    cur.execute(
        """
        SELECT
            wd.id,
            s.name AS station_name,
            s.region,
            wd.timestamp,
            wd.temperature,
            wd.humidity,
            wd.pressure,
            wd.wind_speed
        FROM
            weather_data wd
        JOIN
            stations s ON wd.station_id = s.id
        ORDER BY
            station_name,
            wd.timestamp DESC;
        """
    )
    return cur.fetchall()


def get_LILLE_values():
    """Retourne les données des stations en base."""
    cur.execute(
        """
            SELECT
                wd.id,
                s.name AS station_name,
                wd.timestamp,
                wd.temperature,
                wd.humidity,
                wd.pressure,
                wd.wind_speed
            FROM
                weather_data wd
            JOIN
                stations s ON wd.station_id = s.id
            WHERE
                s.id = 14
            ORDER BY
                s.name,
                wd.timestamp DESC;
        """
    )
    return cur.fetchall()


if __name__ == "__main__":
    rows = get_values()
    #rows = get_LILLE_values()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
