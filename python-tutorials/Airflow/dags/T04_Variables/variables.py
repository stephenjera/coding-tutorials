from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from airflow.utils.dates import days_ago
from typing import Any

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
}


# This function would typically be run before starting the DAG
def set_airflow_variables():
    Variable.set("data_file_path", "/path/to/data/file.csv")
    Variable.set("processing_limit", 1000)
    Variable.set("email_recipient", "user@example.com")


def extract_data() -> dict[str, Any]:
    """
    Extract data using configuration from Airflow Variables.

    :param context: Airflow context dictionary
    :return: Dictionary with extracted data info
    """

    # Retrieve variables
    file_path = Variable.get("data_file_path")
    limit = int(Variable.get("processing_limit"))

    # Simulate data extraction
    print(f"Extracting data from {file_path}")
    print(f"Processing limit: {limit} records")

    # In a real scenario, you would actually read from the file here
    extracted_data = {"num_records": limit, "source": file_path}

    return extracted_data  # This will be automatically pushed to XCom


def process_data(**context) -> None:
    """
    Process data and use Airflow Variables for configuration.

    :param context: Airflow context dictionary
    """
    ti = context["ti"]

    # Retrieve data from XCom
    extracted_data = ti.xcom_pull(task_ids="extract_data_task", key="return_value")

    # Retrieve variable
    email = Variable.get("email_recipient")

    # Simulate data processing
    print(
        f"Processing {extracted_data['num_records']} records from {extracted_data['source']}"
    )
    print(f"Will send results to {email}")


with DAG(
    "T04_Variables",
    default_args=default_args,
    description="An example DAG demonstrating Airflow Variables and XCom",
    schedule_interval=None,
    catchup=False,
) as dag:
    
    set_variables_task = PythonOperator(
        task_id="set_variables_task",
        python_callable=set_airflow_variables
    )

    extract_data_task = PythonOperator(
        task_id="extract_data_task",
        python_callable=extract_data,
    )

    process_data_task = PythonOperator(
        task_id="process_data_task",
        python_callable=process_data,
    )

    set_variables_task >> extract_data_task >> process_data_task
