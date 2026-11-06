import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(500,300)
window.config(padx=20,pady =20)

label = tkinter.Label(text="I am a Label",font=("Arial",24,"bold"))
label.place(x=0,y=0)

input = tkinter.Entry(width = 30)
input.pack()
input.insert(tkinter.END, string="Some text to begin with.")

box = tkinter.Spinbox(from_=0,to=10,width=5)
box.pack()

scale = tkinter.Scale(from_=0,to=100)
scale.pack()

checkbutton = tkinter.Checkbutton(text = "Is on", variable=tkinter.IntVar())
checkbutton.pack()

radioState = tkinter.IntVar()
radio = tkinter.Radiobutton(text = "option 1", value=1, variable=radioState)
radio2 = tkinter.Radiobutton(text = "option 2", value=2, variable=radioState)
radio.pack()
radio2.pack()

def click():
    label["text"] = input.get()
    label.config(text = text.get("1.0",tkinter.END))

text = tkinter.Text(height=5,width = 30)
text.focus()
text.insert(tkinter.END, "Some text to begin with.")
text.pack()

button = tkinter.Button(text = "Button",command=click)
button.pack()

def listbox_used(event):
    label["text"]=(listBox.get(listBox.curselection()))

listBox = tkinter.Listbox(height=4)
list = ["l1","l2","l3","l4"]
for l in list:
    listBox.insert(list.index(l),l)
listBox.pack()
listBox.bind("<<ListboxSelect>>",listbox_used)

#pack - not precise positioning just left right center
#place - precise positioning x and y coordinates
#grid - uses column and rows grid and pack cannot be in same program, starts from 0

window.mainloop()

#Many arguments example
# def add(*args): #Creates tuple
#     total = 0
#     for i in args:
#         total += i
#     return  total
#
# ans = add(1,5,1,8,2,3)
# print(ans)

#Key word arguments example

# def calculate(n,**kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(3,add=5,multiply=8)

# class Hello:
#
#     def __init__(self,**kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#         self.color = kwargs.get("color")
#
# h1 = Hello(make = "Maruti", model= "Suzuki")
# print(h1.make,h1.model,h1.color)