<div align="center">
 
 ![hifi-tui](https://sachinsenal0x64.github.io/picx-images-hosting/test1.1ejfncjvbvuo.webp)
 
</div>

<h1 align="center"> HIFI TUI </h1>

<h4 align="center"> Privacy Focused Cross Platform Tidal Reverse Proxy / Tui + Batteries Included . </h4>

<div align="center">
        
[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](https://opensource.org/licenses/MIT) [![FASTAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com) [![Python](https://img.shields.io/badge/-Python-FCC624?style=style=flat-square&logo=Python)](https://www.python.org) [![PkgGoDev](https://pkg.go.dev/badge/github.com/rivo/tview)](https://pkg.go.dev/github.com/rivo/tview)


    
</div>

<br><br>

# 💕 Community

> 🍻 Join the community:  <a href="https://discord.gg/EbfftZ5Dd4">Discord</a>
> [![](https://cdn.statically.io/gh/sachinsenal0x64/picx-images-hosting@master/discord.72y8nlaw5mdc.webp)](https://discord.gg/EbfftZ5Dd4)
 
<br>


# 📌 F.A.Q

> We DO NOT encourage piracy and made for purely educational purposes / personal use / just for listen not for downloading.

> I'm currently paying for a Tidal HiFi Plus subscription.

> We Dont have any GUI Application for android / ios / windows / mac / linux  contributors are welcome.

> You can access our rest api for free if you want to self-host then need tidal subscription.

> TUI is plug & play also you can add your own tidal account but by default it has our API so you can listen tidal music for free.

> TL;DR  HIFI API Can Get Any Quality & Codec Which Tidal Offer / Some Qualities & Codecs Need Special Driver / Song / Hardware to get maximum output i always recommend to use `HI_RES` or `LOSSLESS` both are in flac.

> [MQA-CHECKER](https://github.com/purpl3F0x/MQA_identifier)

> Low (96 kbps) - 3 MB | Low (320 kbps) - 8 MB | High (FLAC, 16-bit, 44.1 kHz) - 30 MB | Max (MQA) - 26 MB | Max (MQA) - 26  | Max (HiRes FLAC, up to 24-bit, 192 kHz) - 30 MB to 140 MB

> Currently We don't have any GUI Application for android / ios / windows / mac / linux  contributors are welcome.

 
<br>

# ❓ WHY ?

I love cli tools as well as music, so why not to have a tidal music client for the terminal? Unfortunately, I haven't found any terminal client yet, and that's why it's all about :)


<br>

> Tidal Current Situation.

![Doge](https://sachinsenal0x64.github.io/picx-images-hosting/658aud.5f9r4ktllf8.webp)

<br>

<table>
<tr>
<td>
 
# 🚀 Features

- 🍟 TIDAL PREMIUM (HIFI-PLUS) YOU CAN LISTEN FOR FREE USING OUR  [API](https://tidal.401658.xyz) & TUI PLAYER
  
- 📀 AUDIO QUALITY / CODEC  : SONY_360RA | DOLBY ATMOS | MQA 96K  | HI RES FLAC | HI RES LOSSLESS | FLAC LOSSLESS | HIGH | LOW | Up to 24-bit, 192 kHz

- ⌨ VIM LIKE KEY BINDINGS

- 🎧 TIDAL-HIFI | PODCAST PLAYER IN TUI  (⭕ in progress)
  
- 👤 TIDAL ACCOUNTS MANAGEMENT 

- 📚 PLAYLISTS | RECENT PLAYBACK | LIBARAY MANAGEMENT | LYRICS & COVER ART (⭕ in progress)

- 📡 BEAUTIFUL REST API (ACT AS REVERSE PROXY INSTANCE)
  
- ⛓️‍💥 BYPASS GEO RESTRICTED CONTENT
  
- ⚖️ LAYER 7 LOAD BALANCER (ACT AS API GATEWAY | Purely Python & GO Implementations)

- ⚡️ POWERFUL ASYNC | CONCURRENCY SUPPORT

- 📑 DOCS SUPPORT ( SWAGGER UI ) | API PLAYGROUND (/tdoc and /pdoc)
 
- 🕹️ REMOTE (Highly Controllable Remotely Over the Network + Independently, Such an as Play | Pause | Seek | Volume | Next | Previous | Loops (Repeat | Infinity))
  
</table>
</tr>
</td>


<br>


# <img src="https://sachinsenal0x64.github.io/picx-images-hosting/svgviewer-output(1).4gs81c9ecqkg.svg" alt="" height="40px" width="40px"> TIDAL REVERSE API / STATUS

> [!NOTE]  
> TUI based on this api and it free & opensource.

> https://tidal.401658.xyz

> https://status.401658.xyz


<br>

# 🔋 BATTERIES 

- [host-hifi-restapi-on-vercel](https://github.com/sachinsenal0x64/host-hifi-restapi-on-vercel)
- [host-hifi-restapi-on-heroku](https://github.com/sachinsenal0x64/host-hifi-restapi-on-heroku)
- [tidal_auth](https://github.com/sachinsenal0x64/hifi-tui/tree/main/tidal_auth)
- [apigateway](https://github.com/sachinsenal0x64/hifi-tui/tree/main/apigateway)

<br>



# 📄 Documentation

- https://hifitui.401658.xyz
- https://hifitui.pages.dev (Backup Url)

<br>

# 💨 Quick Start

<br>

## 🏠 INSTALLATION (TUI)

> [!NOTE]
> Tui player based on reverse [api](https://github.com/sachinsenal0x64/Hifi-Tui?tab=readme-ov-file#-tidal-reverse-api--status) so its totally free (you can listen without any premium subscription) and easy to install via package manager 


(⭕ WIP)

<br>

## ⌨ KEY BINDINGS (TUI)

(⭕ WIP)

<br>

## 🐳 Docker Hub

```bash
# Clone the Repo
https://github.com/sachinsenal0x64/hifi-tui

# Rename .env-example
cd hifi-tui/api
mv .env-example .env

# Run the Docker contaer
docker pull sachinsenal/hifi-proxy
docker run --env-file .env -p 8000:8000 hifi-tui
```

<br>

## 🏠 API SELF HOSTING

> [!NOTE]
> This Required [Tidal](https://tidal.com) subscription / [Redis](https://github.com/redis/redis) & Fill the [.env](https://github.com/sachinsenal0x64/Hifi-Tui/blob/main/api/env-example) file. / Grab Tokens and Ids Using
[tidal_auth.py](https://github.com/sachinsenal0x64/hifi-tui/tree/main/tidal_auth)

> [!TIP]
> You can access reverse [api](https://github.com/sachinsenal0x64/Hifi-Tui?tab=readme-ov-file#-tidal-reverse-api--status) for free.

<br>

### 🐳 Docker Hub

```bash
# Clone the Repo
https://github.com/sachinsenal0x64/hifi-tui

# Rename .env-example
cd hifi-tui/api
mv .env-example .env

# Run the Docker contaer
docker pull sachinsenal/hifi-proxy
docker run --env-file .env -p 8000:8000 hifi-tui

```
<br>

### 🐳 Docker Compose

```bash
# Clone the Repo
https://github.com/sachinsenal0x64/host-hifi-restapi-on-vercel

# Rename .env-example
cd host-hifi-restapi-on-vercel
mv .env-example .env

# Run the Docker contaer
docker-compose up
```
<br>

### 🐳 Docker File

```bash
# Clone the Repo
https://github.com/sachinsenal0x64/host-hifi-restapi-on-vercel

# Rename .env-example
cd host-hifi-restapi-on-vercel
mv .env-example .env

# Build the Docker image
docker build -t host-hifi-restapi-on-vercel .

# Run the Docker contaer
docker run --env-file .env -p 8000:8000 host-hifi-restapi-on-vercel

```

<br>

```env

CLIENT_ID= 
CLIENT_SECRET=
TIDAL_TOKEN= 
TIDAL_REFRESH=
REDIS_URL=
REDIS_PORT=
REDIS_PASSWORD=
USER_ID= 

```

```console
git clone https://github.com/sachinsenal0x64/hifi-tui
cd hifi-tui
cd api
mv env-example .env
pip install "fastapi[all]"
pip install -r requirements.txt
python main.py

```
![fastapi](https://sachinsenal0x64.github.io/picx-images-hosting/300191675-4330ea31-3f15-45b0-962c-ca5a85041f02.5tz3jj54f2ps.webp)


<br>

## 📡 API DOCUMENTATION

------------------------------------------------------------------------------------------
### Demo

<details>

<summary><code>Here</code></summary>

  <br>
  
 > https://youtu.be/TfIWc5sQ2M0


</details>


------------------------------------------------------------------------------------------

<details>

 <summary><code>GET</code>   <code><b>/track/</b></code> </summary>

## Request


<br>

> | Parameter  |   Type    | Description |
> |------------|-----------|-------------|
> | `id`       |  integer  | Track Id = `286266926` |
> | `quality`  |  string   | Song Quality = `HI_RES_LOSSLESS` or `HI_RES` or `LOSSLESS` or `HIGH` or `LOW ` |


<br>

#### Example

>HTTPie

    https GET "https://tidal.401658.xyz/track/?id=286266926&quality=LOSSLESS"
    

![image](https://github.com/sachinsenal0x64/Hifi-Tui/assets/127573781/e586ec03-68eb-4c54-b6ee-251093f4b8a6)

<br>


### Response

  ```json
{
        "albumPeakAmplitude": 1.0,
        "albumReplayGain": -9.18,
        "assetPresentation": "FULL",
        "audioMode": "STEREO",
        "audioQuality": "LOSSLESS",
        "bitDepth": 16,
        "manifest": "base64 manifest",
        "manifestMimeType": "application/vnd.tidal.bts",
        "sampleRate": 44100,
        "trackId": 286266926,
        "trackPeakAmplitude": 0.988482,
        "trackReplayGain": -7.89
    },
    {
        "originalTrack": "aka song track"
    }
```
<br>


### Status Codes

HIFI returns the following status codes in its API:

> | Status Code | Description |
> | :---        | :--- |
> | 200         | `OK` |
> | 422         | `UNPROCESSABLE CONTENT` |
> | 404         | `NOT FOUND` |
> | 500         | `INTERNAL SERVER ERROR` |


</details>

------------------------------------------------------------------------------------------



<details>

 <summary><code>GET</code>   <code><b>/search/</b></code> </summary>

## Request

<br>

> | Parameter | Type | Description |
> |------|--------|-------------|
> | `s`  | string |  Name = `Spaceship`|
> | `a`  | string |  Artist Name = `Kanye West`|
> | `al` | string |  Album Name = `Late Registration`|
> | `v`  | string |  Video Name = `Spaceship`|
> | `p`  | string |  Playlist Name = `Pop Hits`|
> | `f`  | int    |  Artist ID = `7162333`| 

<br>

#### Example
>HTTPie

    https GET "https://tidal.401658.xyz/search/?s=Consequence"

![2023-11-19_03-05](https://github.com/sachinsenal0x64/Hifi-Tui/assets/127573781/35041774-394c-4b17-9cfd-927e5e113da3)

<br>


### Response

```json

{
  "limit": 1,
  "offset": 0,
  "totalNumberOfItems": 200,
  "items": [
    {
      "id": 82448461,
      "title": "Consequence",
      "duration": 313,
      "replayGain": -9.88,
      "peak": 1,
      "allowStreaming": true,
      "streamReady": true,
      "streamStartDate": "2017-12-05T00:00:00.000+0000",
      "premiumStreamingOnly": false,
      "trackNumber": 10,
      "volumeNumber": 1,
      "version": null,
      "popularity": 6,
      "copyright": "City Slang/big Store",
      "url": "http://www.tidal.com/track/82448461",
      "isrc": "DED620118410",
      "editable": false,
      "explicit": false,
      "audioQuality": "LOSSLESS",
      "audioModes": [
        "STEREO"
      ],
      "artist": {
        "id": 3529689,
        "name": "The Notwist",
        "type": "MAIN"
      },
      "artists": [
        {
          "id": 3529689,
          "name": "The Notwist",
          "type": "MAIN"
        }
      ],
      "album": {
        "id": 82448449,
        "title": "Neon Golden",
        "cover": "ad3ed5f3-37a2-4b27-9002-b83459ab5a0e",
        "videoCover": null
      },
      "mixes": {
        "TRACK_MIX": "001981d70c53d5448599714c407079"
      }
    }
  ]
}

```

<br>

### Status Codes

HIFI returns the following status codes in its API:

> | Status Code | Description |
> | :---        | :--- |
> | 200         | `OK` |
> | 422         | `UNPROCESSABLE CONTENT` |
> | 404         | `NOT FOUND` |
> | 500         | `INTERNAL SERVER ERROR` |


------------------------------------------------------------------------------------------

</details>


------------------------------------------------------------------------------------------

<details>

<summary><code>GET</code> <code><b>/cover/</b></code></summary>


## Request


<br>

> | Parameter  |   Type    | Description |
> |------------|-----------|-------------|
> | `id`       |  integer  | Track Id = `328060990` |
> | `song`     |  string   | Song Name = `Maestro` |

<br>

> #### Sizes = `1280px | 640px | 80px `

<br>

#### Example

>HTTPie

    https GET "https://tidal.401658.xyz/cover/?q=Maestro"
    https GET "https://tidal.401658.xyz/cover/?id=328060990"
    

![image](https://github.com/sachinsenal0x64/Hifi-Tui/assets/127573781/42b43878-00c5-4d35-8210-2cca466bc594)


<br>


### Response

  ```json
[
    {
        "1280": "https://resources.tidal.com/images/6f5c52be/c21c/4fb7/9ce6/0c270f6f1a5a/1280x1280.jpg",
        "640": "https://resources.tidal.com/images/6f5c52be/c21c/4fb7/9ce6/0c270f6f1a5a/640x640.jpg",
        "80": "https://resources.tidal.com/images/6f5c52be/c21c/4fb7/9ce6/0c270f6f1a5a/80x80.jpg",
        "id": 328060988,
        "name": "Maestro: Music by Leonard Bernstein (Original Soundtrack / Dolby Atmos)"
    }
]
```

</details>

------------------------------------------------------------------------------------------


<details>


 <summary><code>GET</code>   <code><b>/song/</b></code> </summary>

## Request


<br>

> | Parameter  |   Type    | Description |
> |------------|-----------|-------------|
> | `q`        |  string   | Song Query   =  `Mine` |
> | `quality`  |  string   | Song Quality = `HI_RES_LOSSLESS` or `HI_RES` or `LOSSLESS` or `HIGH` or `LOW ` |


<br>

#### Example

>HTTPie

    https GET "https://tidal.401658.xyz/song/?q=Mine&quality=HI_RES"
    

![image](https://sachinsenal0x64.github.io/picx-images-hosting/2024-02-07-20:19:04-screenshot.5zw9tsa19wcg.webp)

<br>

### Response

  ```json
{
    "OriginalTrackUrl": "track url",
    "Song Info": {
        "adSupportedStreamReady": true,
        "album": {
            "cover": "22b8ce2a-1912-4fc6-956f-3be5eb4a7f4c",
            "id": 79712262,
            "title": "Mine",
            "vibrantColor": "#a7d9fc",
            "videoCover": null
        },
        "allowStreaming": true,
        "artist": {
            "id": 7384212,
            "name": "Bazzi",
            "picture": "2726f1e5-0435-4c49-a6f7-c2192544638f",
            "type": "MAIN"
        },
        "artists": [
            {
                "id": 7384212,
                "name": "Bazzi",
                "picture": "2726f1e5-0435-4c49-a6f7-c2192544638f",
                "type": "MAIN"
            }
        ],
        "audioModes": [
            "STEREO"
        ],
        "audioQuality": "HI_RES",
        "copyright": "2017",
        "djReady": true,
        "duration": 134,
        "editable": false,
        "explicit": true,
        "id": 79712263,
        "isrc": "USAT21704227",
        "mediaMetadata": {
            "tags": [
                "LOSSLESS",
                "MQA"
            ]
        },
        "mixes": {
            "TRACK_MIX": "0014833cd62b1eecd3b24115e5f8d4"
        },
        "peak": 0.997437,
        "popularity": 64,
        "premiumStreamingOnly": false,
        "replayGain": -10.39,
        "stemReady": false,
        "streamReady": true,
        "streamStartDate": "2017-10-12T00:00:00.000+0000",
        "title": "Mine",
        "trackNumber": 1,
        "url": "http://www.tidal.com/track/79712263",
        "version": null,
        "volumeNumber": 1
    },
    "Track Info": {
        "albumPeakAmplitude": 0.997437,
        "albumReplayGain": -10.39,
        "assetPresentation": "FULL",
        "audioMode": "STEREO",
        "audioQuality": "HI_RES",
        "manifest": "base64 manifest",
        "manifestMimeType": "application/vnd.tidal.bts",
        "trackId": 79712263,
        "trackPeakAmplitude": 0.997437,
        "trackReplayGain": -10.39
    }
}

```

### Status Codes

HIFI returns the following status codes in its API:

> | Status Code | Description |
> | :---        | :--- |
> | 200         | `OK` |
> | 422         | `UNPROCESSABLE CONTENT` |
> | 404         | `NOT FOUND` |
> | 500         | `INTERNAL SERVER ERROR` |


</details>

------------------------------------------------------------------------------------------

<details>

 <summary><code>GET</code>   <code><b>/album/</b></code> </summary>

## Request


<br>

> | Parameter  |   Type    | Description |
> |------------|-----------|-------------|
> | `id`       |  integer  | Album Id = `157117504` |


<br>

#### Example

>HTTPie

    https GET "https://tidal.401658.xyz/album/?id=157117504"
    

![image](https://github.com/sachinsenal0x64/picx-images-hosting/raw/master/2024-02-20-19:33:52-screenshot.99t2w3gelf.webp)

<br>


### Response

  ```json
 {
        "adSupportedStreamReady": true,
        "allowStreaming": true,
        "artist": {
            "id": 7162333,
            "name": "Dua Lipa",
            "picture": "28047130-6ada-4955-b3b9-65bed4508618",
            "type": "MAIN"
        },
        "artists": [
            {
                "id": 7162333,
                "name": "Dua Lipa",
                "picture": "28047130-6ada-4955-b3b9-65bed4508618",
                "type": "MAIN"
            }
        ],
        "audioModes": [
            "SONY_360RA"
        ],
        "audioQuality": "LOW",
        "copyright": "℗ 2017 Dua Lipa Limited under exclusive license to Warner Music UK Limited",
        "cover": "deae7f19-5da7-4d73-97be-ce901911c939",
        "djReady": true,
        "duration": 2456,
        "explicit": false,
        "id": 157117504,
        "mediaMetadata": {
            "tags": [
                "SONY_360RA"
            ]
        },
        "numberOfTracks": 12,
        "numberOfVideos": 0,
        "numberOfVolumes": 1,
        "popularity": 36,
        "premiumStreamingOnly": false,
        "releaseDate": "2020-10-05",
        "stemReady": false,
        "streamReady": true,
        "streamStartDate": "2020-10-05T00:00:00.000+0000",
        "title": "Dua Lipa (360 Reality Audio)",
        "type": "ALBUM",
        "upc": "190295160180",
        "url": "http://www.tidal.com/album/157117504",
        "version": null,
        "vibrantColor": "#6d99c6",
        "videoCover": null
    }
```
<br>


### Status Codes

HIFI returns the following status codes in its API:

> | Status Code | Description |
> | :---        | :--- |
> | 200         | `OK` |
> | 422         | `UNPROCESSABLE CONTENT` |
> | 404         | `NOT FOUND` |
> | 500         | `INTERNAL SERVER ERROR` |


</details>

------------------------------------------------------------------------------------------

<details>

 <summary><code>GET</code>   <code><b>/playlist/</b></code> </summary>

## Request


<br>

> | Parameter  |   Type    | Description |
> |------------|-----------|-------------|
> | `id`       |  string  | Playlist UUID = `910c525f-be8a-41a1-b557-2682af2bcef3` |


<br>

#### Example

>HTTPie

    https GET "https://tidal.401658.xyz/playlist/?id=910c525f-be8a-41a1-b557-2682af2bcef3"
    

![image](https://sachinsenal0x64.github.io/picx-images-hosting/2024-02-20-23:15:31-screenshot.67x6v3b7q9.webp)

<br>


### Response

  ```json
 {
        "created": "2015-04-14T16:32:14.636+0000",
        "creator": {
            "id": 5034071,
            "name": "VIC MENSA",
            "picture": "cdd212a2-dadc-466d-9703-7216a9f66da1",
            "type": null
        },
        "description": "",
        "duration": 2696,
        "image": "c41cfe9b-cda1-4364-b517-f6a706741d24",
        "lastItemAddedAt": null,
        "lastUpdated": "2020-03-24T12:27:23.941+0000",
        "numberOfTracks": 11,
        "numberOfVideos": 0,
        "popularity": 0,
        "promotedArtists": [
            {
                "id": 5034071,
                "name": "VIC MENSA",
                "picture": null,
                "type": "MAIN"
            },
            {
                "id": 25022,
                "name": "Kanye West",
                "picture": null,
                "type": "MAIN"
            },
            {
                "id": 3899583,
                "name": "Theophilus London",
                "picture": null,
                "type": "MAIN"
            },
            {
                "id": 5637986,
                "name": "Allan Kingdom",
                "picture": null,
                "type": "MAIN"
            }
        ],
        "publicPlaylist": false,
        "squareImage": "03750282-401b-481c-bf60-55d6ee9fcc27",
        "title": "My Playlist",
        "type": "ARTIST",
        "url": "http://www.tidal.com/playlist/910c525f-be8a-41a1-b557-2682af2bcef3",
        "uuid": "910c525f-be8a-41a1-b557-2682af2bcef3"
    },
    {
        "items": [
            {
                "cut": null,
                "item": {
                    "adSupportedStreamReady": true,
                    "album": {
                        "cover": "43929b37-df27-4e1a-81b2-70692c058674",
                        "id": 44590541,
                        "releaseDate": "2015-04-16",
                        "title": "U Mad",
                        "vibrantColor": "#FFFFFF",
                        "videoCover": null
                    },
                    "allowStreaming": true,
                    "artist": {
                        "id": 5034071,
                        "name": "VIC MENSA",
                        "picture": "cdd212a2-dadc-466d-9703-7216a9f66da1",
                        "type": "MAIN"
                    },
                    "artists": [
                        {
                            "id": 5034071,
                            "name": "VIC MENSA",
                            "picture": "cdd212a2-dadc-466d-9703-7216a9f66da1",
                            "type": "MAIN"
                        },
                        {
                            "id": 25022,
                            "name": "Kanye West",
                            "picture": "26076dbd-7361-40d3-9335-f944d2c49ea6",
                            "type": "FEATURED"
                        }
                    ],
                    "audioModes": [
                        "STEREO"
                    ],
                    "audioQuality": "LOSSLESS",
                    "copyright": "(C) 2015 Roc Nation Records, LLC",
                    "dateAdded": "2015-04-15T15:03:19.696+0000",
                    "description": null,
                    "djReady": true,
                    "duration": 300,
                    "editable": false,
                    "explicit": true,
                    "id": 44590542,
                    "index": 0,
                    "isrc": "QMJMT1500671",
                    "itemUuid": "90545040-acc7-44c1-9481-7e48f36cefe8",
                    "mediaMetadata": {
                        "tags": [
                            "LOSSLESS"
                        ]
                    },
                    "mixes": {
                        "TRACK_MIX": "00169d5b613bbc32050146c8be21df"
                    },
                    "peak": 0.999359,
                    "popularity": 47,
                    "premiumStreamingOnly": false,
                    "replayGain": -9.38,
                    "stemReady": false,
                    "streamReady": true,
                    "streamStartDate": "2015-04-10T00:00:00.000+0000",
                    "title": "U Mad",
                    "trackNumber": 1,
                    "url": "http://www.tidal.com/track/44590542",
                    "version": null,
                    "volumeNumber": 1
                },
                "type": "track"
            },
```
<br>


### Status Codes

HIFI returns the following status codes in its API:

> | Status Code | Description |
> | :---        | :--- |
> | 200         | `OK` |
> | 422         | `UNPROCESSABLE CONTENT` |
> | 404         | `NOT FOUND` |
> | 500         | `INTERNAL SERVER ERROR` |


</details>

------------------------------------------------------------------------------------------


<details>

 <summary><code>GET</code>   <code><b>/artist/</b></code> </summary>

## Request


<br>

> | Parameter  |   Type    | Description |
> |------------|-----------|-------------|
> | `id`       |  integer  | Artist ID = `5034071` |


<br>

#### Example

>HTTPie

    https GET "https://tidal.401658.xyz/artist/?id=5034071"
    

![image](https://sachinsenal0x64.github.io/picx-images-hosting/2024-02-21-21:19:27-screenshot.1aoq2k57al.webp)

<br>


### Response

  ```json
 [
    {
        "artistRoles": [
            {
                "category": "Artist",
                "categoryId": -1
            },
            {
                "category": "Songwriter",
                "categoryId": 2
            },
            {
                "category": "Production team",
                "categoryId": 10
            },
            {
                "category": "Producer",
                "categoryId": 1
            },
            {
                "category": "Engineer",
                "categoryId": 3
            },
            {
                "category": "Performer",
                "categoryId": 11
            }
        ],
        "artistTypes": [
            "ARTIST",
            "CONTRIBUTOR"
        ],
        "id": 5034071,
        "mixes": {
            "ARTIST_MIX": "000720bd7d7867c71a4c63b1fe61cf"
        },
        "name": "VIC MENSA",
        "picture": "cdd212a2-dadc-466d-9703-7216a9f66da1",
        "popularity": 66,
        "url": "http://www.tidal.com/artist/5034071"
    },
    [
        {
            "750": "https://resources.tidal.com/images/cdd212a2/dadc/466d/9703/7216a9f66da1/750x750.jpg",
            "id": 5034071,
            "name": "VIC MENSA"
        }
    ]
]

```
<br>


### Status Codes

HIFI returns the following status codes in its API:

> | Status Code | Description |
> | :---        | :--- |
> | 200         | `OK` |
> | 422         | `UNPROCESSABLE CONTENT` |
> | 404         | `NOT FOUND` |
> | 500         | `INTERNAL SERVER ERROR` |


</details>

------------------------------------------------------------------------------------------

<br>

## 🫂 Contributing
Please refer to [CONTRIBUTING.md](./CONTRIBUTING.md).


<br>

## 🔐 Security Policy
Please refer to [SECURITY.md](./SECURITY.md).

<br>

## 👩‍⚖️ License

This project is licensed under the terms of the MIT license.
