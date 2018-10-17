from api.jira_api import *
import pytest
import allure


auth = Login()
api = Api()
rerun = Rerun()


@pytest.mark.api
class TestLoginApi:

    @allure.title('Login API test')
    @pytest.mark.parametrize("username, password, expected", [
        ("Alisa_Perminova", "Alisa_Perminova", 200),
        ("wrong", "Alisa_Perminova", 401),
        ("Alisa_Perminova", "wrong", 401),
    ])
    def test_login_api(self, username, password, expected):
        assert auth.login(username, password) == expected


@pytest.mark.usefixtures("prepare_issues_api")
@pytest.mark.api
class TestIssuesApi:

    @allure.title('Create issue with correct data')
    def test_create_issue_api(self):
        assert api.create_issue("Alisa single test issue", "Alisa_Perminova", "Medium") == 201

    @allure.title('Create issue with empty summary')
    def test_create_issue_empty_summary(self):
        assert api.create_issue("", "Alisa_Perminova", "Medium") == 400

    @allure.title('Create issue with unsupported text length summary')
    def test_create_issue_unsupported_text_length(self):
        assert api.create_issue("8" * 256, "Alisa_Perminova", "Medium") == 400

    @allure.title('Update issue API')
    def test_update_isssue_api(self):
        assert api.update_issue("Updated issue", "Alisa_Perminova", "Medium", issue_id_list[5]) == 204

    @allure.title('Search 5 issues API')
    def test_search_5_issues(self):
        assert api.search_issue("Alisa_API") == 5

    @allure.title('Search 1 issue API')
    def test_search_1_issues(self):
        assert api.search_issue("Alisa_API_issue-1") == 1

    @allure.title('Search issue with non-exist summary API')
    def test_search_0_issues(self):
        assert api.search_issue("abcdefghjklmno") is 0

    @allure.title('Delete issue API')
    def test_delete_issue(self):
        assert api.delete_issue(issue_id_list[5]) == 204


@pytest.mark.rerun
class TestRerun:

    @allure.title('Test to check rerun option')
    def test_rerun(self):
        assert rerun.failed_passed() == 2
