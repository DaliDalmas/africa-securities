from crawlers.african_financials_crawler import AfricanFinancialCrawler

def fetch_uganda():
    crawler = AfricanFinancialCrawler('https://africanfinancials.com/uganda-securities-exchange-share-prices/', 30, 'uganda')
    crawler.run_crawler()

def fetch_botswana():
    crawler = AfricanFinancialCrawler('https://africanfinancials.com/botswana-stock-exchange-share-prices/', 30, 'botswana')
    crawler.run_crawler()

def fetch_tanzania():
    crawler = AfricanFinancialCrawler('https://africanfinancials.com/dar-es-salaam-stock-exchange-share-prices/', 30, 'tanzania')
    crawler.run_crawler()

def fetch_ghana():
    crawler = AfricanFinancialCrawler('https://africanfinancials.com/ghana-stock-exchange-share-prices/', 30, 'ghana')
    crawler.run_crawler()

fetch_uganda()
fetch_botswana()
fetch_tanzania()
fetch_ghana()