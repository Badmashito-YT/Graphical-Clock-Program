from tkinter import *
from time import strftime

root = Tk()

root.title("Animesh Clock")

def myTime():
    myString = strftime("%H:%M:%S %p")
    myLabel.config(text= myString)
    myLabel.after(1000,myTime)
    
myLabel = Label(root,font=("ds-digital",80),background="black",foreground="cyan")
myLabel.pack(anchor="center")
myTime()

root.mainloop()
