"""
Python Audio Player

Libraries:
    - pyGame
    - TKInter

Relevant Documentation:
    - pyGame Mixer Documentation (https://www.pygame.org/docs/ref/mixer.html)

"""

"""Import Modules"""

"""Create Window"""

import pygame
import tkinter as tkr
import os
player = tkr.Tk()

"""Edit Window"""
player.title("Audio Player")
player.geometry("400x540")


"""Playlist Register"""
os.chdir("Portfolio/Music Player/album")
print(os.getcwd())
songlist = os.listdir()


"""Create Playlist"""
playlist = tkr.Listbox(player, highlightcolor="blue", selectmode=tkr.SINGLE)
print(songlist)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1


"""Get Song"""
#file = "Portfolio/Music Player/Song.mp3"

""" Pygame init"""
pygame.init()
pygame.mixer.init()


"""Action Event"""


def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volumeLevel.get())
    print(pygame.mixer.music.get_volume())
    print(volumeLevel.get())


def ExitPlayer():
    pygame.mixer.music.stop()


def Pause():
    pygame.mixer.music.pause()


def UnPause():
    pygame.mixer.music.unpause()


def ChangeVolume(newVolume):
    pygame.mixer.music.set_volume(float(newVolume))


"""Register Buttoms"""
button1 = tkr.Button(player, width=5, height=3, text="PLAY", command=Play)
button2 = tkr.Button(player, width=5, height=3,
                     text="STOP", command=ExitPlayer)
button3 = tkr.Button(player, width=5, height=3, text="PAUSE", command=Pause)
button4 = tkr.Button(player, width=5, height=3, text="UNPAUSE", command=Pause)


"""Song Name"""
#contents1 = tkr.Label(player, text=file)
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable=var)


"""Volume Input"""
volumeLevel = tkr.Scale(player, from_=0.0, to_=1.0,
                        orient=tkr.HORIZONTAL, resolution=0.01, command=ChangeVolume)

"""Place Widgets"""
songtitle.pack()
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
volumeLevel.pack(fill="x")
playlist.pack(fill="both", expand="yes")

"""Activate"""
player.mainloop()
