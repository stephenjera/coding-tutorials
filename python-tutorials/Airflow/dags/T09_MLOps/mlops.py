import base64
import logging
import pickle
from datetime import timedelta
from math import sqrt

import mlflow
import pandas as pd
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MLflow settings
mlflow.set_tracking_uri(Variable.get("mlflow_tracking_uri", "http://host.docker.internal:5000"))
mlflow.set_experiment("california_housing_prediction")

# Load configuration
RANDOM_STATE = int(Variable.get("random_state", 42))
TEST_SIZE = float(Variable.get("test_size", 0.2))

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

def load_and_preprocess_data(**context):
    with mlflow.start_run(run_name="data_preprocessing") as run:
        try:
            logger.info("Starting data preprocessing")
            housing = fetch_california_housing()
            df = pd.DataFrame(housing.data, columns=housing.feature_names)
            df["MedHouseValue"] = housing.target
            df = df.drop(df.loc[df["MedHouseValue"] == max(df["MedHouseValue"])].index)

            X = df.drop("MedHouseValue", axis=1)
            y = df["MedHouseValue"]

            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)

            X_train, X_test, y_train, y_test = train_test_split(
                X_scaled, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
            )

            # Log parameters
            mlflow.log_param("random_state", RANDOM_STATE)
            mlflow.log_param("test_size", TEST_SIZE)

            # Log preprocessed data stats
            mlflow.log_metric("train_samples", X_train.shape[0])
            mlflow.log_metric("test_samples", X_test.shape[0])

            logger.info("Data preprocessing completed")

            # Store data in XCom for next tasks
            context['ti'].xcom_push(key='X_train', value=X_train.tolist())
            context['ti'].xcom_push(key='X_test', value=X_test.tolist())
            context['ti'].xcom_push(key='y_train', value=y_train.tolist())
            context['ti'].xcom_push(key='y_test', value=y_test.tolist())

        except Exception as e:
            logger.error(f"Error in data preprocessing: {str(e)}")
            raise

def train_model(**context):
    with mlflow.start_run(run_name="model_training") as run:
        try:
            logger.info("Starting model training")
            
            # Retrieve data from XCom
            X_train = context['ti'].xcom_pull(task_ids='load_and_preprocess_data', key='X_train')
            y_train = context['ti'].xcom_pull(task_ids='load_and_preprocess_data', key='y_train')

            X_train = pd.DataFrame(X_train)
            y_train = pd.Series(y_train)

            model = LinearRegression()
            model.fit(X_train, y_train)

            # Log model
            mlflow.sklearn.log_model(model, "model")

            logger.info("Model training completed")

            # Serialize model using pickle and encode as base64
            pickled_model = pickle.dumps(model)
            encoded_model = base64.b64encode(pickled_model).decode('utf-8')

            # Store encoded model in XCom
            context['ti'].xcom_push(key='model', value=encoded_model)

        except Exception as e:
            logger.error(f"Error in model training: {str(e)}")
            raise

def evaluate_model(**context):
    with mlflow.start_run(run_name="model_evaluation") as run:
        try:
            logger.info("Starting model evaluation")
            
            # Retrieve data and encoded model from XCom
            X_test = context['ti'].xcom_pull(task_ids='load_and_preprocess_data', key='X_test')
            y_test = context['ti'].xcom_pull(task_ids='load_and_preprocess_data', key='y_test')
            encoded_model = context['ti'].xcom_pull(task_ids='train_model', key='model')

            X_test = pd.DataFrame(X_test)
            y_test = pd.Series(y_test)

            # Decode and unpickle the model
            pickled_model = base64.b64decode(encoded_model.encode('utf-8'))
            model = pickle.loads(pickled_model)

            y_pred = model.predict(X_test)

            mse = float(mean_squared_error(y_test, y_pred))
            rmse = float(sqrt(mse))
            r2 = float(r2_score(y_test, y_pred))
            mae = float(mean_absolute_error(y_test, y_pred))

            # Log metrics
            mlflow.log_metrics({
                "mse": mse,
                "rmse": rmse,
                "r2": r2,
                "mae": mae
            })

            logger.info(f"Model evaluation completed. MSE: {mse}, RMSE: {rmse}, R2: {r2}, MAE: {mae}")

            # Store metrics in Airflow Variables for monitoring
            Variable.set("mse", mse)
            Variable.set("rmse", rmse)
            Variable.set("r2", r2)
            Variable.set("mae", mae)

        except Exception as e:
            logger.error(f"Error in model evaluation: {str(e)}")
            raise

with DAG(
    "california_housing_mlops_pipeline",
    default_args=default_args,
    description="An MLOps pipeline for California Housing prediction using MLflow",
    schedule_interval=timedelta(days=1),
) as dag:

    preprocess = PythonOperator(
        task_id="load_and_preprocess_data",
        python_callable=load_and_preprocess_data,
        provide_context=True,
    )

    train = PythonOperator(
        task_id="train_model",
        python_callable=train_model,
        provide_context=True,
    )

    evaluate = PythonOperator(
        task_id="evaluate_model",
        python_callable=evaluate_model,
        provide_context=True,
    )

    preprocess >> train >> evaluate