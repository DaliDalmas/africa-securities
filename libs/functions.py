from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



def make_driver(website, production=False):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless")
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.92 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    options.add_experimental_option("detach", True)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')   

    if production:
        driver = webdriver.Remote(command_executor=f'http://localhost:4444/wd/hub', options=options)
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(website)

    return driver
