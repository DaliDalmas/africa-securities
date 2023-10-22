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

class FetchJSE:
    def __init__(self, website) -> None:
        self.website = website
    
    def run_crawler(self):
        driver = make_driver(self.website, True)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//table[@class="table table-condensed"]'))
            )
        
        table = driver.find_element(By.XPATH, '//table[@class="table table-condensed"][1]')


        values = []
        columns = [col.text.lower() for col in table.find_elements(By.TAG_NAME, 'th')]
        for row in table.find_elements(By.TAG_NAME, 'tr'):
            values.append([str(cell.text).strip() for cell in row.find_elements(By.TAG_NAME, 'td')])
        df = pd.DataFrame(values, columns=columns).replace('', np.nan).dropna()

        for col in ['value', 'change', 'volume', 'high', 'low']:
            df[col] = df[col].apply(lambda x: x.replace(',', '').replace('%', '').strip())
            df[col] = df[col].apply(
                lambda x:
                float(x.replace('B', ''))*1000000000 if 'B' in str(x) 
                else float(x.replace('M', ''))*1000000 if 'M' in str(x) 
                else float(x.replace('K', ''))*1000 if 'K' in str(x)
                else  float(x))
        driver.quit()
        df['country'] = 'South Africa'
        df['exchange'] = 'jse'
        df['fetched_at_utc'] = datetime.utcnow()
        df.to_csv(f'temp/jse/jse_{datetime.now()}.csv', index=False)


if __name__=='__main__':
    FetchJSE('https://www.jse.co.za/indices').run_crawler()