import requests, json
from requests.auth import HTTPBasicAuth
from datetime import datetime

url = "https://api.browserstack.com/automate/builds.json"
session_url = "https://api.browserstack.com/automate/builds/{}/sessions.json"
auth = HTTPBasicAuth("christianpederse1", "TGp7ESBbqgU7y9SETXC2")
r = requests.get(url, auth=auth)
jout = json.loads(r.content)

for build in jout:
    for u in build:
        if build[u]["name"] == "UI Tests":
            r = build[u]

if r is not None:
    session_url = session_url.format(r["hashed_id"])

r = requests.get(session_url, auth=auth)
jout = json.loads(r.content)

for session in jout:
    for s in session:
        se = session[s]
        if se["name"] != "":
            print(se["name"])
            print datetime.strptime(se["name"], "%Y %m %d %H:%M:%S.%f")
#        for y in se:
#            print("{}: {}".format(y, se[y]))





