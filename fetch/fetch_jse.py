from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless")
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')
        options.add_experimental_option("detach", True)
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')   
        remote_webdriver = os.getenv('REMOTE_CHROME')

        # if bool(os.getenv('IN_PRODUCTION')):
        if True:
            driver = webdriver.Remote(command_executor=f'localhost:4444/wd/hub', options=options)
        else:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(self.website)
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
        outdir = './temp/jse'
        if not os.path.exists(outdir):
            os.mkdir('./temp')
            os.mkdir(outdir)
        df.to_csv(f'temp/jse/jse_{datetime.now()}.csv', index=False)


if __name__=='__main__':
    FetchJSE('https://www.jse.co.za/indices').run_crawler()