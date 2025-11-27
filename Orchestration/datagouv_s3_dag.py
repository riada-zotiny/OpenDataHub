import sys
import os
sys.path.append("/mnt/c/Users/akram/Documents/OpendataHub/src")
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

from datetime import datetime
from datagouv_client import get_dataset_metadata, find_resource_for_format
from downloader import download_file
from s3_uploader import upload_file_to_s3
from config import S3_BUCKET, AWS_REGION, DATASET_SLUG

# Récupération des métadonnées
def fetch_metadata(ti):
    dataset_meta = get_dataset_metadata(DATASET_SLUG)
    ti.xcom_push(key='dataset_meta',value=dataset_meta)
    print("Métadonnées récupérées")

#Récupération des sources de données à partir des métadonnées
def select_resource(ti):
    dataset_meta = ti.xcom_pull(key='dataset_meta', task_ids='fetch_metadata')
    resource = find_resource_for_format(dataset_meta, prefer_formats=("xlsx","xls"))
    if not resource:
      raise ValueError("Aucune ressource XLS/XLSX troouvée")
    ti.xcom_push(key='resource', value=resource)
    print(f"Ressource sélectionnée")

#Téléchargement temporaire des sources de données dans un dossier
def download_resource(ti):
    resource = ti.xcom_pull(key='resource',task_ids='select_ressource')
    url = resource["url"]
    if not resource:
        raise ValueError("Resource est vide ! Vérifie le XCom de la tâche précédente")
    file_name = resource.get("title") or os.path.basename(url)
    local_path = f"./OpendataHub/data_temp/{file_name}"
    download_file(url,local_path)
    ti.xcom_push(key='local_path', value=local_path)
    print("Fichier téléchargé")

# Stocker les sources de données dans le service S3
def upload_to_s3(ti):
    local_path = ti.xcom_pull(key='local_path',task_ids='download_ressource')
    resource = ti.xcom_pull(key='resource', task_ids='select_ressource')
    file_name = resource.get("title") or os.path.basename(resource["url"])
    s3_key = f"xlsx_version2/{file_name}"
    upload_file_to_s3(local_path, S3_BUCKET, s3_key ,AWS_REGION)
    print("Fichier upload sur S3")


with DAG(
    dag_id="orchestration_ingestion",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    start = EmptyOperator(
	task_id="start",

    )

    t1 = PythonOperator(
	task_id="fetch_metadata",
        python_callable=fetch_metadata,
    )

    t2 = PythonOperator(
	task_id="select_ressource",
        python_callable=select_resource,

    )

    t3 = PythonOperator(
	task_id="download_ressource", 
	python_callable=download_resource,
    )

    t4 = PythonOperator(
	task_id="Upload_s3",
        python_callable=upload_to_s3,
    )

    end = EmptyOperator(
	task_id="end"
    )


start >> t1 >> t2 >> t3 >> t4 >> end
