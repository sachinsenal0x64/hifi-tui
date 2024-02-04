import asyncio
          "refresh_token": refresh_token,
          "grant_type": "refresh_token",
          "scope": "r_usr+w_usr+w_sub",
      }
      async with httpx.AsyncClient() as client:
        try:
          res2 = await client.post(
              url=refresh_url,
              data=payload,
              auth=Basic(client_id, client_secret),
          )
          # Assuming a successful response code is 200
          if res2.status_code == 200:
            print_token = res2.json()
            tida_token = print_token.get("access_token")
            r.set("access_token", tida_token)
            tidal_token = tida_token
            return tidal_token
          else:
            return {"error": f"Failed to refresh token: {res2.status_code}"}

        except httpx.HTTPError as e:
          return {"error": f"HTTP error occurred: {str(e)}"}
        except Exception as e:
          return {"error": f"An error occurred: {str(e)}"}


async def auth():
  cids = client_id
  csec = client_secret

  url = "https://auth.tidal.com/v1/oauth2/token"

  payload = {
      "grant_type": "client_credentials",
      "client_id": cids,
      "client_secret": csec,
  }
  async with httpx.AsyncClient() as client:
    res = await client.post(url=url, data=payload)

    access_token = res.json()["access_token"]
    expires_in = res.json()["expires_in"]
    token_type = res.json()["token_type"]
    out_res = {
        "access_token": access_token,
        "expires_in": expires_in,
        "token_type": token_type,
    }

  return out_res


@app.api_route("/", methods=["GET"])
async def index():
  return {
      "HIFI-API": "v1",
      "REPO": "https://github.com/sachinsenal0x64/Hifi-Tui"
  }

@app.api_route("/track/", methods=["GET"])
async def get_track(
    id: int,
    quality: str,
    country: Annotated[str | None, Query(max_length=3)] = None,
):
  tokz = await refresh()
