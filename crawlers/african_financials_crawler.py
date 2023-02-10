from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
options = Options()
options.add_experimental_option("detach", True)


class AfricanFinancialCrawler:
    def __init__(self, website, sleep_time, country) -> None:
        self.website = website
        self.sleep_time = sleep_time
        self.country = country

    def run_crawler(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(self.website)
        time.sleep(30)
        securities_table = driver.find_element(By.XPATH, '//table[@id="af21_prices"]')
        table_heads = securities_table.find_element(By.TAG_NAME, 'thead')

        column_titles = []
        for head in table_heads.find_elements(By.TAG_NAME, 'th'):
            column_titles.append(head.text.replace('%', '').strip())

        table_body = securities_table.find_element(By.TAG_NAME, 'tbody')
        all_records = []
        for row in table_body.find_elements(By.TAG_NAME, 'tr'):
            if row.text==table_heads.text:
                continue
            security_record = []
            for cell in row.find_elements(By.TAG_NAME, 'td'):
                security_record.append(cell.text)
            all_records.append(security_record)

        securities_df = pd.DataFrame(all_records, columns=column_titles)
        securities_df['country'] = self.country
        securities_df.to_csv(f'temp/{self.country}.csv', index=False)

        driver.quit()