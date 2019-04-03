import tkinter as tk
from pytube import YouTube
import sys

VIDEO_PATH = "/Users/vigneshwar/Desktop/yt-downloader/videos"

if len(sys.argv) == 2:
    yt = YouTube(sys.argv[1])
    yt.streams.first().download(VIDEO_PATH)
