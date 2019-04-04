import tkinter as tk
from pytube import YouTube
import sys
import os

#getting the current user
current_user = os.getlogin()

#checking the os platform
if os.name == 'posix':
    VIDEO_PATH = f"/Users/{current_user}/Desktop/yt-downloader/videos"
else:
    VIDEO_PATH = f"c:\\users\\{current_user}\\Desktop\\videos"

if len(sys.argv) == 2:
    yt = YouTube(sys.argv[1])
    yt.streams.first().download(VIDEO_PATH)
