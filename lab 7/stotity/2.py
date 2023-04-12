from pygame import mixer as mix
import pygame as pg
import os
from sys import exit
from tkinter import *
from tkinter import filedialog

Playlist=[]

allsongs = os.listdir(r"C:\Users\miss_\OneDrive\Рабочий стол\pp2 labs\lab 7\stotity")
for song in allsongs:
       if song.endswith(".mp3"):
           Playlist.append(song)

pg.init()
mix.init()
clock=pg.time.Clock() # 

screen=pg.display.set_mode((550, 300))
pg.display.set_caption("kama creates stotity")


bg=pg.Surface((550,300)) #
pg.Surface.fill(bg,(90,241,87))
f1=pg.font.SysFont('montserrat', 30, True) #
f2=pg.font.SysFont('montserrat', 15)



btnplay=pg.image.load("play.png")
btnpause=pg.image.load("pause.png")

btnnext=pg.image.load("next.png")
btnnext2=pg.image.load("next.png")

btnprev=pg.image.load("previous.png")
btnprev2=pg.image.load("previous.png")


currid=0
currsong=pg.mixer.music.load(Playlist[currid])
pg.mixer.music.play()
pg.mixer.music.pause()
ch=False
ch1=False
ch2=False
tm=0
tm2=0

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        elif event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                if(ch):
                    pg.mixer.music.pause()
                    ch=0
                else:
                    pg.mixer.music.unpause()
                    ch=1
            if event.key==pg.K_RIGHT:
                currid=(currid+1)%8
                pg.mixer.music.stop()
                pg.mixer.music.load(Playlist[currid])
                pg.mixer.music.play()
                ch1=True
                if not ch :
                    pg.mixer.music.pause()
            if event.key==pg.K_LEFT:
                currid=(currid-1+8)%8
                pg.mixer.music.stop()
                pg.mixer.music.load(Playlist[currid])
                pg.mixer.music.play()
                ch2=True
                if not ch :
                    pg.mixer.music.pause()
                   


                  
    text1=f1.render("From the playlist: The greatest music of all times", True, (198,165,15))
    text2=f2.render(Playlist[currid], True, (99,20,108))        
    screen.blit(bg, (0,0))
    screen.blit(text1,(25,25))
    screen.blit(text2,(100,50))
    if ch:
        screen.blit(btnpause, (200,90))
    else:
        screen.blit(btnplay, (195,90))

    if ch1:
        screen.blit(btnnext2, (295,90))
        tm+=1
    else:
        screen.blit(btnnext, (295,90))

    if ch2:
        screen.blit(btnprev2, (95,90))
        tm2+=1
    else:
        screen.blit(btnprev, (95,90))

    if tm>=8:
        ch1=False
        tm=0
    if tm2>=8:
        ch2=False
        tm2=0
    pg.display.update()
    clock.tick(60)