from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class SystemDashboardPage(BasePage):

    create_issue_locator = (By.ID, "create_link")
    summary_locator = (By.ID, "summary")
    create_submit_button_locator = (By.ID, "create-issue-submit")
    summary_error_locator = (By.CSS_SELECTOR, ".error")
    search_field_locator = (By.ID, "quickSearchInput")
    issue_list_locator = (By.CSS_SELECTOR, ".issue-list li")


    def start_create_issue(self):
        create_issue_btn = self.get_element(self.create_issue_locator)
        self.wait_visible(create_issue_btn)
        create_issue_btn.click()

    def fill_and_submit_issue(self, summary):
        summary_field = self.get_element(self.summary_locator)
        self.wait_visible(summary_field)
        summary_field.clear()
        summary_field.send_keys(summary)
        submit_issue_btn = self.get_element(self.create_submit_button_locator)
        self.wait_visible(submit_issue_btn)
        submit_issue_btn.click()
        sleep(5)

    def issue_created(self):
        if len(self.driver.find_elements(*self.summary_error_locator)) > 0:
            return False
        else:

            return True


    def search_issue(self, query):
        search_field = self.get_element(self.search_field_locator)
        self.wait_visible(search_field)
        search_field.clear()
        search_field.send_keys(query)
        search_field.submit()
        sleep(5)
        issues_list = self.driver.find_elements(*self.issue_list_locator)
        return len(issues_list)

















