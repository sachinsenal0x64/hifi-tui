from fastapi import FastAPI
import uvicorn
import httpx
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


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

    return res.json()


@app.api_route("/auth", methods=["GET"])
async def get_token():
    token = await auth()
    return token


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info", reload=True)
