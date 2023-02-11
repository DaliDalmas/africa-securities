from crawlers.african_financials_crawler import AfricanFinancialCrawler

def fetch_uganda():
    crawler = AfricanFinancialCrawler('https://africanfinancials.com/uganda-securities-exchange-share-prices/', 30, 'uganda', 'uganda_securities_exchange')
    crawler.run_crawler()

def fetch_botswana():
    crawler = AfricanFinancialCrawler('https://africanfinancials.com/botswana-stock-exchange-share-prices/', 30, 'botswana', 'botswana_stock_exchange')
    crawler.run_crawler()

def fetch_tanzania():
    crawler = AfricanFinancialCrawler('https://africanfinancials.com/dar-es-salaam-stock-exchange-share-prices/', 30, 'tanzania', 'dar_es_salaam_stock_exchage')
    crawler.run_crawler()

def fetch_ghana():
    crawler = AfricanFinancialCrawler('https://africanfinancials.com/ghana-stock-exchange-share-prices/', 30, 'ghana', 'ghana_stock_exchange')
    crawler.run_crawler()

def fetch_zambia():
    crawler = AfricanFinancialCrawler('https://africanfinancials.com/lusaka-securities-exchange-share-prices/', 30, 'zambia', 'lusaka_securities_exchange')
    crawler.run_crawler()

def fetch_malawi():
    crawler = AfricanFinancialCrawler('https://africanfinancials.com/malawi-stock-exchange-share-prices/', 30, 'malawi', 'malawi_stock_exchange')
    crawler.run_crawler()

def fetch_kenya():
    crawler = AfricanFinancialCrawler('https://africanfinancials.com/nairobi-securities-exchange-kenya-share-prices/', 30, 'kenya', 'nairobi_securities_exchange')
    crawler.run_crawler()

def fetch_nigeria():
    crawler = AfricanFinancialCrawler('https://africanfinancials.com/nigerian-stock-exchange-share-prices/', 30, 'nigeria', 'nigerian_stock_exchange')
    crawler.run_crawler()

def fetch_mauritius():
    crawler = AfricanFinancialCrawler('https://africanfinancials.com/stock-exchange-of-mauritius-sem-share-prices/', 30, 'mauritius', 'stock_exchange_of_mauritius')
    crawler.run_crawler()

def fetch_zimbabwe1():
    crawler = AfricanFinancialCrawler('https://africanfinancials.com/victoria-falls-stock-exchange-share-prices/', 30, 'zimbabwe', 'victorua_falls_stock_exchange')
    crawler.run_crawler()

def fetch_zimbabwe():
    crawler = AfricanFinancialCrawler('https://africanfinancials.com/zimbabwe-stock-exchange-share-prices/', 30, 'zimbabwe', 'zimbabwe_stock_exchange')
    crawler.run_crawler()

fetch_uganda()
fetch_botswana()
fetch_tanzania()
fetch_ghana()
fetch_zambia()
fetch_malawi()
fetch_mauritius()
fetch_zimbabwe1()
fetch_zimbabwe()