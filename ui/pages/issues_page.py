from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class IssuesPage(BasePage):

    create_issue_locator = (By.ID, "create_link")
    summary_locator = (By.ID, "summary")
    summary_error_locator = (By.CSS_SELECTOR, ".error")
    search_field_locator = (By.ID, "quickSearchInput")
    priority_field_locator = (By.ID, "priority-field")
    assignee_field_locator = (By.ID, "assignee-field")
    issue_list_locator = (By.CSS_SELECTOR, ".issue-list li")
    issue_updated_message_locator = (By.CSS_SELECTOR, ".aui-message.aui-message-success.success.closeable.shadowed.aui-will-close")

    create_submit_button_locator = (By.ID, "create-issue-submit")
    edit_button_locator = (By.CSS_SELECTOR, ".trigger-label")
    update_button_locator = (By.ID, "edit-issue-submit")

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
        #sleep(5)
        issues_list = self.driver.find_elements(*self.issue_list_locator)
        return len(issues_list)

    def click_edit_button(self):
        edit_btn = self.get_element(self.edit_button_locator)
        self.wait_visible(edit_btn)
        edit_btn.click()
        #sleep(5)

    def update_summary(self, summary):
        summary_field = self.get_element(self.summary_locator)
        self.wait_visible(summary_field)
        summary_field.clear()
        summary_field.send_keys(summary)

    def update_priority(self, priority):
        priority_field = self.get_element(self.priority_field_locator)
        self.wait_visible(priority_field)
        priority_field.click()
        priority_field.clear()
        priority_field.send_keys(priority)

    def update_assignee(self, assignee):
        assignee_field = self.get_element(self.assignee_field_locator)
        self.wait_visible(assignee_field)
        assignee_field.click()
        assignee_field.clear()
        assignee_field.send_keys(assignee)

    def click_update_button(self):
        update_btn = self.get_element(self.update_button_locator)
        self.wait_visible(update_btn)
        update_btn.click()
        issue_updated_message = self.get_element(self.issue_updated_message_locator)
        self.wait_invisible(issue_updated_message)
        #sleep(6)





















