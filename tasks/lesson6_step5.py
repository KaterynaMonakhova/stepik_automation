#from Tkinter import *
import Tkinter as tk
from Tkinter import Button
from Tkinter import Label
from Tkinter import Entery
root = tk.Tk()
class But_print:
    def __init__(self):
        self.but = Button(root)
        self.but["text"] = "Hello!"
        self.but["width"]=30
        self.but["height"]=5
        self.but["bg"]="green"
        self.but["fg"]="blue"
        self.but.bind("<Button-1>",self.printer)
        self.but.pack()
    def printer(self,event):
        print ("Hello World!")
lab=Label(root, text="Label\ntwo strings", font="Arial 18")
ent=Entery(root, width=30, bd=3)
obj = But_print()
root.mainloop()