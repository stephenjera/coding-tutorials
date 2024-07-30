from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "T05_Templates",
    default_args=default_args,
    description="A simple DAG demonstrating template usage",
    schedule_interval=None,
) as dag:

    # Task 1: Print the execution date
    print_date = BashOperator(
        task_id="print_date",
        bash_command='echo "Execution Date: {{ ds }}"',
    )

    # Task 2: Print a custom message with the year
    print_year_message = BashOperator(
        task_id="print_year_message",
        bash_command='echo "The year is {{ execution_date.year }}"',
    )

    # Task 3: Use Jinja templating for a more complex command
    complex_command = BashOperator(
        task_id="complex_command",
        bash_command="""
            echo "Task Instance: {{ task_instance }}"
            echo "DAG: {{ task.dag_id }}"
            echo "Execution Date: {{ ds }}"
            echo "Previous Execution Date: {{ prev_ds }}"
            echo "Next Execution Date: {{ next_ds }}"
        """,
    )

# Set task dependencies
print_date >> print_year_message >> complex_command
