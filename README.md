# meteo_etl# 🌤️ Météo ETL – Pipeline de Données Météo pour quelques Villes Françaises

Ce projet implémente un pipeline **ETL (Extract, Transform, Load)** en Python permettant de récupérer, nettoyer et stocker les prévisions météo horaires pour les principales villes françaises. Il combine des technologies modernes pour le traitement et la gestion de données.

---

## 🚀 Objectifs du Projet

- Collecter automatiquement les prévisions météo depuis une API externe (Météo Concept).
- Nettoyer et structurer les données météo (température, humidité, vent, etc.).
- Stocker les données :
  - En **MongoDB** pour les données brutes.
  - En **PostgreSQL** pour les données nettoyées.

- Permettre des requêtes et analyses sur les données consolidées.

---

## 🛠️ Stack Technique

| Composant     | Utilisation                          |
|---------------|--------------------------------------|
| Python        | Logique ETL                          |
| Requests      | Requête API                          |
| PostgreSQL    | Stockage des données nettoyées       |
| Psycopg2      | Connexion PostgreSQL                 |
| Dotenv        | Gestion des variables d’environnement|

---

## 📦 Structure du Projet

meteo_etl/
├── config/ # Fichier .env
├── extract/ # Scripts d'extraction API
│ └── fetch.py
├── transform/ # Nettoyage et normalisation
│ └── clean_data.py
├── load/ # Insertion dans les bases de données
│ └── insert_to_db.py
├── read_data.py # Script pour lire les données depuis PostgreSQL
├── requirements.txt
└── README.md



à venir :
- Orchestration du pipeline avec **Apache Airflow** (en local).

| Pandas        | Transformation des données           |
| MongoDB       | Stockage des données brutes          |
| Airflow       | Orchestration du pipeline            |

├── airflow_dags/ # DAGs pour Airflow