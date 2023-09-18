from __future__ import annotations
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Input, OptionList
import rich
from rich.table import Table
import requests
from requests.auth import HTTPBasicAuth
import json
import webbrowser
import os


# we need this api keys for grant tidal auth
class Hifi:
    def __init__(self, client_id, scope, url, client_secret):
        self.client_id = client_id
        self.scope = scope
        self.url = url
        self.client_secret = client_secret

    @staticmethod
    def Quality(quality):
        if quality == "True":
            return "HI_RES"
        else:
            return None


# in here we create url for get AccessToken & RefreshToken
class Auth(Hifi):
    def __init__(self, client_id, scope, url, client_secret):
        super().__init__(client_id, scope, url, client_secret)
        data = {"client_id": client_id, "scope": scope}
        header = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G965F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36"
        }

        res = requests.post(url, data=data, headers=header)

        self.response = res

        def __str__(self):
            return str(self.response)


authrize = Auth(
    client_id="zU4XHVVkc2tDPo4t",
    scope="r_usr+w_usr+w_sub",
    url="https://auth.tidal.com/v1/oauth2/device_authorization",
    client_secret="VJKhDFqJPqvsPVNBV6ukXTJmwlvbttP7wlMlrc72se4=",
)

res = authrize.response.json()

verifyurl = res["verificationUriComplete"]
dcode = res["deviceCode"]


rich.print(verifyurl)
rich.print(dcode)

HI_RES = authrize.Quality(quality="True")

rich.print(HI_RES)

#
# with open("token.json", "r") as readfile:
#     token = json.loads(readfile.read())
#     rich.print(token)
#     acs_tok = token["access_token"]


ROWS = [
    ("lane", "swimmer", "country", "time"),
    (4, "Joseph Schooling", "Singapore", 50.39),
    (2, "Michael Phelps", "United States", 51.14),
    (5, "Chad le Clos", "South Africa", 51.14),
    (6, "László Cseh", "Hungary", 51.14),
    (3, "Li Zhuhao", "China", 51.26),
    (8, "Mehdy Metella", "France", 51.58),
    (7, "Tom Shields", "United States", 51.73),
    (1, "Aleksandr Sadovnikov", "Russia", 51.84),
    (10, "Darren Burns", "Scotland", 51.84),
]


class Tui(App):
    CSS_PATH = "tidal_tui.css"

    def compose(self) -> ComposeResult:
        yield Input(id="in")
        yield OptionList(
            id="op",
        )
        yield OptionList(
            id="opp",
        )

    @on(Input.Submitted)
    def search(self):
        check = self.query_one(Input)
        song = check.value

        with open("token.json", "r") as tok:
            token = json.loads(tok.read())
            rich.print(token)
            access_token = token["access_token"]
            refresh_token = token["refresh_token"]

            print(access_token, refresh_token)

        url3 = f"https://api.tidal.com/v1/tracks/243872266/playbackinfopostpaywall?countryCode=en_US&audioquality={HI_RES}&playbackmode=STREAM&assetpresentation=FULL"

        header = {"authorization": f"Bearer {access_token}",
                  "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G965F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36"}

        res3 = requests.get(url=url3, headers=header)


        with open("name.json", "a") as files:
            json.dumps(res3.text,indent=4)


if __name__ == "__main__":
    if not os.path.exists("token.json"):
        webbrowser.open(verifyurl)

        # Polling Until Authrize

        url2 = "https://auth.tidal.com/v1/oauth2/token"

        data2 = {
            "client_id": authrize.client_id,
            "scope": authrize.scope,
            "device_code": dcode,
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
        }

        basic = HTTPBasicAuth(authrize.client_id, authrize.client_secret)

        while True:
            res2 = requests.post(url=url2, data=data2, auth=basic)
            if res2.ok:
                access_token = res2.json()["access_token"]
                refresh_token = res2.json()["refresh_token"]
                accs = {"access_token": access_token, "refresh_token": refresh_token}
                print(res2.text)
                with open("token.json", "w") as file:
                    json.dump(accs, file)
                    break

    app = Tui()
    app.run()
