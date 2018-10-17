from ui.pages.login_page import LoginPage
from ui.pages.issues_page import IssuesPage
from api.jira_api import Api
import pytest
import allure
from allure_commons.types import AttachmentType


url = "http://jira.hillel.it:8080"
user = "Alisa_Perminova"
password = "Alisa_Perminova"
api = Api()


@pytest.mark.ui
class TestLoginUi:

    @allure.title('Login UI test')
    @pytest.mark.parametrize("user, password, expected", [
        (user, password, True),
        ("wrong", password, False),
        (user, "wrong", False),
     ])
    def test_login_ui(self, user, password, expected, get_driver, get_url, get_login_page):
        self.login_page.login_procedure(user, password)
        assert self.login_page.is_logged_in() == expected


@pytest.mark.usefixtures("prepare_issues_ui", "get_driver", "get_url")
@pytest.mark.ui
class TestIssuesUi:

    @allure.title('Create issue UI test')
    @pytest.mark.parametrize("summary, expected", [
        ("create issue UI", True),
        ("", False),
        ("a" * 256, False),
    ])
    def test_create_issue_ui(self, summary, expected):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_procedure(user, password)
        self.issues_page = IssuesPage(self.driver)
        self.issues_page.start_create_issue()
        self.issues_page.fill_and_submit_issue(summary)
        assert self.issues_page.issue_created() == expected

    @allure.title('Search issue UI test')
    @pytest.mark.parametrize("query, expected", [
        ("Alisa UI", 5),
        ("Alisa UI issue-1", 1),
        ("no_such_issue?", 0),
    ])
    def test_search_issues_ui(self, query, expected):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_procedure(user, password)
        self.issues_page = IssuesPage(self.driver)
        assert self.issues_page.search_issue(query) == expected

    @allure.title('Update issue UI test')
    def test_update_issue_ui(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_procedure(user, password)
        self.issues_page = IssuesPage(self.driver)
        self.issues_page.search_issue("Alisa UI issue-4")
        self.issues_page.click_edit_button()
        self.issues_page.update_summary("Updated by Alisa")
        self.issues_page.update_priority("Blocker")
        self.issues_page.update_assignee(user)
        self.issues_page.click_update_button()

        allure.attach(self.driver.get_screenshot_as_png(), name="Updated issue",
                      attachment_type=AttachmentType.PNG)
        assert self.issues_page.search_issue("Updated by Alisa") == 1
