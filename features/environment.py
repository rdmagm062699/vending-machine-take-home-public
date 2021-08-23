from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def before_all(context):
    context.base_url = 'http://vending-machine-app:5000'

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(chrome_options=options)
    
    context.browser = browser

    print('BROWSER STARTED')
    
    
def after_all(context):
    context.browser.close()
