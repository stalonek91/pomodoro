import tkinter as tk
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    timer_label["text"] = "Timer"
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    resp = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label["text"] = "Break"
        timer_label["fg"] = RED
        start_counter(long_break_sec)
    elif reps % 2 == 0:
        timer_label["text"] = "Break"
        timer_label["fg"] = PINK
        start_counter(short_break_sec)
    else:
        timer_label["text"] = "Work"
        start_counter(work_sec)



        


    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def start_counter(count):


    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f" {count_min}:{count_sec}")

    if count > 0:

        global timer
        timer = window.after(1000, start_counter, count -1 )

    else:
        start_timer()
        if reps % 2 == 0:

            old_checkmark_value = checkmark_label["text"]
            new_checkmark_value = old_checkmark_value + "✅"
            checkmark_label.config(text=new_checkmark_value)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomidorror')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)



image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))



checkmark_label = Label(background=YELLOW)
checkmark_label.grid(column=1, row=3)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

stop_button = Button(text="Stop", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
stop_button.grid(column=2, row=2)



# ✅

# button_start = tk.Button()
# button_start.grid(column= 0, row=3)

# button_stop = tk.Button()
# button_stop.grid(column= 3, row=3)


window.mainloop()