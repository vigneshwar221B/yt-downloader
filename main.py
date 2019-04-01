import tkinter as tk
from pytube import Playlist
from pytube import YouTube

PATH = "/Users/vigneshwar/Desktop/yt-downloader"

def download_video():
    url = tfield1.get()
    yt = YouTube(url)
    yt.streams.first().download(PATH)


def download_playlist():
    url = tfield1.get()
    pl = Playlist(url)
    pl.download_all(PATH)

window = tk.Tk()

window.title("yt-downloader")

window.geometry("600x400")


title = tk.Label(text = "An youtube video/playlist downloader")
title.grid(column = 0 , row = 0)

text1 = tk.Label(text="video url:")
text1.grid(column=0, row=1)

tfield1 = tk.Entry()
tfield1.grid(column = 1 , row = 1)

button1 = tk.Button(text="download video", command=download_video)
button1.grid(column=2, row=2)

text1 = tk.Label(text="playlist url:")
text1.grid(column=0, row=4)

tfield2 = tk.Entry()
tfield2.grid(column=1, row=4)

button2 = tk.Button(text="download playlist",command = download_playlist)
button2.grid(column = 2 , row = 5)

window.mainloop()
