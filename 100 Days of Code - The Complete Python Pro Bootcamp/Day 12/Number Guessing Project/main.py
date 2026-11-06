import art
import random

game = input("Do you want to play the number guessing game 'y' or 'n'")

while game=='y':
    print(art.logo)
    num = random.randint(1,101)
    print("I have thought a number between 1 to 100")
    diff = input("Could you guess(Choose difficulty:'easy' or 'hard')").lower()
    ran = 0
    if diff == "easy":
        ran = 10
    elif diff == "hard":
        ran = 5
    for i in range(ran):
        print(f"You have {ran-i} attempts remaining")
        guess = int(input("Guess a Number:"))
        if guess<num:
            print("Too Low")
            print("Try again")
        elif guess>num:
            print("Too High")
            print("Try again")
        else:
            print("You won You guessed the number correctly")
            break
    game = input("Do you want to play the number guessing game 'y' or 'n'")
    if game=='y':
        print("\n"*20)
