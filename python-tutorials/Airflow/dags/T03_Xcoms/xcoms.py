from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from pprint import pprint

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
}


def generate_data(**context) -> dict[str, int]:
    """
    Generate some data and push it to XCom.

    :param context: Airflow context dictionary
    :return: Dictionary with generated data
    """
    data = {"value1": 42, "value2": 123}
    context["ti"].xcom_push(key="generated_data", value=data)
    pprint(context)
    return data


def process_data(**context) -> None:
    """
    Retrieve data from XCom and process it.

    :param context: Airflow context dictionary
    """
    ti = context["ti"]
    data = ti.xcom_pull(task_ids="generate_data_task", key="generated_data")

    if not data:
        raise ValueError("No data received from generate_data_task")

    result = data["value1"] + data["value2"]
    print(f"Processed result: {result}")


with DAG(
    "T03_Xcoms",
    default_args=default_args,
    description="An example DAG demonstrating XCom usage",
    schedule_interval=None,
    catchup=False,
) as dag:

    generate_data_task = PythonOperator(
        task_id="generate_data_task",
        python_callable=generate_data,
    )

    process_data_task = PythonOperator(
        task_id="process_data_task",
        python_callable=process_data,
    )

    generate_data_task >> process_data_task
