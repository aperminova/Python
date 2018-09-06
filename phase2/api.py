import requests
import json
from phase2.json_fixtures import JsonFixtures

my_json = JsonFixtures()


jiraUrl = 'http://jira.hillel.it:8080'
headers = {'Content-Type': 'application/json'}
user = "Alisa_Perminova"
password = "Alisa_Perminova"
issue_id = []


def login(username, password):
    result = requests.get(jiraUrl, auth=(username, password))
    return result.status_code


def create_issue(summary):
    new_issue = requests.post(jiraUrl + "/rest/api/2/issue", data=json.dumps(my_json.create_json_for_issue(summary)),
                              headers=headers, auth=(user, password))
    issue_id.append(new_issue.json().get("id"))
    print(issue_id)
    return new_issue.status_code



def delete_issue():


