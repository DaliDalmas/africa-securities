import pandas as pd
from os import listdir
from os.path import isfile, join
from clean_up.clean import Clean
from libs.constants import securities_data_types, securities_floating_columns

import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class CleanAfricanFinancials:
    def __init__(self, path) -> None:
        self.mypath = path

    def delete_tables(self):
        csvs = [f'{self.mypath}/{f}' for f in listdir(self.mypath) if isfile(join(self.mypath, f))]
        for csv in csvs:
            clean_obj = Clean(csv)
            clean_obj.remove()


if __name__=='__main__':
    instance = CleanAfricanFinancials('/opt/airflow/temp')
    instance.delete_tables()
