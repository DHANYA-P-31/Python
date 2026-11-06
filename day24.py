with open("my.txt","a") as file:
    file.write("Hello")

with open("my.txt") as file:
    message = file.read()
    print(message)