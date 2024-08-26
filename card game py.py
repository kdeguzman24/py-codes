from tkinter import *
import random
import sys
from pygame import mixer

#Play the music
mixer.init()
mixer.music.load('music.mp3')

mixer.music.set_volume(5)
mixer.music.play()
mixer.music.play(loops=-1)


# Initialize Tkinter
root = Tk()
root.title("Higher-Lower-Same Guessing Game")
root.geometry("1003x800")
root.resizable(False, False)

# Load the image
background_image = PhotoImage(file="bg_image.png")
background_image = background_image.subsample(2)#size ng bg


canvas = Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Colors
WHITE = "#FFFFFF"
BLACK = "#000000"
BROWN = "#663016"

CARD_WIDTH = 50
CARD_HEIGHT = 80

#random card
def generate_card():
    return random.randint(1, 13)

#user's guess
def check_guess(guess):
    global card1, card2, trees
    
    # Display the second card
    card2_label.config(text=str(card2))
    
    # Compare the cards
    if guess == "higher" and card2 > card1:
        result_label.config(text="Correct!")
        trees += 1
    elif guess == "lower" and card2 < card1:
        result_label.config(text="Correct!")
        trees += 1
    elif guess == "same" and card2 == card1:
        result_label.config(text="A match!")
        trees += 3
    elif guess =="same" and card2 != card1:
        trees -=3
    else:
        result_label.config(text="Wrong!")
        if trees > 0:
            trees -= 1
    
    tree_label.config(text=f"{trees}")
    higher_button.config(state=DISABLED)
    lower_button.config(state=DISABLED)
    same_button.config(state=DISABLED)

# Function to generate a new pair of cards and reset UI
def next_card():
    global card1, card2
    card1 = generate_card()
    card2 = generate_card()
    card1_label.config(text=str(card1))
    card2_label.config(text="")
    result_label.config(text="")
    
    # Enable the buttons for the next round
    higher_button.config(state=NORMAL)
    lower_button.config(state=NORMAL)
    same_button.config(state=NORMAL)

# Function to save and exit the program
def save_and_exit():
    # Save any necessary data here
    
    # Exit the program
    sys.exit()

# Initialize tree counter
trees = 10  # Initial number of trees

# GUI elements
card1_label = Label(root, text="", font=("Arial", 20), bg = BROWN, fg = WHITE, width=6, height=4)
card1_label.place(x=342, y=280)

card2_label = Label(root, text="", font=("Arial", 20), bg = BROWN, fg = WHITE, width=6, height=4)
card2_label.place(x=593, y=280)

higher_button = Button(root, text="Higher", borderwidth=0, command=lambda: check_guess("higher"), width=23, height=1, font=("Arial", 14), bg=BROWN, fg = WHITE)
higher_button.place(x=50, y=569)

lower_button = Button(root, text="Lower", borderwidth=0, command=lambda: check_guess("lower"), width=23, height=1, font=("Arial", 14), bg=BROWN, fg = WHITE)
lower_button.place(x=370, y=569)

same_button = Button(root, text="Same", borderwidth=0, command=lambda: check_guess("same"), width=23, height=1, font=("Arial", 14), bg=BROWN, fg = WHITE)
same_button.place(x=695, y=569)

next_button = Button(root, text="Next", borderwidth=0, command=next_card, font=("Arial", 25), bg = BROWN, fg = WHITE)
next_button.place(x=814, y=305)

result_label = Label(root, text="", font=("Arial", 14), bg = BROWN, fg = WHITE, justify="center")
result_label.place(x=(970 - result_label.winfo_reqwidth()) / 2, y=476)

# Label to display tree counter
tree_label = Label(root, text=f"{trees}", font=("Arial", 30), bg=BROWN, fg=WHITE)
tree_label.place(x=105, y=56)

# Save button
save_button = Button(root, text="Exit", borderwidth=0, command=save_and_exit, font=("Arial", 25), bg = BROWN, fg = WHITE)
save_button.place(x=123, y=300)

# Generate the initial pair of cards
next_card()

root.mainloop()
