from tkinter import PhotoImage
from tkinter import  *
import random
import pandas
import time
BACKGROUND_COLOR = "#B1DDC6"
row = {}
to_learn  = {}

try:
    DataFrame=pandas.read_csv("data/words.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/hindiwords.csv")
    dict = data.to_dict(orient="records")
else:
    dict = DataFrame.to_dict(orient="records")



def display():
    global row
    row = random.choice(dict)
    canvas.itemconfig(img,image = CARDFRONT)
    canvas.itemconfig(lang,text="Hindi",fill = "black")
    canvas.itemconfig(text,text=row["Hindi"],fill = "black")
    timer = window.after(3000, answer)

def answer():
    canvas.itemconfig(img, image=CARDBACK)
    canvas.itemconfig(lang, text="English",fill = "white")
    canvas.itemconfig(text, text=row["English"],fill = "white")

def known():
    dict.remove(row)
    data = pandas.DataFrame(dict)
    data.to_csv("data/words.csv",index = False)

    display()
window = Tk()
window.title("Learn Hindi")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

CARDFRONT = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
img = canvas.create_image(400,263,image = CARDFRONT)
CARDBACK = PhotoImage(file = "images/card_back.png")
lang = canvas.create_text(400,150,text="Hindi", font = ("Ariel",40,"normal"))
text = canvas.create_text(400,290, font = ("Ariel",56,"bold"))
canvas.grid(row = 0, column = 0,columnspan = 2)

WRONG = PhotoImage(file  = "images/wrong.png")
button1 = Button(image=WRONG,highlightthickness=0,command=display)
button1.grid(row = 1, column = 0)

RIGHT = PhotoImage(file  = "images/right.png")
button1 = Button(image=RIGHT,highlightthickness=0,command=known)
button1.grid(row = 1, column = 1)

display()

window.mainloop()