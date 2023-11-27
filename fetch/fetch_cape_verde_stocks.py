from libs.functions import make_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from pathlib import Path
dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

class FetchCapeVerderStocks:
    def __init__(self, website) -> None:
        self.website = website
    
    def run_crawler(self):
        driver = make_driver(self.website, True)
        WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, '//button[@value="en"]'))
        )
        driver.find_element(By.XPATH, '//button[@value="en"]').click()

        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, '(//table[@class="table table-hover"])[1]'))
        )
        table = driver.find_element(By.XPATH, '(//table[@class="table table-hover"])[1]')

        table_headers = [
            'title','date','price','percentage_change'
            ]
        table_rows = table.find_elements(By.XPATH, './tbody/tr')

        table_values = []
        for tr in table_rows[1:]:
            row_values = []
            for cell in tr.find_elements(By.XPATH, './td'):
                row_values.append(str(cell.text).strip().lower().replace(',', '').replace('%', '').replace('nc', '-'))
            table_values.append(row_values)

        df = pd.DataFrame(table_values, columns=table_headers).replace('', np.nan)
        driver.quit()
        df['country'] = 'Cape Verde'
        df['exchange'] = 'Bolsa de Valores de Cabo Verde'
        df['fetched_at_utc'] = datetime.utcnow()
        df.to_csv(f'temp/cape_verde/cape_verde_stocks_{datetime.now()}.csv', index=False)




if __name__=='__main__':
    FetchCapeVerderStocks(
        'https://bvc.cv'
        ).run_crawler()