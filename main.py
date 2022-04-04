from tkinter import *
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
count_down_time = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_button():
    canvas.itemconfig(timer_text, text='00:00')
    window.after_cancel(count_down_time)
    timer.config(text='Timer')
    check_marks.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_button():  # function for the count button
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_secs)
        timer.config(text='Work', fg=GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_secs)
        timer.config(text='Break', fg=PINK)
    elif reps == 8:
        count_down(long_break_secs)
        timer.config(text='Break', fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import math
def count_down(count):  # to make the items on the canvas change at the push of a button since the mainloop is always listening for events.

    count_min = math.floor(count / 60)
    count_secs = count % 60
    if count_secs == 0:
        count_secs = '00'
    elif count_secs < 10:
        count_secs = f'0{count_secs}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_secs}')
    if count > 0:
        global count_down_time
        count_down_time = window.after(1000, count_down, count-1)
    else:
        start_button()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✓'

        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')  # how to use image on a canvas
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

canvas.grid(column=1, row=1)



start = Button(text='start', command=start_button, bg=YELLOW, highlightthickness=0)
start.grid(column=0, row=2)

timer = Label(text='Timer', fg=GREEN, font= (FONT_NAME, 34, 'bold'), bg=YELLOW)
timer.grid(column=1, row=0)




reset = Button(text='Reset', command=reset_button, bg=YELLOW, highlightthickness=0)
reset.grid(column=2, row=2)

check_marks = Label(font=(FONT_NAME, 15), fg=GREEN)
check_marks.grid(column=1, row=3)


window.mainloop()