from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#379B46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
i =0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps,i
    reps = 0
    i =0
    window.after_cancel(timer)
    label.config(text = "Timer", fg = GREEN)
    label2.config(text = "")
    canvas.itemconfig(text,text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps,i
    reps+=1

    if reps%2 == 0:
        i += 1
        label2.config(text = "✔"*i)

    if reps == 8:
        reps = 0
        count_down(LONG_BREAK_MIN*60)
        label.config(text = "Long Break",fg=RED)
    if reps in [1,3,5,7]:
        label.config(text="Working",fg = GREEN)
        count_down(WORK_MIN*60)
    if reps in [2,4,6]:
        label.config(text="Short Break", fg = PINK)
        count_down(SHORT_BREAK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = count//60
    if min<10:
        min = f"0{min}"
    sec = count%60
    if sec <10:
        sec = f"0{sec}"
    canvas.itemconfig(text,text = f"{min}:{sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")

window.config(padx = 100,pady=50,bg = YELLOW)
canvas = Canvas(width = 200,height = 224,bg=YELLOW,highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(100,112 , image = img)
text = canvas.create_text(100,135,text="00:00",fill = "white", font = (FONT_NAME,35,"bold"))
canvas.grid(row = 1, column = 1)

label = Label(text = "Timer", fg=GREEN,bg = YELLOW, font=("Times New Roman",50,"bold"))
label.grid(row = 0, column = 1)

label2 = Label(text = "",fg = GREEN,bg = YELLOW,font=("Times New Roman",30,"bold"))
label2.grid(row = 4, column = 1)

button1 = Button(text="Start",command=start_timer)
button1.grid(row = 3, column = 0)

button2 = Button(text="Reset",command = reset)
button2.grid(row = 3, column = 2)

window.mainloop()