from tkinter import *

import random

window = Tk()
window.title("Hi-Low Game")
window.configure(bg = "#F6B6DD")
window.geometry("900x700")


 
def draw_card():
    return random.randint(1, 13)

def compare_cards(card1, card2, guess):
    if guess == "higher" and card2 > card1:
        return "Correct! The second card is higher."
    elif guess == "lower" and card2 < card1:
        return "Correct! The second card is lower."
    elif guess == "same" and card2 == card1:
        return "It's a match!"
    else:
        return "Sorry, you guessed wrong. Try again!"
    

#BUTTONS
    higher = Button(window, text = "HIGHER", bg ="black", fg = "pink",font = ("Courier New",18,"bold"), width = 30, height = 2, command = lambda:[compare_cards])
    higher.place(x = 30, y = 110)
    higher.config(state = "normal")
    
    
    lower = Button(window, text = "Lower", bg ="black", fg = "pink",font = ("Courier New",18,"bold"), width = 30, height = 2, command = lambda:[compare_cards])
    lower.place(x = 30, y = 110)
    lower.config(state = "normal")

    same = Button(window, text = "Same", bg ="black", fg = "pink",font = ("Courier New",18,"bold"), width = 30, height = 2, command = lambda:[compare_cards])
    same.place(x = 30, y = 110)
    same.config(state = "normal")



window.mainloop()