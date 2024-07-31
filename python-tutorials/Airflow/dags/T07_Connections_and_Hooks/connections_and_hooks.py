from datetime import timedelta

from airflow import DAG, settings
from airflow.models import Connection
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago


# Example only, use Airflow UI or CLI for better security
def create_or_update_connection(
    conn_id, conn_type, host, login, password, port, schema
):
    session = settings.Session()

    # Check if connection exists
    existing_conn = session.query(Connection).filter_by(conn_id=conn_id).first()

    if existing_conn:
        # Update existing connection
        existing_conn.conn_type = conn_type
        existing_conn.host = host
        existing_conn.login = login
        existing_conn.password = password
        existing_conn.port = port
        existing_conn.schema = schema
    else:
        # Create new connection
        connection = Connection(
            conn_id=conn_id,
            conn_type=conn_type,
            host=host,
            login=login,
            password=password,
            port=port,
            schema=schema,
        )
        session.add(connection)

    session.commit()
    session.close()


def test_connection():
    pg_hook = PostgresHook(postgres_conn_id="postgres_conn")
    conn = pg_hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    result = cursor.fetchone()
    print(f"PostgreSQL version: {result[0]}")  # type: ignore
    cursor.close()
    conn.close()


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
    "T07_Connections_and_Hooks",
    default_args=default_args,
    description="A DAG showcasing connections usage",
    schedule_interval=None,
) as dag:

    create_connection_task = PythonOperator(
        task_id="create_connection",
        python_callable=create_or_update_connection,
        op_kwargs={
            "conn_id": "postgres_conn",
            "conn_type": "postgres",
            "host": "host.docker.internal",
            "login": "postgres",
            "password": "postgres",
            "port": 5432,
            "schema": "postgres",
        },
    )

    test_connection_task = (
        PythonOperator(
            task_id="test_connection",
            python_callable=test_connection,
        ),
    )

create_connection_task >> test_connection_task
