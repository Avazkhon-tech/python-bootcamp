from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

# UI design
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
img_front = PhotoImage(file="images/card_front.png")
img_back = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=img_back)
canvas.create_image(400, 263, image=img_front)
canvas.grid(row=0, column=1)

canvas_wrong = Canvas(height=100, width=100, highlightthickness=0, bg=BACKGROUND_COLOR)
img_wrong = PhotoImage(file="images/wrong.png")
img_right = PhotoImage(file="images/right.png")
canvas_wrong.create_image(50, 50, image=img_wrong)
canvas_wrong.create_image(50, 50, image=img_right)
canvas_wrong.grid(row=1, column=1)







































window.mainloop()
