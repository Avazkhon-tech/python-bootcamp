from tkinter import *
import pandas
from random import *
BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv('data/french_words.csv')
current_num = None


def next_card():
    global current_num
    current_num = randint(0, 100)
    canvas.itemconfig(card_title, text="English", fill='black')
    canvas.itemconfig(card_word, text=f'{data['English'][current_num]}', fill='black')
    canvas.itemconfig(canvas_image, image=img_front)


def flip_card():
    global current_num
    canvas.itemconfig(card_title, text="French", fill='white')
    canvas.itemconfig(card_word, text=f'{data['French'][current_num]})', fill='white')
    canvas.itemconfig(canvas_image, image=img_back)

# UI design
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)

window.after(3000, func=flip_card)

img_front = PhotoImage(file="images/card_front.png")
img_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=img_front)
card_title = canvas.create_text(400, 150, text='', font=("Aerial", 40, 'italic'))
card_word = canvas.create_text(400, 262, text='', font=("Aerial", 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, background=BACKGROUND_COLOR, command=next_card)
right_button.grid(column=1, row=1)
next_card()

window.mainloop()
