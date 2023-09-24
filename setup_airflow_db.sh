export PYTHONPATH=`pwd`
export AIRFLOW_HOME=`pwd`/airflow

source venv/bin/activate
airflow db init
