import pandas as pd
from sqlalchemy import create_engine
from libs.constants import securities_data_types, securities_floating_columns
import numpy as np

import os
from dotenv import load_dotenv
from pathlib import Path
dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)


class Load:
    def __init__(self, df_path, table_name, data_types, database_schema, db_user, db_user_pass,
                 db_host, db_port, db, floating_columns) -> None:
        self.path = df_path
        self.data = pd.read_csv(self.path)
        self.data_types = data_types
        self.table = table_name
        self.database_schema = database_schema
        self.db_user = db_user
        self.db_user_pass = db_user_pass
        self.db_host = db_host
        self.db_port = db_port
        self.db = db
        self.floating_columns = floating_columns

    def load(self) -> None:
        db_link = f'postgresql://{self.db_user}:{self.db_user_pass}@{self.db_host}:{self.db_port}/{self.db}'
        print(db_link)
        engine = create_engine(db_link)
        for col in  self.floating_columns:
            self.data[col] = self.data[col].apply(lambda val: str(val).replace(',', '') if val else np.nan)
            self.data[col] = pd.to_numeric(self.data[col])
        self.data.to_sql(self.table,
                         engine,
                         if_exists='append',
                         schema=self.database_schema,
                         dtype=self.data_types,
                         index=False)


if __name__=='__main__':
    data = Load('temp/botswana_stock_exchange.csv',
                table_name=os.getenv('SECURITIES_TABLE_NAME'),
                data_types=securities_data_types,
                database_schema=os.getenv('SECURITIES_DATABASE_SCHEMA'),
                db_user=os.getenv('SECURITIES_DB_USER'),
                db_user_pass=os.getenv('SECURITIES_DB_PASS'),
                db_host=os.getenv('SECURITIES_DB_HOST'),
                db_port=os.getenv('SECURITIES_DB_PORT'),
                db=os.getenv('SECURITIES_DB'),
                floating_columns=securities_floating_columns)
    data.load()
