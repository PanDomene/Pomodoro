from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
CHECK = ""
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global CHECK
    global reps
    reps = 1
    CHECK = ""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text=CHECK)
    title.config(text="Timer", fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global CHECK
    if reps % 2:
        countdown(WORK_MIN)
        title.config(text="Work", fg=GREEN)
    elif not reps % 8:
        CHECK += "✔"
        check_marks.config(text=CHECK)
        countdown(LONG_BREAK_MIN)
        title.config(text="Break", fg=RED)
    else:
        countdown(SHORT_BREAK_MIN)
        title.config(text="Break", fg=PINK)
        CHECK += "✔"
        check_marks.config(text=CHECK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps
    global timer
    if count >= 0:
        minutes = count // 60
        seconds = count % 60
        canvas.itemconfig(timer_text, text="{:02}:{:02}".format(minutes, seconds))
        timer = window.after(1000, countdown, count - 1)
    else:
        reps += 1
        window.lift()
        window.attributes('-topmost', True)
        window.after_idle(window.attributes, '-topmost', False)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

title = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title.grid(row=0, column=1)

start = Button(text="Start", font=(FONT_NAME, 13), highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", font=(FONT_NAME, 13), highlightthickness=0, command=reset)
reset.grid(row=2, column=2)

check_marks = Label(text=CHECK, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, ""))
check_marks.grid(row=3, column=1)

window.mainloop()
