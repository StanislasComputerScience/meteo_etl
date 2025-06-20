# 🌤️ Météo ETL – Pipeline de Données Météo pour quelques Villes Françaises

Ce projet implémente un pipeline **ETL (Extract, Transform, Load)** en Python permettant de récupérer, nettoyer et stocker les prévisions météo horaires pour plusieurs villes françaises. Il combine des outils modernes pour le traitement, l'orchestration et la visualisation de données.

---

## 🚀 Objectifs du Projet

- ✅ **Collecter automatiquement** les prévisions météo via l'API Météo Concept.
- ✅ **Nettoyer et structurer** les données (température, humidité, vent, etc.).
- ✅ **Stocker les données** :
  - En **MongoDB** pour les données brutes (à venir).
  - En **PostgreSQL** pour les données nettoyées.
- ✅ **Visualiser** les données dans une interface interactive avec Streamlit.
- 🔜 **Orchestrer** automatiquement le pipeline avec Airflow.

---

## 🛠️ Stack Technique

| Composant      | Rôle                                      |
|----------------|-------------------------------------------|
| Python         | Langage principal                         |
| Requests       | Appels à l'API météo                      |
| Pandas         | Traitement et nettoyage des données       |
| PostgreSQL     | Stockage des données nettoyées            |
| Psycopg2       | Connexion PostgreSQL                      |
| MongoDB        | Stockage NoSQL des données brutes         |
| SQLAlchemy     | ORM (future intégration possible)         |
| Streamlit      | Visualisation interactive                 |
| Airflow        | Orchestration du pipeline ETL (à venir)   |
| Dotenv         | Gestion des variables d’environnement     |

---

## 📁 Structure du Projet

