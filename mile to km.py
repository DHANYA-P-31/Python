from tkinter import *

window = Tk()
window.minsize(250,100)
window.title("Mile to km convertor")
window.config(padx=15,pady=10)

input = Entry(width=15)
input.grid(row = 0, column = 1)

label1 = Label(text="Miles")
label1.grid(row = 0, column = 2)

label2 = Label(text="is equal to ")
label2.grid(row = 1, column = 0)

label3 = Label(text= 0)
label3.grid(row = 1, column = 1)

label4 = Label(text = "kilometers")
label4.grid(row = 1, column = 2)


def click():
    mile = int(input.get())
    km = round(mile * 1.609,2)
    label3.config(text=km)

button = Button(text="Calculate",command=click)
button.grid(row = 2,column = 1)

window.mainloop()
