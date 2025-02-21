from tkinter import *
import pandas as pd
import random

# Background_color
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}

# Handles FileNotFoundError if words_to_learn.csv doesn't exists yet
try:
    data = pd.read_csv(
        "./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv(
        "./data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    '''Pulls out the next card to learn'''
    global current_word, timer
    # window.after_cancel(timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_word, text=current_word['French'], fill='black')
    canvas.itemconfig(card_title, text="French", fill='black')
    timer = window.after(3000, flip_card)


def flip_card():
    '''Flips the card for the user to check if right or wrong'''
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_word['English'], fill='white')
    window.after_cancel(timer)


def is_known():
    '''Check if the french word is known by the user and remove it to avoid the word popping up again'''
    to_learn.remove(current_word)
    data = pd.DataFrame(to_learn)
    data.to_csv(
        './data/words_to_learn.csv', index=False)
    next_card()


# Window set-up
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flip_timer
timer = window.after(3000, func=flip_card)

# Canvas set-up
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(
    file="./images/card_front.png")
card_back_image = PhotoImage(
    file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Wrong Button set-up
wrong_image = PhotoImage(
    file="./images/wrong.png")
wrong_button = Button(
    image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# Right Button set-up
right_image = PhotoImage(
    file="./images/right.png")
right_button = Button(
    image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

# Func call to display the current word unto the screen
next_card()


window.mainloop()
