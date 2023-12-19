from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = user_input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("my first GUI Program")
window.minsize(width=600, height=500)
window.config(padx=100, pady=200)

# layout managers: pack, place, grid
'''Label'''
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

'''Button'''
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button_2 = Button(text="New button", command=button_clicked)
button_2.grid(column=2, row=0)

'''Entry'''
user_input = Entry(width=10)
user_input.grid(column=3, row=3)

import tkinter

window = tkinter.Tk()
window.title("my first GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")









































window.mainloop()