from libs.web_fetch import Fetch
from scrape.scrape_uganda_securities import ScrapeUSE

def fetch_use():
    url = 'https://www.use.or.ug/content/market-snapshot'
    use = Fetch(url, 'use')
    use.run()
fetch_use()
def scrape_use():
    scrape_use = ScrapeUSE('use')
    scrape_use.scrape()
scrape_use()