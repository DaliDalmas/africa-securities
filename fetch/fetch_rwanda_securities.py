from libs.functions import make_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from pathlib import Path
dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

class FetchRandaSecurities:
    def __init__(self, website) -> None:
        self.website = website
    
    def run_crawler(self):
        driver = make_driver(self.website, True)
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, '//table[@class="tabtable-rs_01k0jris  dataTable"]'))
        )
        table = driver.find_element(By.XPATH, '//table[@class="tabtable-rs_01k0jris  dataTable"]')
        table_headers = [
            str(head.text).strip().lower() for head in table.find_elements(By.XPATH, './thead/tr/td')
            ]
        table_rows = table.find_elements(By.XPATH, './tbody/tr')

        table_values = []
        for tr in table_rows:
            row_values = []
            for cell in tr.find_elements(By.XPATH, './td'):
                row_values.append(str(cell.text).strip().lower().replace(',', '').replace('%', ''))
            table_values.append(row_values)
        df = pd.DataFrame(table_values, columns=table_headers).replace('', np.nan).dropna()
        driver.quit()
        df['country'] = 'Rwanda'
        df['exchange'] = 'rse'
        df['fetched_at_utc'] = datetime.utcnow()
        df.to_csv(f'temp/rse/rse_{datetime.now()}.csv', index=False)




if __name__=='__main__':
    FetchRandaSecurities(
        'https://www.african-markets.com/en/stock-markets/rse/listed-companies'
        ).run_crawler()