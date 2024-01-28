<img src="https://cdn.jsdelivr.net/gh/sachinsenal0x64/PICX-IMAGE-HOSTING@master/ledstrip.3024rqxzahq0.gif"
width="1800"  height="3">

[![hifi-tui](https://sachinsenal0x64.github.io/picx-images-hosting/wallpaperflare.com_wallpaper.3cauvcxohri8.webp)](https://en.wikipedia.org/wiki/Lilith)

<div align="center">

 <p align="center">
 
  <img src="https://cdn.jsdelivr.net/gh/sachinsenal0x64/picx-images-hosting@master/audio-Spectrum-.2jn5ghwym6w0.gif" alt="Audio Spectrum" align="center"> 
  
</p>
</div>

<img src="https://cdn.jsdelivr.net/gh/sachinsenal0x64/PICX-IMAGE-HOSTING@master/ledstrip.3024rqxzahq0.gif"
width="1800"  height="3">

<h1 align="center"> HIFI TUI </h1>

<h4 align="center"> 🎵 Tidal Reverse Proxy & TUI With Extra Batteries. </h4>

<div align="center">
        
[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](https://opensource.org/licenses/MIT) [![FASTAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com) [![Python](https://img.shields.io/badge/-Python-FCC624?style=style=flat-square&logo=Python)](https://www.python.org) [![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=style=flat-square&logo=go&logoColor=white)](https://go.dev/)


   
  
</div>

<br><br>

# 💕 Community

> 🍻 Join the community: <a href="https://www.reddit.com/r/hifitui">Reddit</a> & <a href="https://discord.gg/EbfftZ5Dd4">Discord</a>
 [![](https://cdn.statically.io/gh/sachinsenal0x64/picx-images-hosting@master/reddit(1).4iicqsrtq6m8.webp)](https://www.reddit.com/r/hifitui) [![](https://cdn.statically.io/gh/sachinsenal0x64/picx-images-hosting@master/discord.72y8nlaw5mdc.webp)](https://discord.gg/EbfftZ5Dd4)
 
<br>


# <img src="https://sachinsenal0x64.github.io/picx-images-hosting/svgviewer-output(1).4gs81c9ecqkg.svg" alt="Status" height="40px" width="40px"> TIDAL REVERSE API

> [!NOTE]  
> TUI based on this api and it free & opensource.

> https://tidal.401658.xyz

> https://status.401658.xyz

<br>

# 📌 NOTE

> We DO NOT encourage piracy and made for purely educational purposes / personal use.

> I'm currently paying for a Tidal HiFi Plus subscription.

> You can access our rest api for free if you want to self-host then need tidal subscription.

> TUI is plug & play also you can add your own tidal account but by default its has our API so you can access tidal music for free.
 
<br>

# ❓ WHY ?

I love terminal/CLI tools as well as music, so why not to have a tidal music client for the terminal? Unfortunately, I haven't found any terminal client yet, and that's why it's all about :)

<br>

# 🚀 Features

- 🍟 TIDAL PREMIUM (HIFI-PLUS) YOU CAN ACCESS FOR FREE USING OUR  [API](https://tidal.401658.xyz) & TUI PLAYER
  
- 📀 AUDIO QUALITY / CODEC: DOLBY ATMOS | MQA 96K | HI RES FLAC | FLAC | HIGH | LOW | Up to 24-bit, 192 kHz

- 🎧 TIDAL-HIFI | PODCAST | YOUTUBE MUSIC PLAYER IN TUI  (⭕ in progress)
  
- 👤 TIDAL ACCOUNTS MANAGEMENT 

- 📚 PLAYLISTS | RECENT PLAYBACK | LIBARAY MANAGEMENT (⭕ in progress)

- 🕹 QUALITY SWITCH   (⭕ in progress)

- 📡 REST API (ACT AS REVERSE PROXY INSTANCE)

- ⚖️ LAYER 7 LOAD BALANCER (ACT AS API GATEWAY | Purely Python & GO Implementations)

- ⚡️ ASYNC SUPPORT

- 📑 DOCS SUPPORT ( SWAGGER UI ) 

<br>


# 💨 Quick Start

## 🏠 HOW TO SELF-HOST (API)

> [!NOTE]
> This required tidal subscription / Redis & Fill the .env file.

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
git clone https://github.com/sachinsenal0x64/Hifi-Tui.git
cd Hifi-Tui
cd API
rename .env-example to .env
pip install -r requirements.txt
python main.py

```
![fastapi](https://sachinsenal0x64.github.io/picx-images-hosting/300191675-4330ea31-3f15-45b0-962c-ca5a85041f02.5tz3jj54f2ps.webp)


<br>

## 📡 API DOCUMENTATION

> [!TIP]
> You can access reverse [api](https://github.com/sachinsenal0x64/Hifi-Tui#-tidal-reverse-api) for free.

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
> | `quality`  |  string   | Song Quality = `HI_RES` or `LOSSLESS` or `HIGH` or `LOW ` |


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

 <summary><code>GET</code>   <code><b>/song/</b></code> </summary>

## Request

<br>

> | Parameter | Type | Description |
> |------|--------|-------------|
> | `q`  | string | Song Name = `Consequence`|

<br>


#### Example
>HTTPie

    https GET "https://tidal.401658.xyz/search/?q=Consequence"

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
> | `sizes`    |  string   | Size =  `1280 / 640 / 80`|

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

<br>


## 🏠 HOW TO INSTALL (TUI)


> [!NOTE]
> Tui player based on reverse [api](https://github.com/sachinsenal0x64/Hifi-Tui#-tidal-reverse-api) so its totally free and easy to install via package manager 


(⭕ WIP)

<br>

## 🏗️ Contributing

> Workflow Diagram
<br>

![2023-11-06_18-12](https://cdn.statically.io/gh/sachinsenal0x64/picx-images-hosting@master/2023-11-08_23-58.220qxiet1zkw.png)


- Before send PR first open a issue then fork the repo.
  
- We need volunteers who have Tidal subscriptions because we might get banned by Tidal.

- Feel free to send PR's regarding spelling mistakes, incorrect grammar etc.

- All of your commits should go to the dev or misc branch. Please don't push to the main branch.
  

<br>

## 👩‍⚖️ License

This project is licensed under the terms of the MIT license.
