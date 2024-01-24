from tkinter import *
from tkinter.ttk import Labelframe
import marker
import pygame
import os


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Symphony")
        self.root.geometry("1400x200+100+200")
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()

        trackframe = LabelFrame(self.root, text="Song Track", font=("times new roman", 15, "bold"), bg="Navyblue",
                                fg="white", bd=5, relief=GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)
        # Inserting Song Track Label
        songtrack = Label(trackframe, textvariable=self.track, width=20, font=("times new roman", 24, "bold"),
                          bg='orange', fg='gold').grid(row=0, column=0, padx=10, pady=5)
        trackstatus = Label(trackframe, textvariable=self.status, font=("times new roman", 24, "bold"), bg='orange',
                            fg='gold').grid(row=0, column=1, padx=10, pady=5)
        # ButtonFrame
        buttonframe = LabelFrame(self.root, text="Control Panel", font=("times new roman", 15, "bold"), bg="grey",
                                 fg="white", bd=5, relief=GROOVE)
        buttonframe.place(x=0, y=100, width=600, height=100)

        plybtn = Button(buttonframe, text="PLAY", command=self.playsong, width=10, height=1,
                        font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=0, padx=10,
                                                                                             pady=5)
        pausebtn = Button(buttonframe, text="PAUSE", command=self.pause, width=8, height=1,
                          font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=1, padx=10,
                                                                                               pady=5)
        unpbtn = Button(buttonframe, text="UNPAUSE", command=self.unpause, width=10, height=1,
                        font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=2, padx=10,
                                                                                             pady=5)
        stpbtn = Button(buttonframe, text="STOP", command=self.stop, width=10, height=1,
                        font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=3, padx=10,
                                                                                             pady=5)

        # song frame
        songframe = LabelFrame(self.root, text="Playlist", font=("times new roman", 15, "bold"), bg="grey", fg="white",
                               bd=5, relief=GROOVE)
        songframe.place(x=600, y=0, width=400, height=200)
        # scrolling and lust
        scrol_y = Scrollbar(songframe, orient=VERTICAL)
        self.playlist = Listbox(songframe, yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=SINGLE,
                                font=("times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

        # adding songs
        os.chdir('music')
        songstrack = os.listdir()

        for i in songstrack:
            self.playlist.insert(END, i)

        self.shapeframe = LabelFrame(self.root, text="Shapes", font=("times new roman", 15, "bold"), bg="grey",
                                     fg="white", bd=5, relief=GROOVE)
        self.shapeframe.place(x=1000, y=0, width=400, height=200)
        # shape = Shape(shapeframe)

    def playsong(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-PLAYING")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()
        Shape(self.shapeframe)

    def pause(self):
        self.status.set("-PAUSED")
        pygame.mixer.music.pause()

    def stop(self):
        self.status.set("-STOPPED")
        pygame.mixer.music.stop()

    def unpause(self):
        self.status.set("-PLAYING")
        pygame.mixer.music.unpause()


class Shape:
    def __init__(self, master=None):
        self.master = master

        # Calls create method of class Shape
        self.master.after(1000, self.rect)

    def rect(self):
        canvas = Canvas(self.master)
        canvas.create_rectangle(230, 10, 290, 60, outline="black", fill="blue", width=2)
        canvas.pack(fill=BOTH, expand=1)
        self.master.after(3000, canvas.destroy)
        self.master.after(2000, self.circle)

    def circle(self):
        canvas = Canvas(self.master)
        canvas.create_oval(10, 10, 80, 80, outline="black", fill="white", width=2)
        canvas.pack(fill=BOTH, expand=1)
        self.master.after(3000, canvas.destroy)
        self.master.after(2000, self.ellipse)

    def ellipse(self):
        canvas = Canvas(self.master)
        canvas.create_oval(110, 10, 210, 80, outline="red", fill="green", width=2)
        canvas.pack(fill=BOTH, expand=1)