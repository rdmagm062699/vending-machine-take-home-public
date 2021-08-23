import os
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def before_all(context):
    context.base_url = 'http://vending-machine-app:5000'

    browser = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.CHROME)

    context.browser = browser

    print('BROWSER STARTED')
    
    
def after_all(context):
    context.browser.close()
