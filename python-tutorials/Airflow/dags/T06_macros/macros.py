from datetime import timedelta

from airflow import DAG
from airflow.macros import ds_add
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


# Custom macro function
def custom_greeting(name: str) -> str:
    return f"Hello, {name}! Welcome to Airflow macros."


def print_macro_results(**context):
    print(f"Execution Date: {context['ds']}")
    print(f"Tomorrow's Date: {context['tomorrow_ds']}")
    print(f"Task Instance: {context['task_instance']}")
    print(f"Custom Greeting: {context['custom_greeting']('Airflow User')}")
    print(f"Formatted Date: {context['execution_date'].strftime('%Y-%m-%d')}")
    print(f"7 Days from Now: {ds_add(context['ds'], 7)}")


# DAG definition
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
    "T06_Macros",
    default_args=default_args,
    description="A DAG showcasing various macro usages",
    schedule_interval=None,
    user_defined_macros={"custom_greeting": custom_greeting},
) as dag:

    macro_task = PythonOperator(
        task_id="macro_showcase_task",
        python_callable=print_macro_results,
        provide_context=True,
        op_kwargs={
            "custom_greeting": custom_greeting,
            "tomorrow_ds": "{{ macros.ds_add(ds, 1) }}",
        },
    )

macro_task
