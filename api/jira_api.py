import requests
import json
from json_fix.json_fixtures import JsonFixtures


my_json = JsonFixtures()

jiraUrl = 'http://jira.hillel.it:8080'
headers = {'Content-Type': 'application/json'}
user = "Alisa_Perminova"
password = "Alisa_Perminova"
issue_id = []


class Login:

    def login(self, username, password):
        result = requests.get(jiraUrl, auth=(username, password))
        return result.status_code


class Api:

    j = 1

    def create_issue(self, summary, assignee, priority):
        new_issue = requests.post(jiraUrl + "/rest/api/2/issue",
                                  data=json.dumps(my_json.create_json_for_issue(summary, assignee, priority)),
                                  headers=headers, auth=(user, password))
        if new_issue.status_code != 201:
            return new_issue.status_code
        else:
            issue_id.append(new_issue.json().get("id"))
        return new_issue.status_code

    def create_issues(self):
        for i in range(5):
            self.create_issue("Alisa Test-" + str(i), "Alisa_Perminova", "High")

    def search_issue(self, summary):
        requested_issues = requests.post(jiraUrl + "/rest/api/2/search",
                                         data=json.dumps(my_json.create_json_for_search(summary)), headers=headers,
                                         auth=(user, password))
        return requested_issues.json().get('total')

    def update_issue(self, summary, assignee, priority, id):
        updated_issue = requests.put(jiraUrl + "/rest/api/2/issue/" + id,
                                     data=json.dumps(my_json.create_json_for_issue(summary, assignee, priority)),
                                     headers=headers, auth=(user, password))
        return updated_issue.status_code

    def delete_issue(self):
        for id in issue_id:
            requests.delete(jiraUrl + "/rest/api/2/issue/" + str(id), auth=(user, password))

    def rerun(self):
        if  self.j == 1:
            self.j += 1
            return 1
        else:
            return self.j
