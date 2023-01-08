import time
from tkinter import *
from pygame import mixer
import os


status = False
track_number = 0

tk = Tk()
tk.title('Name')
tk['bg'] = '#584141'
tk.resizable(False, False)

music_list = os.listdir('music_pack')
file = open(f'music_pack/{music_list[track_number]}', 'rb')
music_names = [i.split('.')[0] for i in music_list]


def Volume(val):
    mixer.music.set_volume(int(val)/100)


def Prev_track():
    global track_number
    global status
    status = False
    if track_number > 0 and track_number <= len(music_list) - 1:
        track_number -= 1
        nazva.configure(text=f'{music_names[track_number]}')
        b1.configure(image=photo_pause)
        b2.configure(state=NORMAL)
        file = open(f'music_pack/{music_list[track_number]}', 'rb')
        mixer.music.load(file)
        mixer.music.play()


def Next_track():
    global track_number
    global status

    status = False
    if track_number >= 0 and track_number < len(music_list) - 1:
        track_number += 1
        b1.configure(image=photo_pause)
        b3.configure(state=NORMAL)
        nazva.configure(text=f'{music_names[track_number]}')
        file = open(f'music_pack/{music_list[track_number]}', 'rb')
        mixer.music.load(file)
        mixer.music.play()


def Button_press():
    global status
    status = not status
    if status:
        b1.configure(image=photo_play)
        mixer.music.pause()
    if not status:
        b1.configure(image=photo_pause)
        mixer.music.unpause()


canvas = Canvas(tk, width=350, height=600, bg='#584141', highlightthickness=0)
canvas.pack()


photo_pause = PhotoImage(file='photo/pause.png').subsample(2, 2)
photo_play = PhotoImage(file='photo/play.png').subsample(2, 2)
photo_right = PhotoImage(file='photo/right.png').subsample(4, 4)
photo_left = PhotoImage(file='photo/left.png').subsample(4, 4)


b1 = Button(tk, image=photo_pause, highlightthickness=0, bd=0, bg='#584141', activebackground='#584141', command=Button_press)
b1.place(x=110, y=200)
b2 = Button(tk, image=photo_right, highlightthickness=0, bd=0, bg='#584141', activebackground='#584141', command=Next_track)
b2.place(x=245, y=235)
b3 = Button(tk, image=photo_left, highlightthickness=0, bd=0, bg='#584141', activebackground='#584141', command=Prev_track)
b3.place(x=45, y=235)

nazva = Label(text=f'{music_names[track_number]}', font= 'Arial 20', fg='white', bg='#584141')
nazva.place(x=20, y=30)

slider = Scale(tk, from_=0, to=100, length=80, orient='horizonta', command=Volume, bd=0, highlightthickness=0, background='#584141')
slider.set(40)
slider.place(x=120, y=320)

mixer.init()
mixer.music.load(file)
mixer.music.set_volume(slider.get())
mixer.music.play()

tk.mainloop()