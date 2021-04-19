import tkinter as tk
#import numpy
import random as r
root= tk.Tk()
root.title("Moving Label")

global clicky
global clickx
global positionx
global positiony
positiony= r.randint(0,360)
positionx = r.randint(0,980)
clickx= 1
clicky= 1
def cover():
    
    global positionx
    global positiony
    coveryy = tk.Label(root,text="          ").place(x= positionx, y=positiony)
    print(positionx)
    print(positiony)
    
def movey():
    global clicky
    global movingl
    global positionx
    global positiony
    if clicky >= 1:
        cover()
    positiony += 20
    yy.set(positiony)
    movingl = tk.Label(root, text = "Going").place(x= positionx, y=positiony)
    clicky += 1
def movex():
    global clickx
    global movingl
    global positiony
    global positionx
    if clickx >= 1:
        cover()
    positionx += 35
    xx.set(positionx)
    movingl = tk.Label(root, text = "Going").place(x = positionx, y=positiony)
    clickx += 1
    
def backy():
    global clicky
    global movingl
    global positionx
    global positiony
    if clicky >= 1:
        cover()
    positiony -= 20
    yy.set(positiony)
    movingl = tk.Label(root, text = "Going").place(x= positionx, y=positiony)
    clicky += 1
def backx():
    global clickx
    global movingl
    global positiony
    global positionx
    if clickx >= 1:
        cover()
    positionx -= 35
    xx.set(positionx)
    movingl = tk.Label(root, text = "Going").place(x = positionx, y=positiony)
    clickx += 1
    
def randpos():
    cover()
    global positionx
    global positiony
    positiony= r.randint(0,360)
    positionx = r.randint(0,940)
    movex()
yy= tk.IntVar()
yy.set(positiony)
xx= tk.IntVar()
xx.set(positionx)
forwardy = tk.Button(root,text = "Move -Y",width=25,command = movey).place(x=300,y=550)
forwardx = tk.Button(root, text = "Move +X", width = 25, command = movex).place(x=500,y=500)
backwardy = tk.Button(root,text = "Move +Y", width=25, command = backy).place(x=300,y=500)
backwardx = tk.Button(root, text = "Move -X", width=25, command = backx).place(x=500,y=550)
randomize = tk.Button(root, text = "Randomize!",width=25,height=5,command = randpos).place(x=400,y=400)
root.geometry("1000x600")
root.mainloop()