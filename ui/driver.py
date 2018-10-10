
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure


@allure.step('Get driver')
def get_driver():

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    return driver
