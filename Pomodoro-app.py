import tkinter
from tkinter import *
from tkinter import PhotoImage
from time import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
timer= NONE


window=Tk()
window.title("pomodoro")
window.config(padx=100, pady=100, bg= YELLOW)
canvas= Canvas(width=200,height=224, bg= YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)
png= PhotoImage(file="tomato.png")
canvas.create_image(100,112, image =png)
time_label= canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
title_label= tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW,font=(FONT_NAME, 35, "bold") )
title_label.grid(column=1, row=0)
reps=0
text_tik=""
#---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(time_label, text=f"00:00")
    title_label.config(text="Timer", fg=GREEN)
    reps = 0
    tik_label.config(text= "")





def start_timer():
    global reps
    reps += 1

    if reps % 8==0:
        countdown(LONG_BREAK_MIN*60)
        title_label.config(text= "Break", fg = RED)
    elif reps % 2==0:
        countdown(SHORT_BREAK_MIN*60)
        title_label.config(text= "Break", fg = PINK)
    else:
        countdown(WORK_MIN*60)
        title_label.config(text= "Work", fg = GREEN)


# TIMER MECHANISM#
def countdown(count):
    global reps
    global text_tik
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(time_label, text=f"{minutes:02d}:{seconds:02d}")
    if (count > 0):
       global timer
       timer= window.after(1000, countdown, count-1)
    else:
       start_timer()
       if reps % 2 ==0:
           text_tik += "\u2714\uFE0F"
           tik_label.config(text=text_tik)



button2= Button(window, text="START",fg= "black", command=start_timer, font=(FONT_NAME, 9, "bold"),highlightthickness=0)
button2.grid(column=0, row=2)
button= Button(window, text="RESET", fg= "black", command= reset_timer, font=(FONT_NAME, 9, "bold"), highlightthickness=0)
button.grid(column=2, row=2)
tik_label = tkinter.Label(text=text_tik, fg=GREEN, bg=YELLOW)
tik_label.grid(column=1, row=2)

window.mainloop()