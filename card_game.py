from tkinter import *
import pygame
import random
import sys
 

# Initialize Tkinter
window = Tk()
window.title("Higher-Lower-Same Guessing Game")
window.geometry("1003x800")

# Load the image
background_image = PhotoImage(file="bg_image.png")
background_image = background_image.subsample(2)  # Adjust scaling if needed

window.mainloop