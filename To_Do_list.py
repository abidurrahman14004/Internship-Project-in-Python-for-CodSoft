import tkinter as tk
from tkinter import *

root = Tk()
root.title("To-Do list for CodeSoft")
root.geometry("400x600+400+100")
root.resizable(False, False)

task_list = []

def addTask():
    task = entry.get()
    entry.delete(0, END)
    
    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"{task}\n")
            task_list.append(task)
            listitems.insert(END, task)

def deleteTask():
    task = str(listitems.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listitems.delete(ANCHOR)

def OpenTaskFile():
    try:
        global task_list
    
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
            for task in tasks:
                if task != '\n':
                    task_list.append(task.strip())
                    listitems.insert(END, task.strip())
    
    except FileNotFoundError:
        file = open('tasklist.txt', 'w')
        file.close()

heading = Label(root, text="To Do List", font="poppins 20 bold", fg="white", bg="green")
heading.place(x=130, y=20)

frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=100)

task = StringVar()
entry = Entry(frame, width=18, font="poppins 20", bd=0, textvariable=task)
entry.place(x=10, y=7)
entry.focus()

button = Button(frame, text="ADD", font="poppins 20 bold", width=6, bg="red", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)

newframe = Frame(root, bd=3, width=700, height=350, bg="#32405b")
newframe.pack(pady=(160, 0))

listitems = Listbox(newframe, font=("poppins", 12), width=40, height=16, bg="#000080", fg="white", cursor="hand2", selectbackground="#5a95ff")
listitems.pack(side=LEFT, fill=BOTH, padx=2)

scroll = Scrollbar(newframe)
scroll.pack(side=RIGHT, fill=BOTH)

listitems.config(yscrollcommand=scroll.set)
scroll.config(command=listitems.yview)

OpenTaskFile()


delete_image_path = "images/delete.png"
try:
    delete = PhotoImage(file=delete_image_path)
    Button(root, image=delete, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)
except TclError:
    print(f"Image not found at {delete_image_path}. Please check the file path.")

root.mainloop()
