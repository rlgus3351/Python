from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF8B8B"
RED = "#EB4747"
BLUE = "#ABC9FF"
YELLOW = "#FAEA48"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# text = "✔"
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Title")
    check_marks.config(text = "")
    global reps
    resp = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 ==0:
        count_down(long_break_sec)
        title_label.config(text = "Break", fg = RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text = "Break", fg = YELLOW)
    else:
        count_down(work_sec)
        title_label.config(text = "work", fg = BLUE)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text =f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg = PINK)

canvas = Canvas(width=200, height= 224, bg = PINK, highlightthickness= 0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(103, 132, text = "00:00", fill= "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row = 1)

title_label = Label(text= "Timer", fg = BLUE, bg = PINK, font =(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row = 0)

start = Button(text= "Start", highlightthickness= 0, command=start_timer)
start.grid(column=0, row = 2)

Reset = Button(text= "Reset", highlightthickness= 0, command = reset_timer)
Reset.grid(column=2, row = 2)

check = Label(fg = BLUE, bg = PINK, font =(FONT_NAME, 15, "bold"))
check.grid(column=1, row = 3)


window.mainloop()


