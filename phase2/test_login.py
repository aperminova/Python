from phase2.api import *
import pytest


class TestLogin:
    @pytest.mark.parametrize("username, password, expected", [
        ("Alisa_Perminova", "Alisa_Perminova", 200),
        ("wrong", "Alisa_Perminova", 401),
        ("Alisa_Perminova", "wrong", 401),
    ])
    def test_login(self, username, password, expected):
        assert login(username, password) == expected

    def test_create_issue(self):
         assert create_issue("Alisa") == 201

