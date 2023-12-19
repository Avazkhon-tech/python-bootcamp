from tkinter import *


def calculate_on_click():
    miles = float(user_input.get())
    km = miles * 1.609
    km = round(km)
    label_4.config(text=km)


window = Tk()
window.title("Mile to Km converter")
window.minsize(250, 100)
window.config(padx=40, pady=40)

"""labels"""
label_pad_x = 5
label_pad_y = 5
label_1 = Label(text="is equal to")
label_1.grid(row=1, column=0)
label_1.config(padx=label_pad_x, pady=label_pad_y)

label_3 = Label(text="Miles")
label_3.grid(row=0, column=2)
label_3.config(padx=label_pad_x, pady=label_pad_y)

label_4 = Label(text="0")
label_4.grid(row=1, column=1)
label_4.config(padx=label_pad_x, pady=label_pad_y)

label_5 = Label(text="Km")
label_5.grid(row=1, column=2)
label_5.config(padx=label_pad_x, pady=label_pad_y)

"""Buttons"""
button = Button(text="Calculate", command=calculate_on_click)
button.grid(row=2, column=1)

"""inputs"""
user_input = Entry(width=10)
user_input.grid(row=0, column=1)

































window.mainloop()