# airflow_dags/meteo_etl_dag.py

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Arguments communs pour toutes les tâches
default_args = {
    "owner": "Rémi",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

# Définition du DAG
with DAG(
    dag_id="meteo_etl_pipeline",
    default_args=default_args,
    description="Pipeline ETL météo - Extract, Transform, Load",
    schedule_interval="@daily",  # tous les jours
    catchup=False,
    tags=["meteo", "ETL"],
) as dag:

    # Étape 1 - Extraction
    extract = BashOperator(
        task_id="extract_data",
        bash_command="python3 /home/patrick/Simplon/meteo_etl/extract/fetch_data.py",
    )

    # Étape 2 - Transformation
    transform = BashOperator(
        task_id="transform_data",
        bash_command="python3 /home/patrick/Simplon/meteo_etl/transform/clean_data.py",
    )

    # Étape 3 - Chargement
    load = BashOperator(
        task_id="load_data",
        bash_command="python3 /home/patrick/Simplon/meteo_etl/load/insert_to_db.py",
    )

    # Orchestration des tâches
    extract >> transform >> load
