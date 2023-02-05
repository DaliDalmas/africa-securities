import pandas as pd
from bs4 import BeautifulSoup
import re
class ScrapeUSE:
    def __init__(self, html_file_name: str):
        self.html_file_name = html_file_name

    def scrape(self):
        with open(f'temp/{self.html_file_name}.html', 'rb') as file:
            html_doc = file.read()

        soup = BeautifulSoup(html_doc, features="html.parser")
        table = soup.find('table')
        table_head = table.find('thead')

        # creating dataframe columns
        columns = []
        for head in table_head.find('tr').findAll('th'):
            columns.append(
                re.sub(
                    '[^A-Za-z0-9 ]+',
                    '',
                    head.text).strip()
                )


        # creating dataframe rows
        table_rows = table.findAll('tr')
        for row in table_rows:
            for cell in row.findAll('td'):
                cell_text = re.sub(
                    '[^A-Za-z0-9 ]+',
                    '',
                    cell.text
                ).strip().replace('\n', '')
                print(cell_text)

