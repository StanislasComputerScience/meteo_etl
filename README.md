# 🌤️ Météo ETL – Pipeline de Données Météo pour quelques Villes Françaises

Ce projet implémente un pipeline **ETL (Extract, Transform, Load)** en Python permettant de récupérer, nettoyer et stocker les prévisions météo horaires pour plusieurs villes françaises. Il combine des outils modernes pour le traitement, l'orchestration et la visualisation de données.

---

## 🚀 Objectifs du Projet

- ✅ **Collecter automatiquement** les prévisions météo via l'API Météo Concept.
- ✅ **Nettoyer et structurer** les données (température, humidité, vent, etc.).
- ✅ **Stocker les données** :
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
| Streamlit      | Visualisation interactive                 |
| Airflow        | Orchestration du pipeline ETL (à venir)   |
| Dotenv         | Gestion des variables d’environnement     |

---

## 📁 Structure du projet

```text
meteo_etl/
├── airflow_dags/           # 🔜 DAGs Airflow (pipeline automatique)
├── config/
│   └── .env                # Token API, INSEE code, credentials
├── data/
│   └── create_tables_data.py   # Création des tables PostgreSQL
├── extract/
│   └── fetch_data.py       # Récupération via API Météo Concept
├── transform/
│   └── clean_data.py       # Nettoyage et formatage des données
├── load/
│   └── insert_to_db.py     # Insertion dans la base PostgreSQL
├── visualise.py            # Interface Streamlit pour explorer les données
├── read_data.py            # Lecture simple depuis PostgreSQL
├── requirements.txt        # Dépendances Python
└── README.md               # Documentation du projet


## ⚙️ Utilisation

### 1. Configuration

Créer un fichier `.env` dans le dossier `config/` :

```env
API_TOKEN=your_api_token_here
INSEE_CODE=75056
DB_NAME=meteo
DB_USER=meteo_user
DB_PASSWORD=meteo123
DB_HOST=localhost

### 2. Installation des dépendances
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

### 3. Lancer le pipeline ETL manuellement
python load/insert_to_db.py

### 4. Lancer Aiflow
./run_airflow.sh

### 📊 Exemple de Visualisation
L’interface Streamlit permet de :

Sélectionner une station météo

Afficher les températures horaires

Explorer les humidités, vents, pressions, etc.

Visualiser les données brutes sous forme de tableau

### 🧑‍💻 Auteur
Projet réalisé par Rémi LABONNE

### 📄 Licence
Ce projet est open-source, sous licence MIT.
