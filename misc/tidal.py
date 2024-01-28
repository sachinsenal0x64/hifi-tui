from ytmusicapi import YTMusic
import sys
import rich
import mpv
import time
import locale
from rich.progress import track, Progress
from pynput.keyboard import Key, Controller
import re
from tqdm import tqdm
import threading
import os
import yt_dlp
import warnings
import requests
from requests.auth import HTTPBasicAuth
import json
import webbrowser
import base64
from textual.app import App, ComposeResult
from rich.progress import track
from textual.containers import Center, Middle
from textual.timer import Timer
from textual.widgets import Footer, ProgressBar


warnings.filterwarnings(action="once")
warnings.simplefilter("ignore")


ytmusic = YTMusic()

key = Controller()


choice = input(
    "Choose a music source:\n1. YouTube Music\n2. Tidal HiFi\nEnter 1 or 2: "
)


def clear_screen():
    if os.name == "nt":
        os.system("cls")  # Clear the screen on Windows
    else:
        os.system("clear")  #


# Specify the command to run

if choice == "1":
    ask = input("search: ")

    # Convert the input into lowercase
    ask = ask.lower()

    search_results = ytmusic.search(ask)

    print(search_results)

    video_id = search_results[0]["videoId"]

    duration = search_results[0]["duration"]

    song_name = search_results[0]["title"]

    play = ytmusic.get_song(video_id)
    url = play["microformat"]["microformatDataRenderer"]["urlCanonical"]

    # Define the options for yt-dlp
    ydl_opts = {
        "quiet": True,
        "format": "bestaudio/best",
        "no_warnings": True,
    }

    # Create a yt-dlp object and pass in the options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Use the `extract_info` method to get information about the video without downloading it
        info = ydl.extract_info(url, download=False)

    # Extract the best audio URL from the info
    audio_url = info.get("url")

    # Regular expression to extract the 'dur' parameter value
    duration_match = re.search(r"dur=([\d.]+)", audio_url)

    duration_seconds = float(duration_match.group(1))

    rich.print(duration_seconds)

    def format_time(duration_seconds):
        hours = int(duration_seconds // 3600)
        minutes = int((duration_seconds % 3600) // 60)
        seconds = int(duration_seconds % 60)
        formatted_duration = f"{minutes:02}:{seconds:02}"
        return formatted_duration

    def update_progress_bar(player, duration_seconds, song_name):
        try:
            formatted_total_duration = format_time((duration_seconds))
            rich.print(f"Total Duration: {formatted_total_duration}")

            with Progress() as progress:
                task = progress.add_task(
                    "[cyan] Processing...", total=float(duration_seconds)
                )

                while duration_seconds:
                    progress.update(task, completed=player.time_pos)

            # with tqdm(
            #     total=duration_seconds,
            #     bar_format=f"[Song] [{{bar}}] {{desc}}",
            #     colour="#3b8b9c",
            #     ascii=" |",
            # ) as progress_bar:
            #     while duration_seconds:
            #         current_time_pos = player.time_pos
            #         if current_time_pos is not None:
            #             remaining_time = duration_seconds - player.time_pos
            #             formatted_time_pos = format_time(current_time_pos)
            #             progress_bar.n = current_time_pos
            #             description = f" [ {'Pause' if player.pause else 'Play'} ] {formatted_time_pos}/{formatted_total_duration} ({format_time(remaining_time)})"
            #             progress_bar.set_description(description, refresh=True)

        except Exception as e:
            print(f"Error {e}")
        finally:
            player.terminate()


if choice == "2":
    # we need this api keys for grant tidal auth
    class Hifi:
        def __init__(self, client_id, scope, url, client_secret):
            self.client_id = client_id
            self.scope = scope
            self.url = url
            self.client_secret = client_secret

        @staticmethod
        def Quality(quality):
            rate = {quality: "HI_RES"}
            return rate[quality]

    # in here we create url for get AccessToken & RefreshToken
    class Auth(Hifi):
        def __init__(self, client_id, scope, url, client_secret):
            super().__init__(client_id, scope, url, client_secret)
            data = {"client_id": client_id, "scope": scope}
            header = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G965F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36"
            }

            res = requests.post(url, data=data, headers=header)

            self.response = res

            def __str__(self):
                return str(self.response)

    if choice == "2":
        authrize = Auth(
            client_id="zU4XHVVkc2tDPo4t",
            scope="r_usr+w_usr+w_sub",
            url="https://auth.tidal.com/v1/oauth2/device_authorization",
            client_secret="VJKhDFqJPqvsPVNBV6ukXTJmwlvbttP7wlMlrc72se4=",
        )

    res = authrize.response.json()

    verifyurl = res["verificationUriComplete"]
    dcode = res["deviceCode"]

    rich.print(verifyurl)
    rich.print(dcode)

    HI_RES = authrize.Quality(quality="True")

    rich.print(HI_RES)

    webbrowser.open(verifyurl)

    # Polling Until Authrize
    url2 = "https://auth.tidal.com/v1/oauth2/token"

    data2 = {
        "client_id": authrize.client_id,
        "scope": authrize.scope,
        "device_code": dcode,
        "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
    }

    basic = HTTPBasicAuth(authrize.client_id, authrize.client_secret)

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

    url3 = f"https://api.tidal.com/v1/tracks/286266926/playbackinfopostpaywall/v4?audioquality=LOSSLESS&playbackmode=STREAM&assetpresentation=FULL"

    header = {"authorization": f"Bearer {acs_tok}"}

    res3 = requests.get(url=url3, headers=header)

    rich.print(res3.text)

    mani = res3.json()["manifest"]

    decodem = base64.b64decode(mani)

    loaddeco = json.loads(decodem)

    audio_url = loaddeco.get("urls")[0]

    print(audio_url)


if __name__ == "__main__":
    # clear_screen()

    # Configure mpv player
    locale.setlocale(locale.LC_NUMERIC, "C")
    player = mpv.MPV(
        input_default_bindings=True,
        input_vo_keyboard=True,
        terminal=True,
        input_terminal=True,
        really_quiet=True,
    )

    @player.on_key_press("r")
    def rep():
        player.loop = not player.loop
        print("repeat")

    @player.on_key_press("UP")
    def increase_volume():
        player.volume += 5

    @player.on_key_press("DOWN")
    def decrease_volume():
        player.volume -= 5

    # @player.on_key_press('q')
    # def my_q_binding():
    #     player.pause = not player.pause
    #     print('pause')

    player.play(audio_url)

    # Create a separate thread to update the progress bar
    progress_thread = threading.Thread(
        target=update_progress_bar, args=(player, duration_seconds, song_name)
    )

    progress_thread.start()
    player.wait_for_playback()
    progress_thread.join()
