# transform/clean_data.py

from datetime import datetime
from typing import List, Dict
from extract.fetch import get_forecast


def process_forecast(raw_data: List[Dict]) -> List[Dict]:
    cleaned_data = []

    for entry in raw_data:
        cleaned_entry = {
            "datetime": parse_datetime(entry.get("datetime")),
            "insee": entry.get("insee"),
            "latitude": entry.get("latitude"),
            "longitude": entry.get("longitude"),
            "temperature": entry.get("temp2m"),
            "humidite": entry.get("rh2m"),
            "pluie_mm": entry.get("rr10"),
            "vent_kmh": entry.get("wind10m"),
            "rafale_kmh": entry.get("gust10m"),
            "direction_vent_deg": entry.get("dirwind10m"),
            "code_meteo": entry.get("weather"),
            "source": "meteo-concept",
        }
        cleaned_data.append(cleaned_entry)

    return cleaned_data


def parse_datetime(dt_str: str) -> str:
    """
    Transforme la date au format '2025-06-17T12:00:00+0200' en ISO UTC (str).
    """
    try:
        dt = datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S%z")
        return dt.astimezone().isoformat()
    except Exception as e:
        print(f"Erreur de parsing date: {e}")
        return dt_str  # fallback brut


if __name__ == "__main__":
    from extract.fetch import get_forecast

    raw = get_forecast()
    cleaned = process_forecast(raw)

    print(f"{len(cleaned)} entrées nettoyées :")
    for c in cleaned[:2]:
        print(c)
