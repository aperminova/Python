from ui.driver import get_driver
from ui.pages.login_page import LoginPage
from ui.pages.issues_page import IssuesPage
from api.jira_api import Api
import pytest
from jira import JIRA
import allure
from allure_commons.types import AttachmentType


url = "http://jira.hillel.it:8080"
user = "Alisa_Perminova"
password = "Alisa_Perminova"
api = Api()


@pytest.mark.ui
class TestLoginUi:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(url)

    @pytest.mark.parametrize("user, password, expected", [
        (user, password, True),
        ("wrong", password, False),
        (user, "wrong", False),
     ])
    def test_login_ui(self, user, password, expected):

        self.login_page = LoginPage(self.driver)
        self.login_page.fill_login_field(user)
        self.login_page.fill_password_field(password)
        self.login_page.click_login_button()
        assert self.login_page.is_logged_in() == expected

    def teardown_method(self):
        self.driver.close()


@pytest.mark.ui
class TestIssuesUi:

    def setup_class(cls):
        api.create_issues("Alisa UI issue-")

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(url)
        self.login_page = LoginPage(self.driver)
        self.login_page.fill_login_field(user)
        self.login_page.fill_password_field(password)
        self.login_page.click_login_button()

    def teardown_method(self):
        self.driver.close()

    def teardown_class(cls):
        jira = JIRA(basic_auth=(user, password), server=url)
        issues = jira.search_issues("reporter=Alisa_Perminova")
        for issue in issues:
            issue.delete()

    @pytest.mark.parametrize("summary, expected", [
        ("create issue UI", True),
        ("", False),
        ("a" * 256, False),
    ])
    def test_create_issue_ui(self, summary, expected):
        self.issues_page = IssuesPage(self.driver)
        self.issues_page.start_create_issue()
        self.issues_page.fill_and_submit_issue(summary)
        assert self.issues_page.issue_created() == expected

    @pytest.mark.parametrize("query, expected", [
        ("Alisa UI", 5),
        ("Alisa UI issue-1", 1),
        ("no_such_issue?", 0),
    ])
    def test_search_issues_ui(self, query, expected):
        self.issues_page = IssuesPage(self.driver)
        assert self.issues_page.search_issue(query) == expected

    def test_update_issue_ui(self):
        self.issues_page = IssuesPage(self.driver)
        self.issues_page.search_issue("Alisa UI issue-4")
        self.issues_page.click_edit_button()
        self.issues_page.update_summary("Updated summary UI")
        self.issues_page.update_priority("Blocker")
        self.issues_page.update_assignee(user)
        self.issues_page.click_update_button()

        allure.attach(self.driver.get_screenshot_as_png(), name="Updated issue",
                      attachment_type=AttachmentType.PNG)
        assert self.issues_page.search_issue("Updated summary UI") == 1
