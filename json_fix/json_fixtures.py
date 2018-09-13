class JsonFixtures:

    def create_json_for_issue(self, summary, assignee, priority):
        json = {
            "fields": {
                "project":
                    {
                        "key": "AQAPYTHON"
                    },
                "summary": summary,
                "description": "Creating of an issue using project keys and issue type names using the REST API",
                "assignee": {"name": assignee},
                "priority": {"name": priority},
                "issuetype": {
                    "name": "Bug"
                }
            }
        }
        return json

    def  create_json_for_search(self, summary):
        json = {"jql": "summary~" + summary,
                "startAt": 0,
                "maxResults": 10
                }

        return json



