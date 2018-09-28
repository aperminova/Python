
from selenium import webdriver

def get_driver():

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome('chromedriver.exe',
                                       chrome_options=options)

    return driver