from tkinter import *
import random
import sys
 

# Initialize Tkinter
window = Tk()
window.title("Higher-Lower-Same Guessing Game")
window.geometry("1003x800")

# Load the image
background_image = PhotoImage(file="bg_image.png")
background_image = background_image.subsample(2)  # Adjust scaling if needed

# Create a Canvas widget and add the image
canvas = Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Colors
WHITE = "#FFFFFF"
BLACK = "#000000"
BROWN = "#663016"

# Function to check the user's guess
def check_guess(guess):
    global card1, card2, trees
    
    card2_label.config(text=str(card2))
    
    if guess == "higher" and card2 > card1:
        result_label.config(text="Correct!")
        trees += 1
    elif guess == "lower" and card2 < card1:
        result_label.config(text="Correct!")
        trees += 1
    elif guess == "same" and card2 == card1:
        result_label.config(text="A match!")
        trees += 3
    elif guess == "same" and card2 != card1:
        trees -= 3
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
    card1 = rand_cards1()
    card2 = rand_cards2()
    card1_label.config(text=str(card1))
    card2_label.config(text="")
    result_label.config(text="")
    
    higher_button.config(state=NORMAL)
    lower_button.config(state=NORMAL)
    same_button.config(state=NORMAL)
    
# Function to save and exit the program
def save_and_exit():
    sys.exit()

# Initialize tree counter
trees = 10

# GUI elements
card1_label = Label(window, text="", font=("Wanted", 20), bg=BLACK, fg=WHITE, width=5, height=2)
card1_label.place(x=window.winfo_screenwidth() * 0.35, y=window.winfo_screenheight() * 0.4)

card2_label = Label(window, text="", font=("Arial", 20), bg=BLACK, fg=WHITE, width=5, height=2)
card2_label.place(x=window.winfo_screenwidth() * 0.6, y=window.winfo_screenheight() * 0.4)

higher_button = Button(window, text="Higher", borderwidth=0, command=lambda: check_guess("higher"), width=23, height=1, font=("Arial", 14), bg=BROWN, fg=WHITE)
higher_button.place(x=window.winfo_screenwidth() * 0.05, y=window.winfo_screenheight() * 0.7)

lower_button = Button(window, text="Lower", borderwidth=0, command=lambda: check_guess("lower"), width=23, height=1, font=("Arial", 14), bg=BROWN, fg=WHITE)
lower_button.place(x=window.winfo_screenwidth() * 0.4, y=window.winfo_screenheight() * 0.7)

same_button = Button(window, text="Same", borderwidth=0, command=lambda: check_guess("same"), width=23, height=1, font=("Arial", 14), bg=BROWN, fg=WHITE)
same_button.place(x=window.winfo_screenwidth() * 0.7, y=window.winfo_screenheight() * 0.7)

next_button = Button(window, text="Next", borderwidth=0, command=next_card, font=("Arial", 25), bg=BROWN, fg=WHITE)
next_button.place(x=window.winfo_screenwidth() * 0.8, y=window.winfo_screenheight() * 0.5)

result_label = Label(window, text="", font=("Arial", 14), bg=BROWN, fg=WHITE, justify="center")
result_label.place(x=(window.winfo_screenwidth() - result_label.winfo_reqwidth()) / 2, y=window.winfo_screenheight() * 0.6)

tree_label = Label(window, text=f"{trees}", font=("Arial", 30), bg=BROWN, fg=WHITE)
tree_label.place(x=window.winfo_screenwidth() * 0.1, y=window.winfo_screenheight() * 0.1)

save_button = Button(window, text="Exit", borderwidth=0, command=save_and_exit, font=("Arial", 25), bg=BROWN, fg=WHITE)
save_button.place(x=window.winfo_screenwidth() * 0.1, y=window.winfo_screenheight() * 0.4)

def rand_cards1():
    card1 = random.randint(1,13)
    card1_display = card1
    if card1 == 1:
        card1_display = card2
    elif card1 == 2:
        card1_display = card3
    elif card1 == 3:
        card1_display = card4
    elif card1 == 4:
        card1_display = card5
    elif card1 == 5:
        card1_display = card6
    elif card1 == 6:
        card1_display = card7
    elif card1 == 7:
        card1_display = card8
    elif card1 == 8:
        card1_display = card9
    elif card1 == 9:
        card1_display = card10
    elif card1 == 10:
        card1_display = card11
    elif card1 == 11:
        card1_display = card12
    elif card1 == 12:
        card1_display = card13
    elif card1 == 13:
        card1_display = card14

    card1_label.config(image=card1_display)
    return card1

def rand_cards2():
    card2 = random.randint(1,13)
    card2_display = card2
    if card2 == 1:
        card2_display = card2
    elif card2 == 2:
        card2_display = card3
    elif card2 == 3:
        card2_display = card4
    elif card2 == 4:
        card2_display = card5
    elif card2 == 5:
        card2_display = card6
    elif card2 == 6:
        card2_display = card7
    elif card2 == 7:
        card2_display = card8
    elif card2 == 8:
        card2_display = card9
    elif card2 == 9:
        card2_display = card10
    elif card2 == 10:
        card2_display = card11
    elif card2 == 11:
        card2_display = card12
    elif card2 == 12:
        card2_display = card13
    elif card2 == 13:
        card2_display = card14

    card2_label.config(image=card2_display)
    return card2

card2 = PhotoImage(file = "2.png").subsample(16)
card3 = PhotoImage(file = "3.png").subsample(16)
card4 = PhotoImage(file = "4.png").subsample(16)
card5 = PhotoImage(file = "5.png").subsample(16)
card6 = PhotoImage(file = "6.png").subsample(16)
card7 = PhotoImage(file = "7.png").subsample(16)
card8 = PhotoImage(file = "8.png").subsample(16)
card9 = PhotoImage(file = "9.png").subsample(16)
card10 = PhotoImage(file = "10.png").subsample(16)
card11 = PhotoImage(file = "11.png").subsample(16)
card12 = PhotoImage(file = "12.png").subsample(16)
card13 = PhotoImage(file = "13.png").subsample(16)
card14 = PhotoImage(file = "14.png").subsample(16)

# Generate the initial pair of cards
next_card()

window.mainloop()
