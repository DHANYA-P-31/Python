from  art import  logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

calculate = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}
continue_or_not = 'n'
while True:
    num1 = int(input("Enter first number:"))
    operation = input("Enter the operator ('+' or '-' or '*' or '/')")
    num2 = int(input("Enter Second number:"))
    result = calculate[operation](num1, num2)
    continue_or_not = input(f"Enter 'y' to continue with result {result} or enter 'n' to new calculation:").lower()
    while continue_or_not == 'y':
        operation=input("Enter the operator ('+' or '-' or '*' or '/')")
        num2 = int(input("Enter Second number:"))
        result = calculate[operation](result,num2)
        continue_or_not = input(f"Enter 'y' to continue with result {result} or enter 'n' to new calculation:").lower()
    print(f"The result is {result}")
    if continue_or_not == "n":
        print("\n"*20)
    elif not continue_or_not == "y":
        break


