from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 6),
    'retries': 1,
}

dag = DAG(
    'extract_data_ad',
    default_args=default_args,
    description='A simple DockerOperator example',
    schedule_interval='@daily',
)

docker_task = DockerOperator(
    task_id='extract',
    image='your_image:latest',
    api_version='auto',
    auto_remove=True,
    docker_url='tcp://docker-socket-proxy:2375',
    dag=dag,
    command="",
    force_pull=False,
)

docker_task
