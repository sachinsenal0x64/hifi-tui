from ytmusicapi import YTMusic
import rich
import mpv
import time
import locale
from pynput.keyboard import Key, Controller
import re
from tqdm import tqdm
import threading
import os
import yt_dlp
import warnings



warnings.filterwarnings(action='once')
warnings.simplefilter("ignore")


ytmusic = YTMusic()

key = Controller()


ask = input("search: ")

# Convert the input to lowercase
ask = ask.lower()

search_results = ytmusic.search(ask)



video_id = search_results[0]['videoId']

duration =  search_results[0]['duration']

song_name = search_results[0]['title']


play = ytmusic.get_song(video_id)
url = play['microformat']['microformatDataRenderer']['urlCanonical']





# Define the options for yt-dlp
ydl_opts = {
    'quiet': True,
    'format': 'bestaudio/best',
    'no_warnings': True,

}

# Create a yt-dlp object and pass in the options
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    # Use the `extract_info` method to get information about the video without downloading it
    info = ydl.extract_info(url, download=False)

# Extract the best audio URL from the info
audio_url = info.get("url")




def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # Clear the screen on Windows
    else:
        os.system('clear')  #



# Regular expression to extract the 'dur' parameter value
duration_match = re.search(r'dur=([\d.]+)', audio_url)


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
        formatted_total_duration = format_time(duration_seconds)
        rich.print(f"Total Duration: {formatted_total_duration}")

        with tqdm(total=duration_seconds, ncols=100, bar_format="Now Playing {bar}  {desc}", colour='#3b8b9c') as progress_bar:
            while True:
                current_time_pos = player.time_pos
                if current_time_pos is not None:
                    formatted_time_pos = format_time(current_time_pos)
                    progress_bar.n = current_time_pos
                    description = f" {formatted_time_pos}/{formatted_total_duration}"
                    progress_bar.set_description(description)
                    progress_bar.refresh()
                    if current_time_pos >= duration_seconds:
                            break
                time.sleep(0.1)  # Adjust the sleep interval as needed


    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        player.terminate()


if __name__ == '__main__':
    clear_screen()

    # Configure mpv player
    locale.setlocale(locale.LC_NUMERIC, 'C')
    player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True,terminal=True,
                        input_terminal=True)

    # @player.on_key_press('q')
    # def my_q_binding():
    #     player.pause = not player.pause
    #     print('pause')

    player.play(audio_url)


    # Create a separate thread to update the progress bar
    progress_thread = threading.Thread(target=update_progress_bar, args=(player, duration_seconds,song_name))
    progress_thread.start()

    player.wait_for_playback()
    progress_thread.join()








