# This script takes a video directory and an audio directory as arguments
# The video directory should contain all the videos you want to get audio from
# The audio directory is where the new audio files will be saved
# The audio will be extracted from the videos and saved as mp3 files

import os
import moviepy.editor as mp
import time


def get_created_time(video_path):
    modified_time = os.path.getmtime(video_path)
    # convert to strftime
    return time.strftime("%d-%m-%Y %H:%M", time.localtime(modified_time))


def get_file_name(video_path):
    video_id = video_path.split("#")[1].replace(".mp4", "")
    created_time = get_created_time(video_path)
    return f"{created_time} {video_id}.mp3"


def get_audio_from_video(video_path, audio_path):
    video_files = os.listdir("video_files")
    print(video_files)

    for video in video_files:
        video_path = os.path.join("video_files", video)
        file_name = get_file_name(video_path)
        clip = mp.VideoFileClip(video_path)
        clip.audio.write_audiofile(f"audio_files/{file_name}")


if __name__ == "__main__":
    get_audio_from_video("video_files", "audio_files")
