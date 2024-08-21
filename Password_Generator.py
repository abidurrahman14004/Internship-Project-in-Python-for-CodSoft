import tkinter as tk
from tkinter import *
import random
import string

root = Tk()
root.title("Password Generator for CodeSoft")

root.geometry("400x300")
root.resizable(False, False)


heading = Label(root, text="Generate your Password", font="poppins 20 bold", fg="white", bg="black")
heading.place(x=32, y=20)


label = Label(root, text="Choose your Length")
label.place(x=150, y=70)


val = IntVar(value=8) 
spinlength = Spinbox(root, from_=8, to_=24, textvariable=val, width=50)
spinlength.place(x=40, y=100)


def passgen():
    number = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return "".join(random.sample(number, val.get()))


def callback():
    generated_password = passgen()
    lsum.config(text=generated_password)

passButton = Button(root, text="Generate Password",font="poppins 10 ", bd=5, height=2 ,bg="light green", command=callback)
passButton.place(x=140, y=140)


lsum = Label(root, text="", bg="#ffffff", width=40, height=2)
lsum.place(x=50, y=210)

root.mainloop()
