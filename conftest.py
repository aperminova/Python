import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure
from ui.pages.login_page import LoginPage
from api.jira_api import *
from jira import JIRA

url = "http://jira.hillel.it:8080"


@pytest.mark.early
@pytest.fixture(scope='function')
def get_driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="function")
def get_url(request):
    driver = request.cls.driver
    driver.get(url)


@pytest.fixture(scope="function")
def get_login_page(request):
    request.cls.login_page = LoginPage(request.cls.driver)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if 'get_driver' in item.fixturenames:
        driver = item.instance.driver
        if rep.when == "call" and rep.failed or rep.skipped:
            try:
                allure.attach(driver.get_screenshot_as_png(), name=item.name,
                              attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(e)


@pytest.fixture(scope="class")
def prepare_issues_api():
    api = Api()
    api.create_issues("Alisa_API_issue-")
    yield
    api.clean_up()


@pytest.fixture(scope="class")
def prepare_issues_ui():
    api = Api()
    api.create_issues("Alisa UI issue-")
    yield
    jira = JIRA(basic_auth=(user, password), server=url)
    issues = jira.search_issues("reporter=Alisa_Perminova")
    for issue in issues:
        issue.delete()
