pyenv local 3.8.6
python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

export PYTHONPATH=`pwd`
export AIRFLOW_HOME=`pwd`/airflow

airflow info
airflow version