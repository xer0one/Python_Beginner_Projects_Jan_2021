from tkinter import *
import pytube

def download():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download('/home/xeroone/Desktop')
        notify.config(fg='green', text='Download Complete')
    except Exception as e:
        print(e)
        notify.config(fg='red', text='Video could not be downloaded')


# - Main Screen
master = Tk()
master.title('Personal Youtube Downloader')

#Labels
Label(master, text='Youtube Video Converter', fg='red', font=('Calibri', 15)).grid(sticky=N, padx = 100, row=0)
Label(master, text='Please enter the link below', fg='black', font=('Calibri', 12)).grid(sticky=N, pady=15, row=1)
notify = Label(master,font=('Calibri', 12))
notify.grid(sticky=N, pady=1, row=4)
url = StringVar()
Entry (master, width=50, textvariable=url).grid(sticky=N, row=2)
Button(master,width=20, text='Download', font=('Calibri', 12), command=download).grid(sticky=N, row=3, pady=15)
master.mainloop()