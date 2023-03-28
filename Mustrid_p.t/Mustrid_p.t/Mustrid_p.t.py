
from tkinter import *
from math import*
from tkinter import font 




aken = Tk()
aken.title("Tahvel")
tahvel = Canvas(aken, width=180, height=180, background="WHITE")

def Eesti():
    tahvel.create_rectangle(5,5, 180,45, fill="BLUE")
    tahvel.create_rectangle(5,45, 180,90, fill="BLACK")
    tahvel.create_rectangle(5,130, 180,90, fill="WHITE")

def Netherlands():
    tahvel.create_rectangle(5,5, 180,45, fill="RED")
    tahvel.create_rectangle(5,45, 180,90, fill="WHITE")
    tahvel.create_rectangle(5,130, 180,90, fill="BLUE")

def Bahamas():
    tahvel.create_rectangle(5,5,  180,45,fill="#00A9CE")
    tahvel.create_rectangle(5,45,  180,90,fill="YELLOW")
    tahvel.create_rectangle(5,130,  180,90,fill="#00A9CE")
    tahvel.create_polygon(5,5,  90,65,  5,130,  5,4, width=5,fill="BLACK")


rb1=Radiobutton(aken, text="Eesti",variable=IntVar, value=1,command=Eesti) 
rb2=Radiobutton(aken, text="Netherlands",variable=IntVar, value=2,command=Netherlands) 
rb3=Radiobutton(aken, text="Bahamas",variable=IntVar, value=3,command=Bahamas) 


rb1.grid(row=0,column=0)
rb2.grid(row=1,column=0)
rb3.grid(row=2,column=0)

tahvel.grid()

aken.mainloop()
