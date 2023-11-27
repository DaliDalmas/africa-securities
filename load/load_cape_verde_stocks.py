from os import listdir
from os.path import isfile, join
from load.load import Load
from libs.constants import cape_verde_stocks_data_types, cape_verde_stocks_floating_columns

import os
from dotenv import load_dotenv


class LoadCapeVerdeStocks:
    def __init__(self, path) -> None:
        self.mypath = path
    
    def load_tables(self):
        csvs = [f'{self.mypath}/{f}' for f in listdir(self.mypath) if isfile(join(self.mypath, f))]
        for csv in csvs:
            data = Load(csv,
                        table_name=os.getenv('CAPE_VERDE_STOCK_TABLE'),
                        data_types=cape_verde_stocks_data_types,
                        database_schema=os.getenv('SECURITIES_DATABASE_SCHEMA'),
                        db_user=os.getenv('SECURITIES_DB_USER'),
                        db_user_pass=os.getenv('SECURITIES_DB_PASS'),
                        db_host=os.getenv('SECURITIES_DB_HOST'),
                        db_port=os.getenv('SECURITIES_DB_PORT'),
                        db=os.getenv('SECURITIES_DB'),
                        floating_columns=cape_verde_stocks_floating_columns)
            data.load()

if __name__=='__main__':
    instance = LoadCapeVerdeStocks('temp/cape_verde')
    instance.load_tables()