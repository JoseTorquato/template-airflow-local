import requests
import logging
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


logging.basicConfig(level=logging.INFO)

def get_profile_url_from_guithub():
    usuario = "giovanag13"
    url = f"https://api.github.com/users/{usuario}"
    resposta = requests.get(url)
    perfil = resposta.json().get('html_url') if resposta.status_code == 200 else "Perfil não encontrado"
    logging.info(f"Aqui está o perfil: {perfil}")

with DAG(
    dag_id="giovanag13",
    start_date=datetime(2024, 8, 1),
    schedule_interval="*/1 * * * *",
    catchup=False
) as dag:
    tarefa_buscar_perfil = PythonOperator(
        task_id="tarefa_buscar_perfil",
        python_callable=buscar_url_perfil
    )

    tarefa_buscar_perfil
