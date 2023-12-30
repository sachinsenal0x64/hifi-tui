from fastapi import FastAPI, Query, HTTPException
      album_name = tracks["title"]
      album_ids.append(album_cover)
      album_ids.append(album_name)
      album_ids.append(album_track_id)

      json_data = [{
          "id":
          album_ids[i + 2],
          "name":
          album_ids[i + 1],
          "cover1280":
          f"https://resources.tidal.com/images/{album_ids[i]}/1280x1280.jpg",
          "cover640":
          f"https://resources.tidal.com/images/{album_ids[i]}/640x640.jpg",
          "cover80":
          f"https://resources.tidal.com/images/{album_ids[i]}/80x80.jpg",
      } for i in range(0, len(album_ids), 3)]

      # Create a list of dictionaries with "cover" and "name" keys
      return json_data

  else:
    search_url = f"https://api.tidal.com/v1/search/tracks?countryCode=US&query={q}"
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
      json_data = [{
          "id":
          album_ids[i + 2],
          "name":
          album_ids[i + 1],
          "cover1280":
          f"https://resources.tidal.com/images/{album_ids[i]}/1280x1280.jpg",
          "cover640":
          f"https://resources.tidal.com/images/{album_ids[i]}/640x640.jpg",
          "cover80":
          f"https://resources.tidal.com/images/{album_ids[i]}/80x80.jpg",
      } for i in range(0, len(album_ids), 3)]

      # Create a list of dictionaries with "cover" and "name" keys
      return json_data


async def main():
  config = uvicorn.Config("main:app", port=5000)
  server = uvicorn.Server(config)
  await server.serve()


if __name__ == "__main__":
  asyncio.run(main())
