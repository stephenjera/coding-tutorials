from datetime import timedelta

import mlflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

with DAG(
    "mlflow_example_dag",
    default_args={
        "owner": "airflow",
        "depends_on_past": False,
        "start_date": days_ago(1),
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    schedule_interval=None,
) as dag:

    def log_mlflow_experiment():
        mlflow.set_tracking_uri("http://host.docker.internal:5000")
        with mlflow.start_run(
            experiment_id="0"
        ) as run:  # Replace 0 with your experiment ID
            mlflow.log_param("learning_rate", 0.1)
            mlflow.log_metric("accuracy", 0.9)
            # mlflow.log_artifact("model.pkl")  # Replace with your model path

    log_mlflow_task = PythonOperator(
        task_id="log_mlflow_experiment", python_callable=log_mlflow_experiment
    )

log_mlflow_task
