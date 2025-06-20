#!/bin/bash

# Initialiser la base de données Airflow
airflow db init

# Créer un utilisateur admin personnalisé
airflow users create \
    --username Moi \
    --firstname Rémi \
    --lastname LABONNE \
    --role Admin \
    --email remilabonne@yahoo.fr \
    --password meteo123

# Lancer le webserver en arrière-plan (ou garder ce terminal pour logs)
airflow webserver --port 8080 &

# Lancer le scheduler dans un autre terminal, ou ici si souhaité
airflow scheduler
