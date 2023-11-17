from fastapi import FastAPI
import uvicorn
import httpx
from dotenv import load_dotenv
import os
import asyncio

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

        access_token = res.json()["access_token"]
        expires_in = res.json()["expires_in"]
        token_type = res.json()["token_type"]
        out_res = {
            "access_token": access_token,
            "expires_in": expires_in,
            "token_type": token_type,
        }

    return out_res


@app.api_route("/auth", methods=["GET"])
async def get_token():
    token = await auth()
    return token


async def main():
    config = uvicorn.Config(
        "main:app", port=5000, log_level="info", loop="asyncio", reload=True
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
