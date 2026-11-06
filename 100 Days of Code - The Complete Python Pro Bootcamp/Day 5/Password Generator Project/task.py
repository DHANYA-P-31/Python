letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
import random
#import random module to select randomly
print("Welcome to the PyPassword Generator!")
#prompt to get inputs from user
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy level generators
#create an empty list
password_list=[]
#for number of letter generate the choices randomly from list letters
for letter in range(0,nr_letters):
    password_list.append(random.choice(letters))
#for number of symbols generate the choices randomly from list symbols
for symbol in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
# for number of numbers generate the choices randomly from list numbers
for num in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
print(password_list)
#shuffle the elements in original list it does not return anything
random.shuffle(password_list)
print(password_list)
result=""
#create a password string
for i in password_list:
    result+=i
print(f"The suggested password is:{result}")