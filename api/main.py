import asyncio
import base64
import json
import os
from logging import raiseExceptions
from typing import Union
import httpx
import redis
import rich
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from fastapi.datastructures import Default
from redis import client

app = FastAPI()

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
access_token = os.getenv("TIDAL_TOKEN")
refresh_token = os.getenv("TIDAL_REFRESH")
redis_url = os.getenv("REDIS_URL")
redis_port = os.getenv("REDIS_PORT")
redis_password = os.getenv("REDIS_PASSWORD")
user_id = os.getenv("USER_ID")

client_id = "zU4XHVVkc2tDPo4t"
client_secret = "VJKhDFqJPqvsPVNBV6ukXTJmwlvbttP7wlMlrc72se4="


# with open("token.json", "r") as tok:
#     token = json.loads(tok.read())


# refresh_token = token["refresh_token"]
# access_token = token["access_token"]

r = redis.Redis(
    host=redis_url or "localhost",
    port=int(redis_port or 6379),
    password=redis_password,
    db=0,
    protocol=3,
    decode_responses=True,
)

cached_tok = r.get("access_token")


async def token_checker():
    refresh_url = f"https://api.tidal.com/v2/feed/activities/?userId={user_id}"

    headers = {"authorization": f"Bearer {cached_tok}"}

    async with httpx.AsyncClient() as client:
        res2 = await client.get(url=refresh_url, headers=headers)
        rich.print(res2.json())
        # Assuming a successful response code is 200
        if res2.status_code == 200:
            return res2.status_code


async def refresh():
    status = await token_checker()
    if status == 200:
        tidal_token = cached_tok
        return tidal_token

    elif status != 200:
        r.delete("access_token")

    if not cached_tok:
        if not r.get("access_token"):
            refresh_url = "https://auth.tidal.com/v1/oauth2/token"
            payload = {
                "client_id": client_id,
                "refresh_token": refresh_token,
                "grant_type": "refresh_token",
                "scope": "r_usr+w_usr+w_sub",
            }
            async with httpx.AsyncClient() as client:
                try:
                    res2 = await client.post(
                        url=refresh_url,
                        data=payload,
                        auth=(client_id, client_secret),
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
    return {"HIFI-API": "v1", "REPO": "https://github.com/sachinsenal0x64/Hifi-Tui"}


@app.api_route("/track/", methods=["GET"])
async def get_track(
    id: int,
    quality: str,
    country: Union[str, None] = Query(default=None, max_length=3),
):
    tokz = await refresh()
    tidal_token = tokz

    track_url = f"https://api.tidal.com/v1/tracks/{id}/playbackinfopostpaywall/v4?audioquality={quality}&playbackmode=STREAM&assetpresentation=FULL"

    info_url = f"https://api.tidal.com/v1/tracks/{id}/?countryCode=US"

    payload = {
        "authorization": f"Bearer {tidal_token}",
    }

    async with httpx.AsyncClient() as client:
        track_data = await client.get(url=track_url, headers=payload)
        info_data = await client.get(url=info_url, headers=payload)
    try:
        final_data = track_data.json()["manifest"]
        decode_manifest = base64.b64decode(final_data)
        con_json = json.loads(decode_manifest)
        audio_url = con_json.get("urls")[0]
        au_j = {"OriginalTrackUrl": audio_url}
        fetch_info = info_data.json()

        return [fetch_info, track_data.json(), au_j]

    except KeyError:
        raise HTTPException(
            status_code=404,
            detail="Quality not found. check API docs = https://github.com/sachinsenal0x64/Hifi-Tui?tab=readme-ov-file#-api-documentation",
        )


@app.api_route("/song/", methods=["GET"])
async def get_song(q: str, quality: str):
    tokz = await refresh()
    tidal_token = tokz
    search_url = f"https://api.tidal.com/v1/search/tracks?countryCode=US&query={q}"
    payload = {
        "authorization": f"Bearer {tidal_token}",
    }
    async with httpx.AsyncClient() as clinet:
        search_data = await clinet.get(url=search_url, headers=payload)
        try:
            id = search_data.json()["items"][0]["id"]

        except IndexError:
            raise HTTPException(status_code=404)

        track_url = f"https://api.tidal.com/v1/tracks/{id}/playbackinfopostpaywall/v4?audioquality={quality}&playbackmode=STREAM&assetpresentation=FULL"
        track_data = await clinet.get(url=track_url, headers=payload)

    try:
        rich.print(track_data.json())
        final_data = track_data.json()["manifest"]
        decode_manifest = base64.b64decode(final_data)
        con_json = json.loads(decode_manifest)
        audio_url = con_json.get("urls")[0]
        au_j = {"OriginalTrackUrl": audio_url}

        return [search_data.json()["items"][0], track_data.json(), au_j]

    except KeyError:
        raise HTTPException(
            status_code=404,
            detail="Quality not found. check API docs = https://github.com/sachinsenal0x64/Hifi-Tui?tab=readme-ov-file#-api-documentation",
        )


@app.api_route("/search/", methods=["GET"])
async def search_track(q: str):
    tokz = await refresh()
    tidal_token = tokz
    search_url = f"https://api.tidal.com/v1/search/tracks?countryCode=US&query={q}"
    header = {"authorization": f"Bearer {tidal_token}"}
    async with httpx.AsyncClient() as clinet:
        search_data = await clinet.get(url=search_url, headers=header)
        sed = search_data.json()["items"]
        return [sed]


@app.api_route("/album/", methods=["GET"])
async def search_album(id: int):
    tokz = await refresh()
    tidal_token = tokz
    search_url = f"https://api.tidal.com/v1/albums/{id}/?countryCode=US"
    header = {"authorization": f"Bearer {tidal_token}"}
    async with httpx.AsyncClient() as clinet:
        album_data = await clinet.get(url=search_url, headers=header)
        sed = album_data.json()
        return [sed]


@app.api_route("/cover/", methods=["GET"])
async def search_cover(id: Union[int, None] = None, q: Union[str, None] = None):
    tokz = await refresh()
    tidal_token = tokz
    try:
        if id:
            search_url = f"https://api.tidal.com/v1/tracks/{id}/?countryCode=US"
            header = {"authorization": f"Bearer {tidal_token}"}
            async with httpx.AsyncClient() as clinet:
                cover_data = await clinet.get(url=search_url, headers=header)
                tracks = cover_data.json()["album"]

                album_ids = []  # list to store album ids

                album_track_id = tracks["id"]
                album_cover = tracks["cover"].replace("-", "/")
                album_name = tracks["title"]
                album_ids.append(album_cover)
                album_ids.append(album_name)
                album_ids.append(album_track_id)

                json_data = [
                    {
                        "id": album_ids[i + 2],
                        "name": album_ids[i + 1],
                        "1280": f"https://resources.tidal.com/images/{album_ids[i]}/1280x1280.jpg",
                        "640": f"https://resources.tidal.com/images/{album_ids[i]}/640x640.jpg",
                        "80": f"https://resources.tidal.com/images/{album_ids[i]}/80x80.jpg",
                    }
                    for i in range(0, len(album_ids), 3)
                ]

                # Create a list of dictionaries with "cover" and "name" keys
                return json_data

        elif q:
            search_url = (
                f"https://api.tidal.com/v1/search/tracks?countryCode=US&query={q}"
            )
            header = {"authorization": f"Bearer {tidal_token}"}
            async with httpx.AsyncClient() as clinet:
                cover_data = await clinet.get(url=search_url, headers=header)
                tracks = cover_data.json()["items"][:10]

                album_ids = []  # list to store album ids

                for track in tracks:
                    album_track_id = track["id"]
                    print(album_track_id)
                    album_cover = track["album"]["cover"].replace("-", "/")
                    album_name = track["title"]
                    album_ids.append(album_cover)
                    album_ids.append(album_name)
                    album_ids.append(album_track_id)
                json_data = [
                    {
                        "id": album_ids[i + 2],
                        "name": album_ids[i + 1],
                        "1280": f"https://resources.tidal.com/images/{album_ids[i]}/1280x1280.jpg",
                        "640": f"https://resources.tidal.com/images/{album_ids[i]}/640x640.jpg",
                        "80": f"https://resources.tidal.com/images/{album_ids[i]}/80x80.jpg",
                    }
                    for i in range(0, len(album_ids), 3)
                ]

                # Create a list of dictionaries with "cover" and "name" keys
                return json_data

        else:
            raise HTTPException(
                status_code=404,
                detail="Cover not found. check API docs = https://github.com/sachinsenal0x64/Hifi-Tui?tab=readme-ov-file#-api-documentation",
            )

    except KeyError:
        raise HTTPException(
            status_code=404,
            detail="Cover not found. check API docs = https://github.com/sachinsenal0x64/Hifi-Tui?tab=readme-ov-file#-api-documentation",
        )


async def main():
    config = uvicorn.Config("main:app", port=5000)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
