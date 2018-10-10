from api.jira_api import *
import pytest


auth = Login()
api = Api()
rerun = Rerun()


@pytest.mark.api
class TestLoginApi:

    @pytest.mark.parametrize("username, password, expected", [
        ("Alisa_Perminova", "Alisa_Perminova", 200),
        ("wrong", "Alisa_Perminova", 401),
        ("Alisa_Perminova", "wrong", 401),
    ])
    def test_login_api(self, username, password, expected):
        assert auth.login(username, password) == expected


@pytest.mark.api
class TestIssuesApi:

    def setup_class(cls):
        api.create_issues("Alisa_API_issue-")

    def teardown_class(cls):
        api.delete_issue()

    def test_create_issue_api(self):
        assert api.create_issue("Alisa single test issue", "Alisa_Perminova", "Medium") == 201

    def test_create_issue_empty_summary(self):
        assert api.create_issue("", "Alisa_Perminova", "Medium") == 400

    def test_create_issue_unsupported_text_length(self):
        assert api.create_issue("8" * 256, "Alisa_Perminova", "Medium") == 400

    def test_update_isssue_api(self):
        assert api.update_issue("Updated issue", "Alisa_Perminova", "Medium", issue_id_list[5]) == 204

    def test_search_5_issues(self):
        assert api.search_issue("Alisa_API") == 5

    def test_search_1_issues(self):
        assert api.search_issue("Alisa_API_issue-1") == 1

    def test_search_0_issues(self):
        assert api.search_issue("abcdefghjklmno") is 0


@pytest.mark.rerun
class TestRerun:

    def test_rerun(self):
        assert rerun.failed_passed() == 2
