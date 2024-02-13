import json
import webbrowser

import requests
import rich
from requests.auth import HTTPBasicAuth


# we need this api keys for grant tidal auth
class Hifi:
    def __init__(self, client_id, scope, url, client_secret):
        self.client_id = client_id
        self.scope = scope
        self.url = url
        self.client_secret = client_secret

    @staticmethod
    def Quality(quality):
        rate = {quality: "HI_RES"}
        return rate[quality]


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


while res == True:
    res2 = requests.post(url=url2, data=data2, auth=basic)
    if res2.ok:
        access_token = res2.json()["access_token"]
        refresh_token = res2.json()["refresh_token"]
        user_id = res2.json()["user"]["userId"]
        accs = {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "userID": user_id,
            "client_ID": "zU4XHVVkc2tDPo4t",
            "client_secret": "VJKhDFqJPqvsPVNBV6ukXTJmwlvbttP7wlMlrc72se4=",
        }
        with open("token.json", "w") as file:
            json.dump(accs, file, indent=4)

        res = False

with open("token.json", "r") as readfile:
    token = json.loads(readfile.read())
    rich.print(token)
    acs_tok = token["access_token"]

url3 = f"https://api.tidal.com/v1/tracks/227809464/playbackinfopostpaywall?countryCode=en_US&audioquality={HI_RES}&playbackmode=STREAM&assetpresentation=FULL&audioMode=DOLBY_ATMOS"

header = {"authorization": f"Bearer {acs_tok}"}

res3 = requests.get(url=url3, headers=header)

rich.print(res3.json())


print("TOKEN IS VALID")
