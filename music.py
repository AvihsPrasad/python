from distutils import command

import pygame
import tkinter as tkr
import os

from Tools.scripts import highlight

player = tkr.Tk()

player.title("Audio player")
player.geometry("330x400")
"""this is used for background transperency"""
player.wm_attributes("-alpha", 1)

os.chdir("D:\\music")
songlist = os.listdir()

pygame.init()
pygame.mixer.init()

volumelevel = tkr.Scale(player, from_=0.0, to_=1.0, orient=tkr.HORIZONTAL, resolution=0.1)

playlist = tkr.Listbox(player, highlightcolor="blue", selectmode=tkr.SINGLE)

for items in songlist:
    pos = 0
    playlist.insert(pos, items)
    pos = pos + 1

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volumelevel.get())
    print(pygame.mixer.music.get_volume())
    print(volumelevel.get())

def exitplayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()



button1 = tkr.Button(player, width=3, height=1, text="PLAY", command= play)
button2 = tkr.Button(player, width=5, height=1, text="stop", command=exitplayer)
button3 = tkr.Button(player, width=5, height=1, text="Pause", command=pause)
button4 = tkr.Button(player, width=5, height=1, text="UnPause", command=unpause)


label1 = tkr.LabelFrame(player, text="song name")
label1.pack(fill="both", expand="yes")

var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable=var)
songtitle.pack()

button1.pack()
button2.pack()
button3.pack()
button4.pack()
volumelevel.pack(fill="x")
playlist.pack(fill="both", expand="yes")


player.mainloop()
