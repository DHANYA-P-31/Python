from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)
    password_list=[]
    for letter in range(0,nr_letters):
        password_list.append(random.choice(letters))
    for symbol in range(0,nr_symbols):
        password_list.append(random.choice(symbols))
    for num in range(0,nr_numbers):
        password_list.append(random.choice(numbers))
    random.shuffle(password_list)
    result="".join(password_list)
    input3.delete(0, END)
    input3.insert(0,result)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input1.get()
    user = input2.get()
    password = input3.get()
    details = {
        website:{
            "email":user,
            "password": password
        }
    }
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Don't let anything empty")
    isok = messagebox.askokcancel(title=website,message=f"Username:{user}\npassword:{password}")

    if isok:
        try:
            with open("pass.json","r") as file:
                data = json.load(file)
                data.update(details)
        except FileNotFoundError:
            with open("pass.json", "w") as file:
                json.dump(details, file, indent=4)
        else:
            with open("pass.json","w") as file:
                json.dump(data,file,indent=4)
        finally:
            input1.delete(0,END)
            input3.delete(0,END)

def search():
    try:
        with open("pass.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="Some error")
    else:
        website = input1.get()
        try:
            messagebox.askokcancel(title=website, message=f"Username:{data[website]["email"]}\npassword:{data[website]["password"]}")
        except KeyError:
            messagebox.showinfo(title="Oops", message="Website not found")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.config(padx=50,pady=50)

img = PhotoImage(file="logo.png")
canvas = Canvas(width = 200,height = 200)
canvas.create_image(100,100 , image = img)
canvas.grid(row = 0, column = 1)

label = Label(text="Website:")
label.grid(row = 1, column = 0)

label2 = Label(text = "Email/Username:")
label2.grid(row = 2, column = 0)

label3 = Label(text="Password:")
label3.grid(row = 3, column = 0)

input1 =Entry(width=30)
input1.focus()
input1.grid(row = 1, column = 1)

input2 = Entry(width=50)
input2.insert(0,"abc@gmail.com")
input2.grid(row = 2, column = 1,columnspan = 2)

input3 = Entry( width=30)
input3.grid(row = 3, column = 1)

button = Button(text = "Search",command= search,width=15)
button.grid(row = 1, column = 2)

button1 = Button(text = "Generate Password",command=generate)
button1.grid(row = 3, column = 2)

button2 = Button(text = "Add",width=42,command=save)
button2.grid(row = 4, column = 1,columnspan = 2)

window.mainloop()