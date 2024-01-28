from fastapi import FastAPI, HTTPException
import httpx
import uvicorn

app = FastAPI()


@app.get("/search/{path:path}")
async def proxy_to_bing(path: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{path}")

            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(
                    status_code=response.status_code, detail="API request failed"
                )
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"HTTP error: {e}")


if __name__ == "__main__":
    ser = uvicorn.run("test:app", port=5001)
