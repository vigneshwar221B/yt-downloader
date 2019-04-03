import tkinter as tk
from PIL import ImageTk, Image
from pytube import Playlist
from pytube import YouTube

import time

# test_url = https://www.youtube.com/watch?v=IGQBtbKSVhY

VIDEO_PATH = "/Users/vigneshwar/Desktop/yt-downloader/videos"
PLAYLIST_PATH = "/Users/vigneshwar/Desktop/yt-downloader/playlist"
t = 0

def is_valid(url):
    if not url:
        print("false")
        return False
    else:
        return True


def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
    print(bytes_remaining)
    if bytes_remaining == 0:
        global t
        my_string_var.set(f"Downloaded!!! finished in {format(time.time()-t, '.2f')} sec")

def download_video():
    global t
    t = time.time()
    url = tfield1.get()
    print(url)
    if is_valid(url):
        yt = YouTube(url)
        yt.register_on_progress_callback(show_progress_bar)
        yt.streams.first().download(VIDEO_PATH)


def download_playlist():
    url = tfield1.get()
    if is_valid(url):
        pl = Playlist(url)
        pl.download_all(PLAYLIST_PATH)


window = tk.Tk()
my_string_var = tk.StringVar(value="!")

window.title("yt-downloader")
window.resizable(False, False)
window.geometry("650x400")

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

label1 = tk.Label(textvariable = my_string_var)
label1.grid(column=1, row=6)

img = ImageTk.PhotoImage(Image.open(r"/Users/vigneshwar/Desktop/yt-downloader/image1.jpg").resize((150, 150), Image.ANTIALIAS))
panel = tk.Label(image=img)
panel.grid(column = 1, row = 7)

window.mainloop()
