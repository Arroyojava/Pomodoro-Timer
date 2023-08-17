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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
# Window Config
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas / Background
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Label
timer_label = Label(text='Timer', font=(FONT_NAME, 50, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

check_label = Label(text='✔', font=(FONT_NAME, 20), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

# Buttons
start_button = Button(text='Start', font=(FONT_NAME, 12), bg=YELLOW, fg=RED)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', font=(FONT_NAME, 12), bg=YELLOW, fg=RED)
reset_button.grid(column=2, row=2)

window.eval('tk::PlaceWindow . Center')
window.mainloop()
