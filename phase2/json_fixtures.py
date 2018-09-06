class JsonFixtures:

    def create_json_for_issue(self, summary):
        json = {
            "fields": {
                "project":
                    {
                        "key": "AQAPYTHON"
                    },
                "summary": summary,
                "description": "Creating of an issue using project keys and issue type names using the REST API",
                "issuetype": {
                    "name": "Bug"
                }
            }
        }
        return json
