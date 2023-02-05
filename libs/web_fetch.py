import requests

class Fetch:
    def __init__(self, url: str, file_name: str)->None:
        self.url = url
        self.file_name = file_name

    def run(self):
        html_doc = requests.get(self.url, timeout=None).content
        
        with open(f'temp/{self.file_name}.html', 'wb') as file:
            file.write(html_doc)
