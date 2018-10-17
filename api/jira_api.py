import requests
import json
from json_fix.json_fixtures import JsonFixtures
import allure


my_json = JsonFixtures()

jiraUrl = 'http://jira.hillel.it:8080'
headers = {'Content-Type': 'application/json'}
user = "Alisa_Perminova"
password = "Alisa_Perminova"
issue_id_list = []


class Login:

    @allure.step('Login using JIRA REST API')
    def login(self, username, password):
        result = requests.get(jiraUrl, auth=(username, password))
        return result.status_code


class Api:

    @allure.step('Create 1 issue using JIRA REST API')
    def create_issue(self, summary, assignee, priority):
        new_issue = requests.post(jiraUrl + "/rest/api/2/issue",
                                  data=json.dumps(my_json.create_json_for_issue(summary, assignee, priority)),
                                  headers=headers, auth=(user, password))
        if new_issue.status_code != 201:
            return new_issue.status_code
        else:
            issue_id_list.append(new_issue.json().get("id"))
        return new_issue.status_code

    @allure.step('Create 5 issues in cycle for search')
    def create_issues(self, sample):
        for i in range(5):
            self.create_issue(sample + str(i), "Alisa_Perminova", "High")

    @allure.step('Search number of issues using JIRA REST API')
    def search_issue(self, summary):
        requested_issues = requests.post(jiraUrl + "/rest/api/2/search",
                                         data=json.dumps(my_json.create_json_for_search(summary)), headers=headers,
                                         auth=(user, password))
        return requested_issues.json().get('total')

    @allure.step('Update issue using JIRA REST API')
    def update_issue(self, summary, assignee, priority, issue_id):
        updated_issue = requests.put(jiraUrl + "/rest/api/2/issue/" + issue_id,
                                     data=json.dumps(my_json.create_json_for_issue(summary, assignee, priority)),
                                     headers=headers, auth=(user, password))
        return updated_issue.status_code

    @allure.step('Delete issue by ID using JIRA REST API')
    def delete_issue(self, issue_id):
        deleted_issue = requests.delete(jiraUrl + "/rest/api/2/issue/" + issue_id, auth=(user, password))
        return deleted_issue.status_code

    @allure.step('Delete issues using JIRA REST API')
    def clean_up(self):
        for issue_id in issue_id_list:
            requests.delete(jiraUrl + "/rest/api/2/issue/" + str(issue_id), auth=(user, password))


class Rerun:

    j = 1

    @allure.step("To check rerun of tests. It always fails first time and passes second time")
    def failed_passed(self):
        if self.j == 1:
            self.j += 1
            return 1
        else:
            return self.j
