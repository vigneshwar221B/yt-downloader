from pytube import YouTube
import sys
import os

VIDEO_PATH = os.getcwd()+"/videos"

if len(sys.argv) == 2:
    yt = YouTube(sys.argv[1])
    yt.streams.first().download(VIDEO_PATH)
