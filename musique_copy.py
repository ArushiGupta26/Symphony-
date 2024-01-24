from tkinter import *
from random import * 
f1 = open("musique.txt", "r") #path needs to be changed

data = f1.readlines()

data0 = data[0]
data0 = data0.split()
ls = list()
for i in range(len(data0)):
    ls.append(int(data0[i]))

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Symphony")
        self.root.geometry("1000x700+100+0")
        self.track = StringVar()
        self.status = StringVar()

        self.shapeframe = LabelFrame(self.root,text="Shapes",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        self.shapeframe.place(x=0, y=0, width=1000, height=500)
        #matrix Labels
        self.a00 = LabelFrame(self.shapeframe, bd=5)
        self.a00.place(x=0, y=0, width=333, height=150)
        self.a01 = LabelFrame(self.shapeframe, bd=5)
        self.a01.place(x=333, y=0, width=333, height=150)
        self.a02 = LabelFrame(self.shapeframe, bd=5)
        self.a02.place(x=666, y=0, width=333, height=150)
        self.a10 = LabelFrame(self.shapeframe, bd=5)
        self.a10.place(x=0, y=150, width=333, height=150)
        self.a11 = LabelFrame(self.shapeframe, bd=5)
        self.a11.place(x=333, y=150, width=333, height=150)
        self.a12 = LabelFrame(self.shapeframe, bd=5)
        self.a12.place(x=666, y=150, width=333, height=150)
        self.a20 = LabelFrame(self.shapeframe, bd=5)
        self.a20.place(x=0, y=300, width=333, height=150)
        self.a21 = LabelFrame(self.shapeframe, bd=5)
        self.a21.place(x=333, y=300, width=333, height=150)
        self.a22 = LabelFrame(self.shapeframe, bd=5)
        self.a22.place(x=666, y=300, width=333, height=150)

        self.map = dict()
        self.ls1 = [self.a00, self.a01, self.a02, self.a10, self.a12, self.a20, self.a21, self.a22]
        j=0
        for i in range(1,9):
            self.map[i] = self.ls1[j]
            j+=1



        self.ans = list()
        for i in ls:
            self.ans.append(self.map[i])


        #ButtonFrame
        buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="#AFB4FF",fg="white",bd=5,relief=GROOVE)
        buttonframe.place(x=0, y=500, width=1000, height=330)

        plybtn = Button(buttonframe, text="PLAY",command=self.play, width=30, height=1, font=("times new roman", 16, "bold"), fg="#100720", bg="#B1E1FF").grid(row=0, column=0, padx=300, pady=50)
       

        #song frame
        #scrolling and lust
        
        
    def change(self,color,ls, i=0):
            if(i<8):
                ls[i].config(bg=color)
                ls[i].after(1500, self.change, 'white',ls, i)
                ls[i].after(1500, self.change,'aqua',ls,  i+1)

        #shape = Shape(shapeframe)
        
    def play(self):
        
        self.change('aqua', self.ans)


root = Tk()
MusicPlayer(root)
root.mainloop()
