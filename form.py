from tkinter import *
from datetime import date
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')
lbl = Label(text = "Hi bro" , fg = "red" , bg = "#FFFF00" , height = 150 , width = 100)
name_lbl = Label(text = "Full name" , bg = "#FFFFFF")
name_entry = Entry()
def display():
    name = name_entry.get()
    global message 
    message = "Welcome to the coding Application! /n Todays date is:  "
    greet = "Hello"+name+"/n"
    text_box.insert( End , greet)
    text_box.insert( End , message)
    text_box.insert( End , date.today())
text_box = Text(height = 3)
btn = Button(text = "begin" , command = display , height = 3, bg = "#0000FF" , fg = "white")
lbl.pack() 
name_lbl.pack()  
name_entry.pack()  
btn.pack()    
text_box.pack()   
