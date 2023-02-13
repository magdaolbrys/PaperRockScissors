from tkinter import *
from tkinter import Button
from tkinter import font
import random


def RockPaperScisors(choice, computer):
    if choice == 'rock':
        if computer == 'scissors':
            return True
        elif computer == 'paper':
            return False
        else:
            return None
    elif choice == 'paper':
        if computer == 'rock':
            return True
        elif computer == 'scissors':
            return False
        else:
            return None
    elif choice == 'scissors':
        if computer == 'rock':
            return False
        elif computer == 'paper':
            return True
        else:
            return None

won = []
lost = []
draw = []

def game(choice):
    computer = random.choice(['rock', 'paper', 'scissors'])
    x = RockPaperScisors(choice, computer)

    if x == True:
        won.append(1)
        label.config(text=f"Computer: {computer}\n You: {choice} \n{choice} beats {computer} \n You win! \n Try again: ", fg="green", font = fnt2)
        points.config(text=f"\nWon: {len(won)} \t\t Lost: {len(lost)} \t\t Draw: {len(draw)}", font=fnt2)
    elif x == False:
        lost.append(1)
        label.config(text=f"Computer: {computer}\n You: {choice}\n {computer} beats {choice} \n You lose! \n Try again: ", fg="red", font = fnt2)
        points.config(text=f"\nWon: {len(won)} \t\t Lost: {len(lost)} \t\t Draw: {len(draw)}", font = fnt2)
    else:
        draw.append(1)
        label.config(text=f"Computer: {computer}\n You: {choice}\n Draw!\n\n Try again: ", fg="blue", font = fnt2)
        points.config(text=f"\nWon: {len(won)} \t\t Lost: {len(lost)} \t\t Draw: {len(draw)}", font=fnt2)


def reset():
    won = []
    lost = []
    draw = []
    label.config(text="Let's play paper, rock, scissors!\n\n", font=fnt, fg="black")
    points.config(text=f"\nWon: {len(won)} \t\t Lost: {len(lost)} \t\t Draw: {len(draw)}", font=fnt2)


root = Tk()
root.title('Paper Rock Scissors')
root.geometry("800x500")

fnt = font.Font(family="Helvetica", size =50, weight= "bold")
fnt2 = font.Font(family="Helvetica", size =30, weight= "bold")
label = Label(root, text="Let's play paper, rock, scissors!\n\n", font=fnt, fg="black")
label.pack()

Button(root, text="🧻 Paper", font=fnt, width=10, command = lambda: game('paper')).pack()
Button(root, text="👊 Rock", font=fnt, width=10, command= lambda: game('rock')).pack()
Button(root, text="✂️ Scissors", font=fnt, width=10, command= lambda: game('scissors')).pack()

reset_button = Button(root, text="RESET", font=fnt2, width=8, command = lambda: reset())
reset_button.place(x = 10, y = 100)

points = Label(text=f"\nWon: {len(won)} \t\t Lost: {len(lost)} \t\t Draw: {len(draw)}", font=fnt2)
points.pack()

root.mainloop()

