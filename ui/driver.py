
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    #driver = webdriver.Chrome('C:\\Users\\aperminova\\PycharmProjects\\Python\\ui\\chromedriver.exe',
    #                          chrome_options=options)
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    return driver
