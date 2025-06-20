import streamlit as st
import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os
from pathlib import Path

# Chargement du .env
env_path = Path(__file__).resolve().parent / "config" / ".env"
load_dotenv(dotenv_path=env_path)

DB_NAME = os.getenv("DB_NAME", "meteo")
DB_USER = os.getenv("DB_USER", "meteo_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "meteo123")
DB_HOST = os.getenv("DB_HOST", "localhost")

# Connexion DB
@st.cache_data
def load_data():
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
    )
    query = """
        SELECT
            s.name AS station,
            wd.timestamp,
            wd.temperature,
            wd.humidity,
            wd.wind_speed
        FROM weather_data wd
        JOIN stations s ON wd.station_id = s.id
        ORDER BY wd.timestamp DESC
        LIMIT 500;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Streamlit UI
st.title("🌦️ Visualisation des Données Météo")
df = load_data()

st.write("Aperçu des données :")
st.dataframe(df)

st.subheader("📈 Température par station")
station = st.selectbox("Choisir une station", df["station"].unique())
df_station = df[df["station"] == station]

st.line_chart(df_station.set_index("timestamp")["temperature"])
