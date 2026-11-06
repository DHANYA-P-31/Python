rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
list_1=[rock,paper,scissors]
choice=int(input("What is your choice?Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("You choose:")
print(list_1[choice])
print("Computer chooses:")
com=random.randint(0,2)
print(list_1[com])
if (com==0 and choice==1) or (com==1 and choice==2) or (com==2 and choice==0):
    print("YOU WON")
elif com==choice:
    print("DRAW")
else:
    print("You Lose")