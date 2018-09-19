from api.jira_api import *
import pytest


auth = Login()
api = Api()



class TestLogin:

    @pytest.mark.parametrize("username, password, expected", [
        ("Alisa_Perminova", "Alisa_Perminova", 200),
        ("wrong", "Alisa_Perminova", 401),
        ("Alisa_Perminova", "wrong", 401),
    ])
    def test_login(self, username, password, expected):
        assert auth.login(username, password) == expected


class TestIssues:


    def setup_class(cls):
        api.create_issues()

    def teardown_class(cls):
        api.delete_issue()

    def test_create_issue(self):
        assert api.create_issue("Alisa single test issue", "Alisa_Perminova", "Medium") == 201

    def test_create_issue_empty_summary(self):
        assert api.create_issue("", "Alisa_Perminova", "Medium") == 400

    def test_create_issue_unsupported_text_length(self):
        assert api.create_issue("8" * 256, "Alisa_Perminova", "Medium") == 400


    def test_update_isssue(self):
        assert api.update_issue("Updated issue", "Alisa_Perminova", "Medium", issue_id[5]) == 204


    def test_search_5_issues(self):
        assert api.search_issue("Alisa") == 5

    def test_search_1_issues(self):
        assert api.search_issue("Test-1") == 1

    def test_search_0_issues(self):
        assert api.search_issue("abcdefghjklmno") is 0

    def test_rerun(self):
        assert api.rerun() == 2
