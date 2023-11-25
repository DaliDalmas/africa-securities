from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from fetch import fetch_african_financials as faf
from fetch.fetch_jse import FetchJSE
from fetch.fetch_rwanda_securities import FetchRandaSecurities
from fetch.fetch_algeria_stocks import FetchAlgeriaStocks
from load import load_african_financials as laf
from load import load_jse as ljse
from clean_up import clean_african_financials as caf

from load import load_rwanda_stock_exchange as lrse
from load import load_algeria_stocks as lase

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

run_victoria_falls_stock_exchange = PythonOperator(
    task_id = 'run_victoria_falls_stock_exchange',
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
    python_callable=laf.LoadAfricanFinancials('temp/af').load_tables
)

run_clean_african_financials = PythonOperator(
    task_id = 'run_clean_african_financials',
    dag=dag,
    python_callable=caf.CleanAfricanFinancials('temp/af').delete_tables
)

run_load_jse = PythonOperator(
    task_id = 'run_load_jse',
    dag=dag,
    python_callable=ljse.LoadJSE('temp/jse').load_tables
)

run_fetch_jse = PythonOperator(
    task_id = 'run_fetch_jse',
    dag=dag,
    python_callable=FetchJSE('https://www.jse.co.za/indices').run_crawler
)

run_clean_jse = PythonOperator(
    task_id = 'run_clean_jse',
    dag=dag,
    python_callable=caf.CleanAfricanFinancials('temp/jse').delete_tables
)

run_load_rse = PythonOperator(
    task_id = 'run_load_rse',
    dag=dag,
    python_callable=lrse.LoadRwandaStockExchange('temp/rse').load_tables
)

run_fetch_rse = PythonOperator(
    task_id = 'run_fetch_rse',
    dag=dag,
    python_callable=FetchRandaSecurities('https://www.african-markets.com/en/stock-markets/rse/listed-companies').run_crawler
)

run_clean_rse = PythonOperator(
    task_id = 'run_clean_rse',
    dag=dag,
    python_callable=caf.CleanAfricanFinancials('temp/rse').delete_tables
)

run_load_algeria_stock_exchange = PythonOperator(
    task_id = 'run_load_algeria_stock_exchange',
    dag=dag,
    python_callable=lase.LoadAlgeriaStockExchange('temp/algeria').load_tables
)

run_fetch_algeria_stocks = PythonOperator(
    task_id = 'run_fetch_algeria_stocks',
    dag=dag,
    python_callable=FetchAlgeriaStocks('https://www.sgbv.dz/?page=detail_creance&lang=eng').run_crawler
)

run_clean_algeria_stocks = PythonOperator(
    task_id = 'run_clean_algeria_stocks',
    dag=dag,
    python_callable=caf.CleanAfricanFinancials('temp/algeria').delete_tables
)

run_fetch_algeria_stocks.set_downstream(run_load_algeria_stock_exchange)
run_load_algeria_stock_exchange.set_downstream(run_clean_algeria_stocks)

run_load_african_financials.set_upstream(
    [
        run_zimbabwe_stock_exchange,
        run_victoria_falls_stock_exchange,
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

run_load_jse.set_upstream(run_fetch_jse)
run_clean_jse.set_upstream(run_load_jse)


run_load_rse.set_upstream(run_fetch_rse)
run_clean_rse.set_upstream(run_load_rse)

