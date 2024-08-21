from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Rock-Paper-Scissor Game for CodeSoft")
root.configure(bg="skyblue")
root.geometry("1200x700")

heading = Label(root, text="Rock Paper Scissors Game", font="poppins 20 bold", fg="white", bg="#000080")
heading.place(relx=0.5, y=20, anchor=CENTER)


rock_u = ImageTk.PhotoImage(Image.open("./images/rock.png"))
paper_u = ImageTk.PhotoImage(Image.open("./images/paper.png"))
scissor_u = ImageTk.PhotoImage(Image.open("./images/scissors.png"))

rock_c = ImageTk.PhotoImage(Image.open("./images/rock_cp.png"))
paper_c = ImageTk.PhotoImage(Image.open("./images/paper_cp.png"))
scissors_c = ImageTk.PhotoImage(Image.open("./images/scissors_cp.png"))

# Labels for User and Computer
user_label_text = Label(root, text="User", font=("Arial", 18), width=20, bg="#000080", fg="white")
comp_label_text = Label(root, text="Computer", font=("Arial", 18), width=20, bg="#000080", fg="white")

user_label_text.place(x=100, y=60)
comp_label_text.place(x=860, y=60)


user_label = Label(root, image=scissor_u, bg="skyblue")
comp_label = Label(root, image=scissors_c, bg="skyblue")

user_label.place(x=40, y=100)
comp_label.place(x=800, y=100)

# Score labels
playscore = Label(root, text="0", font=("poppins", 30), bg="skyblue", fg="white")
comp_score = Label(root, text="0", font=("poppins", 30), bg="skyblue", fg="white")

playscore.place(x=490, y=250)
comp_score.place(x=750, y=250)


msg = Label(root, font="poppins 30 bold", bg="skyblue", fg="purple", text="")
msg.place(x=610, y=400, anchor=CENTER)

def updateMessage(x):
    msg['text'] = x

def updateUserScore():
    score = int(playscore["text"])
    score += 1
    playscore["text"] = str(score)

def updateComputerScore():
    score = int(comp_score["text"])
    score += 1
    comp_score["text"] = str(score)

def checkWinner(player, computer):
    if player == computer:
        updateMessage("It's a Tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You Lose!")
            updateComputerScore()
        else:
            updateMessage("You Win!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Lose!")
            updateComputerScore()
        else:
            updateMessage("You Win!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You Lose!")
            updateComputerScore()
        else:
            updateMessage("You Win!")
            updateUserScore()


choices = ["rock", "paper", "scissor"]

def updateChoice(x):
    compchoice = choices[randint(0, 2)]

    if compchoice == "rock":
        comp_label.configure(image=rock_c)
    elif compchoice == "paper":
        comp_label.configure(image=paper_c)
    else:
        comp_label.configure(image=scissors_c)

    if x == "rock":
        user_label.configure(image=rock_u)
    elif x == "paper":
        user_label.configure(image=paper_u)
    else:
        user_label.configure(image=scissor_u)

    checkWinner(x, compchoice)


def resetGame():
    playscore["text"] = "0"
    comp_score["text"] = "0"
    msg["text"] = ""
    user_label.configure(image=scissor_u)
    comp_label.configure(image=scissors_c)


rock = Button(root, width=20, height=2, text="ROCK", font="poppins 14 bold", bg="#ff3e4d", fg="white", command=lambda: updateChoice("rock"))
paper = Button(root, width=20, height=2, text="PAPER", font="poppins 14 bold", bg="orange", fg="white", command=lambda: updateChoice("paper"))
scissors = Button(root, width=20, height=2, text="SCISSORS", font="poppins 14 bold", bg="blue", fg="white", command=lambda: updateChoice("scissor"))


reset_button = Button(root, width=20, height=2, text="RESET", font="poppins 14 bold", bg="green", fg="white", command=resetGame)


rock.place(relx=0.2, rely=0.9, anchor=CENTER)
paper.place(relx=0.5, rely=0.9, anchor=CENTER)
scissors.place(relx=0.8, rely=0.9, anchor=CENTER)
reset_button.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()
