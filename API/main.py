from fastapi import FastAPI, Query
import uvicorn
import httpx
from dotenv import load_dotenv
import os
import asyncio
from typing import Annotated
import base64
import json

app = FastAPI()

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
tidal_token = os.getenv("TIDAL_TOKEN")


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


async def track():
    auths = await auth()
    access_token = auths.get("access_token")
    return access_token


@app.api_route("/", methods=["GET"])
async def index():
    return {"HIFI-API": "v1", "REPO": "https://github.com/sachinsenal0x64/Hifi-Tui"}


@app.api_route("/track/", methods=["GET"])
async def get_track(
    id: int,
    quality: str,
    country: Annotated[str | None, Query(max_length=3)] = None,
):
    token = await track()
    track_url = f"https://api.tidal.com/v1/tracks/{id}/playbackinfopostpaywall/v4?audioquality={quality}&playbackmode=STREAM&assetpresentation=FULL"

    payload = {
        "authorization": f"Bearer {tidal_token}",
    }

    print(token)
    async with httpx.AsyncClient() as client:
        track_data = await client.get(url=track_url, headers=payload)

        final_data = track_data.json()["manifest"]
        decode_manifest = base64.b64decode(final_data)
        con_json = json.loads(decode_manifest)
        audio_url = con_json.get("urls")[0]

    return track_data.json(), {"originalTrack": audio_url}


async def main():
    config = uvicorn.Config("main:app", port=5000, log_level="trace", reload=True)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
