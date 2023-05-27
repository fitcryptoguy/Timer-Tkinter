# This is a sample Python script.
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
time_to_be_passed = 0
rep = 0
window_running = None



# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep
    rep = rep + 1
    if rep % 8 == 0:
        seconds = 20 * 60
        heading_label.config(text="Break")

    elif rep % 2 != 0:
        seconds = 25 * 60
        heading_label.config(text="Work")


    elif rep % 2 == 0:
        seconds = 5 * 60
        heading_label.config(text="Break")

    counter(seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def counter(seconds):
    global window_running
    time_minutes = math.floor(seconds / 60)
    time_seconds = seconds % 60

    if seconds > 0:
        canvas.itemconfig(canva_text, text=f"{time_minutes}:{time_seconds}")
        canvas_text = canvas.itemcget(canva_text, 'text')
        seconds = seconds - 1
        window_running = window.after(1000, counter, seconds)

    else:
        start_timer()
        marks = " "
        for i in range(math.floor(rep / 2)):
            marks = marks + "✔"

        checkmark.config(text=marks)


def reset_game():
    window.after_cancel(window_running)
    heading_label.config(text="timer")
    canvas.itemconfig(canva_text, text="00:00")


# ---------------------------- UI SETUP -------------------------------
window = Tk()
window.title("pomodoro timer")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=220, height=233, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 115, image=tomato_img)
canva_text = canvas.create_text(113, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

heading_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 45, "bold"), bg=YELLOW)
heading_label.grid(column=2, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_game)
reset_button.grid(column=3, row=3)

checkmark = Label(fg=GREEN, bg="white")
checkmark.grid(column=2, row=4)

window.mainloop()
