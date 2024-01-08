from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from pytube import Playlist
amer=Tk()
amer.title('VideoHacker')
amer.geometry('500x315')
amer.resizable(0,0)
amer.iconbitmap('D:\\EGY-HD\\video-hacker\\vh.ico')
amer.config(background='#4A235A')
Label(text='VideoHacker',fg='white',bg='#4A235A',font=('Gabriola',30,'bold')).pack()
Label(text='Video link : ',bg='#4a235a',fg='white',font='arial 10 bold').place(x=5,y=100)
link=Entry(width=50,font='arial 10 bold')
link.place(x=90,y=103)
Label(text='Video path : ',bg='#4a235a',fg='white',font='arial 10 bold').place(x=5,y=175)
path=Entry(width=50,font='arial 10 bold')
path.place(x=90,y=175)
def browse():
    file=filedialog.askdirectory()
    path.delete(0,END)
    path.insert(0,file)
def dpl():
    l=link.get()
    fp=path.get()
    videos=Playlist(l)
    for video in videos:
        YouTube(video).streams.get_highest_resolution().download(fp)
    state.config(text='complete')
def dv():
    l=link.get()
    videos=l.split(',')
    for video in videos:
        YouTube(video).streams.get_highest_resolution().download(path.get())
        state.config(text='complete')
Button(text='.  .  .',font='impact 10 bold',fg='white',bg='#4a235a',activebackground='#4a235a',activeforeground='white',width=5,command=browse,cursor='hand2').place(y=173,x=450)
Button(text='Download playlist',bg='lightgreen',fg='white',activebackground='lightgreen',activeforeground='white',height=3,width=20,borderwidth=0,font='arial 13 bold',command=dpl,cursor='hand2').place(x=50,y=220)
Button(text='Download video',bg='lightgreen',fg='white',activebackground='lightgreen',activeforeground='white',height=3,width=20,borderwidth=0,font='arial 13 bold',command=dv,cursor='hand2').place(x=260,y=220)
state=Label(text='ready for download',bg='gray',fg='white',width=75)
state.place(x=0,y=292)
amer.mainloop()