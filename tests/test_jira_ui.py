from ui.driver import get_driver
from ui.pages.login_page import LoginPage
from ui.pages.system_dashboard_page import SystemDashboardPage
from api.jira_api import Api
import pytest

url = "http://jira.hillel.it:8080"
user = "Alisa_Perminova"
password = "Alisa_Perminova"
api = Api()

# class TestUiLogin:
#
#     def setup_method(self):
#         self.driver = get_driver()
#         self.driver.get(url)
#
#     @pytest.mark.parametrize("user, password, expected", [
#         (user, password, True),
#         ("wrong", password, False),
#         (user, "wrong", False),
#      ])
#     def test_login_ui_jira(self, user, password, expected):
#
#         self.login_page = LoginPage(self.driver)
#         self.login_page.fill_login_field(user)
#         self.login_page.fill_password_field(password)
#         self.login_page.click_login_button()
#         assert self.login_page.is_logged_in() == expected
#
#     def teardown_method(self):
#         self.driver.close()


class TestUiIssues:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(url)
        self.login_page = LoginPage(self.driver)
        self.login_page.fill_login_field(user)
        self.login_page.fill_password_field(password)
        self.login_page.click_login_button()



    def teardown_method(self):
        self.driver.close()



    @pytest.mark.parametrize("summary, expected", [
        ("Alisa Test UI", True),
        ("", False),
        ("a" * 256, False),
    ])
    def test_create_issue(self, summary, expected):
        self.dashboard_page = SystemDashboardPage(self.driver)
        self.dashboard_page.start_create_issue()
        self.dashboard_page.fill_and_submit_issue(summary)
        assert self.dashboard_page.issue_created() == expected







    @pytest.mark.parametrize("query, expected", [
        ("Alisa", 5),
        ("Alisa Test-1", 1),
        ("no_such_issue?", 0),
    ])
    def test_search_issues(self, query, expected):
        api.create_issues()
        self.dashboard_page = SystemDashboardPage(self.driver)
        assert self.dashboard_page.search_issue(query) == expected
        api.delete_issue()





