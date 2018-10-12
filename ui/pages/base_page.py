from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import allure


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step('Receive element by selector')
    def get_element(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Wait until element appears on the page')
    def wait_visible(self, element):
        return self.wait.until(EC.visibility_of(element))

    @allure.step('Wait until element disappears from the page')
    def wait_invisible(self, element):
        return self.wait.until(EC.invisibility_of_element(element))
