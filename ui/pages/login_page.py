from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from time import sleep
import allure


class LoginPage(BasePage):

    username_locator = (By.ID, "login-form-username")
    password_locator = (By.ID, "login-form-password")
    login_button_locator = (By.ID, "login")
    intro_locator = (By.CSS_SELECTOR, ".intro")
    error_login_locator = (By.CSS_SELECTOR, ".aui-message.error")

    @allure.step('Fill login field')
    def fill_login_field(self, user):
        username_field = self.get_element(self.username_locator)
        self.wait_visible(username_field)
        username_field.clear()
        username_field.send_keys(user)

    @allure.step('Fill password field')
    def fill_password_field(self, password):
        password_field = self.get_element(self.password_locator)
        self.wait_visible(password_field)
        password_field.clear()
        password_field.send_keys(password)

    @allure.step('Click "Login" button')
    def click_login_button(self):
        login_btn = self.get_element(self.login_button_locator)
        self.wait_visible(login_btn)
        login_btn.click()
        sleep(3)

    @allure.step('Check that user successfully logged in')
    def is_logged_in(self):
        if len(self.driver.find_elements(*self.error_login_locator)) > 0:
            return False
        intro_element = self.get_element(self.intro_locator)
        self.wait_visible(intro_element)
        return "secure" in self.driver.current_url
