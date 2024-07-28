from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define default arguments for the DAG
default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 7, 23),
    "retries": 1,
}


# Define the download function
def download_data(download_url, local_filepath):
    print(f"Downloading data from {download_url} to {local_filepath}")


# Define the DAG with a schedule interval of None (run manually)
with DAG(
    dag_id="T01_Python_Operator",
    default_args=default_args,
    schedule_interval=None,
) as dag:

    # Define the download task using PythonOperator
    download_task = PythonOperator(
        task_id="download_task",
        python_callable=download_data,
        op_args=[
            # Provide download URL and local filepath as arguments
            "https://www.example.com/data.csv",
            "/tmp/data.csv",
        ],
    )
