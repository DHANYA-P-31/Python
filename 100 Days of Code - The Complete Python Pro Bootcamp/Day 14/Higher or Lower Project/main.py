import random
import art
from game_data import data

score = 0
game_over= False
A = random.choice(data)

while not game_over:
    B = random.choice(data)
    while A == B:
        B = random.choice(data)
    print(art.logo)
    print(f"Score:{score}")
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(art.vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    Ans = input("Who has more followers on Instagram? 'A' or 'B' : ").upper()
    if A['follower_count']>B['follower_count']:
        Correct = 'A'
    else:
        Correct = 'B'
    if Ans == Correct:
        score+=1
        print(f"You are Right")
    else:
        game_over = True
    print("\n"*20)
    A = B

print(art.logo)
print("OOPS! Your answer is wrong")
print(f"Your final score : {score}")
