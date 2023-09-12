import requests
from requests.auth import HTTPBasicAuth
import json
import rich
import webbrowser


class Hifi:
    def __init__(self, client_id, scope, url):
        self.client_id = client_id
        self.scope = scope
        self.url = url


class Auth(Hifi):
    def __init__(self, client_id, scope, url):
        super().__init__(client_id, scope, url)
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
)

res = authrize.response.json()

verifyurl = res["verificationUriComplete"]
dcode = res["deviceCode"]


rich.print(verifyurl)
rich.print(dcode)

webbrowser.open(verifyurl)

url2 = "https://auth.tidal.com/v1/oauth2/token"

data2 = {
    "client_id": authrize.client_id,
    "scope": authrize.scope,
    "device_code": dcode,
    "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
}

basic = HTTPBasicAuth(
    authrize.client_id, "VJKhDFqJPqvsPVNBV6ukXTJmwlvbttP7wlMlrc72se4="
)

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


with open("token.json", "r") as readfile:
    token = json.loads(readfile.read())
    rich.print(token)
    acs_tok = token["access_token"]


url3 = "https://api.tidal.com/v1/tracks/243872266/playbackinfopostpaywall?countryCode=en_US&audioquality=HI_RES&playbackmode=STREAM&assetpresentation=FULL"


header = {"authorization": f"Bearer {acs_tok}"}

res3 = requests.get(url=url3, headers=header)

print(res3.text)
