import os
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
from pathvalidate import sanitize_filename

version = "v 1.00"
author = "jaikishpai"


def message_success():
    messagebox.showinfo(title='Success', message='Downloaded Successful!')


def widget():
    sel = IntVar()
    top_frame = Frame(master)
    top_frame.pack(side=TOP)
    bottom_frame = Frame(master)
    top_frame.pack(fill="both", expand=True, padx=20, pady=20)
    bottom_frame.place(in_=top_frame, anchor="c", relx=.5, rely=.5)
    #bottom_frame.pack(side=BOTTOM)
    tk.Label(top_frame, text="Download URL", font=("Arial", 18)).grid(row=4, column=0)
    tk.Label(top_frame, text="Download Path", font=("Arial", 18)).grid(row=5, column=0)
    master.url_path = Entry(top_frame, textvariable=video_link, width=100).grid(row=4, column=1)
    master.download_folder = Entry(top_frame, textvariable=download_path, width=100).grid(row=5, column=1)
    browse_button = Button(top_frame, text="Browse", command=Browse).grid(row=5, column=2)
    tk.Button(bottom_frame, text='Quit', command=master.quit, height=3, width=10).grid(row=0, column=0)

    try:
        download_video_button = Button(bottom_frame, text="Download Video", command=download_video, height=3).grid(row=0, column=1)
        download_audio_button = Button(bottom_frame, text="Download Audio", command=download_audio, height=3).grid(row=0, column=2)
    except Exception as e:
        messagebox.showerror(title="Error", message=e)



def Browse():
    try:
        download_directory = filedialog.askdirectory(title="Save Video")
        download_path.set(download_directory)
    except Exception as e:
        messagebox.showerror(title="Error", message=e)


def download_audio():
    try:
        video = YouTube(video_link.get())
        stream = video.streams.get_audio_only()
        file_name = stream.title
        file_name = sanitize_filename(file_name)
        file_name = file_name + "_audio.mp4"
        stream.download(output_path=download_path.get(), filename=file_name)
        message_success()
    except Exception as e:
        messagebox.showerror(title="Error", message=e)

def download_video():
    try:
        video = YouTube(video_link.get())
        stream = video.streams.get_highest_resolution()
        file_name = stream.title
        file_name = sanitize_filename(file_name)
        file_name = file_name + "_video.mp4"
        stream.download(output_path=download_path.get(), filename=file_name)
        message_success()
    except Exception as e:
        messagebox.showerror(title="Error", message=e)


# Creating object of tk class
master = tk.Tk()

# Setting the title, background color
# and size of the tkinter window and
# disabling the resizing property
#master.geometry("400x360")
#master.resizable(True, True)
width=1200
height=660
screenwidth = master.winfo_screenwidth()
screenheight = master.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
master.geometry(alignstr)
master.title("YouTube Video Downloader"+"["+version+"]")
master.iconbitmap('YoutubeIcon.ico')
master.config(background="black")
# Creating the tkinter Variables
video_link = StringVar()
download_path = StringVar()
widget()

master.mainloop()
