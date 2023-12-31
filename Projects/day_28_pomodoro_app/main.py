from tkinter import Tk, Canvas, PhotoImage, Label, Button
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
ticks = ''
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    label_timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    label_tick.config(text="")
    reps = 0# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    global ticks
    reps += 1
    if reps % 2 == 0 and reps % 8 != 0:
        count_down(SHORT_BREAK_MIN*60)
        label_timer.config(text="Break", fg=PINK)
    elif reps != 0 and reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        label_timer.config(text="Break", fg=RED)
    else:
        label_timer.config(text="Work", fg=GREEN)
        count_down(WORK_MIN*60)
    if reps % 2 == 0:
        ticks += '✔'
        label_tick.config(text=ticks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minute = count//60
    second = count % 60
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)

window.title("Pomodoro")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

# labels
label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label_timer.grid(row=0, column=1)

label_tick = Label(bg=YELLOW, fg=GREEN)
label_tick.grid(row=3, column=1)

# buttons
button_start = Button(text="Start", highlightthickness=0, command=start_count)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(row=2, column=2)






















window.mainloop()