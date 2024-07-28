from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 7, 23),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def print_task_name(task_name):
    print(f"Executing task: {task_name}")

with DAG('T02_Task_Dependency',
         default_args=default_args,
         description='A DAG demonstrating various task dependency patterns',
         schedule_interval=timedelta(days=1),
         ) as dag:

    # Start and end tasks
    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    # Linear dependency
    task_a = PythonOperator(
        task_id='task_a',
        python_callable=print_task_name,
        op_args=['Task A']
    )
    task_b = BashOperator(
        task_id='task_b',
        bash_command='echo "Executing Task B"'
    )
    task_c = PythonOperator(
        task_id='task_c',
        python_callable=print_task_name,
        op_args=['Task C']
    )

    # Fan-out dependency
    task_d = BashOperator(
        task_id='task_d',
        bash_command='echo "Executing Task D"'
    )
    task_e = PythonOperator(
        task_id='task_e',
        python_callable=print_task_name,
        op_args=['Task E']
    )
    task_f = BashOperator(
        task_id='task_f',
        bash_command='echo "Executing Task F"'
    )

    # Fan-in dependency
    task_g = PythonOperator(
        task_id='task_g',
        python_callable=print_task_name,
        op_args=['Task G']
    )

    # Complex dependencies
    task_h = BashOperator(
        task_id='task_h',
        bash_command='echo "Executing Task H"'
    )
    task_i = PythonOperator(
        task_id='task_i',
        python_callable=print_task_name,
        op_args=['Task I']
    )

    # Define task dependencies

    # Linear dependency
    start >> task_a >> task_b >> task_c

    # Fan-out dependency
    task_c >> [task_d, task_e, task_f]

    # Fan-in dependency
    [task_d, task_e, task_f] >> task_g

    # Complex dependencies
    task_b >> task_h >> task_i
    task_e >> task_i

    # Connect to end task
    [task_c, task_g, task_i] >> end

    # Alternative syntax for setting dependencies
    # start.set_downstream(task_a)
    # task_g.set_upstream([task_d, task_e, task_f])
    # end.set_upstream([task_c, task_g, task_i])