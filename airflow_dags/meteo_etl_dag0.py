# airflow_dags/meteo_etl_dag.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'patrick',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='meteo_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',  # tous les jours
    catchup=False,
    description='Pipeline météo automatisé',
    tags=['meteo', 'ETL']
) as dag:

    extract = BashOperator(
        task_id='extract_data',
        bash_command='python3 /chemin/vers/extract/fetch_data.py'
    )

    transform_load = BashOperator(
        task_id='transform_and_load',
        bash_command='python3 /chemin/vers/load/insert_to_db.py'
    )

    extract >> transform_load
