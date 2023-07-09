from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from fetch import fetch_african_financials as faf
from load import load_african_financials as laf
from clean_up import clean_african_financials as caf

dag = DAG(
    dag_id='run_three_hourly_dag',
    catchup=False,
    description='This dag runs every three hours.',
    schedule='0 */3 * * *',
    default_args={"retries": 2},
    start_date=datetime(2023, 7, 5),
)

run_use = PythonOperator(
    task_id = 'run_uganda_securities_exchange',
    dag=dag,
    python_callable=faf.fetch_uganda
)

run_botswana_stock_exchange = PythonOperator(
    task_id = 'run_botswana_stock_exchange',
    dag=dag,
    python_callable=faf.fetch_botswana
)

run_dar_es_salaam_stock_exchage = PythonOperator(
    task_id = 'run_dar_es_salaam_stock_exchage',
    dag=dag,
    python_callable=faf.fetch_tanzania
)

run_ghana_stock_exchange = PythonOperator(
    task_id = 'run_ghana_stock_exchange',
    dag=dag,
    python_callable=faf.fetch_ghana
)

run_lusaka_securities_exchange = PythonOperator(
    task_id = 'run_lusaka_securities_exchange',
    dag=dag,
    python_callable=faf.fetch_zambia
)

run_malawi_stock_exchange = PythonOperator(
    task_id = 'run_malawi_stock_exchange',
    dag=dag,
    python_callable=faf.fetch_malawi
)

run_nairobi_securities_exchange = PythonOperator(
    task_id = 'run_nairobi_securities_exchange',
    dag=dag,
    python_callable=faf.fetch_kenya
)

run_nigerian_stock_exchange = PythonOperator(
    task_id = 'run_nigerian_stock_exchange',
    dag=dag,
    python_callable=faf.fetch_nigeria
)

run_stock_exchange_of_mauritius = PythonOperator(
    task_id = 'run_stock_exchange_of_mauritius',
    dag=dag,
    python_callable=faf.fetch_mauritius
)

run_victorua_falls_stock_exchange = PythonOperator(
    task_id = 'run_victorua_falls_stock_exchange',
    dag=dag,
    python_callable=faf.fetch_zimbabwe1
)

run_zimbabwe_stock_exchange = PythonOperator(
    task_id = 'run_zimbabwe_stock_exchange',
    dag=dag,
    python_callable=faf.fetch_zimbabwe
)

run_load_african_financials = PythonOperator(
    task_id = 'run_load_african_financials',
    dag=dag,
    python_callable=laf.LoadAfricanFinancials('/opt/airflow/temp').load_tables
)

run_clean_african_financials = PythonOperator(
    task_id = 'run_clean_african_financials',
    dag=dag,
    python_callable=caf.CleanAfricanFinancials('/opt/airflow/temp').delete_tables
)

run_load_african_financials.set_upstream(
    [
        run_zimbabwe_stock_exchange,
        run_victorua_falls_stock_exchange,
        run_stock_exchange_of_mauritius,
        run_nigerian_stock_exchange,
        run_nairobi_securities_exchange,
        run_malawi_stock_exchange,
        run_lusaka_securities_exchange,
        run_ghana_stock_exchange,
        run_dar_es_salaam_stock_exchage,
        run_botswana_stock_exchange,
        run_use
        ]
        )

run_clean_african_financials.set_upstream(run_load_african_financials)