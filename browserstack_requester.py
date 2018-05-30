import json
import requests

from BSSession import BSSession
from Utils import init_data_object
from requests.auth import HTTPBasicAuth

from BSBuild import BSBuild

class BrowserStack(object):
    _builds_url = "https://api.browserstack.com/automate/builds.json"
    _sessions_X_url = "https://api.browserstack.com/automate/builds/{}/sessions.json"
    _auth = HTTPBasicAuth("christianpederse1", "TGp7ESBbqgU7y9SETXC2")

    def _get_json(self, url):
        _r = requests.get(url, auth=self._auth)
        return json.loads(_r.content)

    def get_builds(self):
        jr = self._get_json(self._builds_url)
        for build in jr:
            for key in build:
                b = build[key]
                yield BSBuild(b["name"], b["status"], b["duration"], b["hashed_id"])

    def get_sessions(self):
        url = ""
        for build in self.get_builds():
            if build.name == "UI Tests":
                url = self._sessions_X_url.format(build.hashed_id)
        jr = self._get_json(url)
        for sessions in jr:
            for key in sessions:
                bss = BSSession()
                init_data_object(bss, sessions[key])
                yield bss

    # if _r is not None:
    #     _sessions_X_url = _sessions_X_url.format(_r["hashed_id"])
    #
    # _r = requests.get(_sessions_X_url, auth=_auth)
    # _jout = json.loads(_r.content)
    #
    # sessions = []
    #
    # for session in _jout:
    #     for s in session:
    #         se = session[s]
    #         if se["name"] != "":
    #             se["date"] = datetime.strptime(se["name"], "%Y %m %d %H:%M:%S.%f")
    #             sessions.append(se)
    # #        for y in se:
    # #            print("{}: {}".format(y, se[y]))
    #
    # sessions = sorted(sessions, key=lambda x: x["date"])
    # for x in sessions:
    #     print(x)

bs = BrowserStack()

for x in bs.get_sessions():
    print(x.hashed_id)
