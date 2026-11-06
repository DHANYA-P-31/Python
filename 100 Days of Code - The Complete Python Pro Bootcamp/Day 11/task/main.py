from art import logo
import random
def draw_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Return 0 if blackjack or else return the sum of cards"""
    if sum(cards)==21 and len(cards)==0:
        return 0

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(score1,score2):
    """Compare the scores and determine winner"""
    if score1==score2:
        print("Draw")
    elif score2==0:
        print("Computer won by blackjack")
    elif score1==0:
        print("You won by blackjack")
    elif score1>21:
        print("You lose")
    elif score2>21:
        print("You won")
    elif score1<score2:
        print("You lose")
    else:
        print("You Won")

start = input("Do you want to play Blackjack?'y' or 'n'").lower()
while start == 'y':
    game = True
    print(logo)
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(draw_card())
        computer_cards.append(draw_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards {user_cards} ,score is {user_score}")
    print(f"Computer's first card is {computer_cards[0]}")

    while game:
        if computer_score==0 or user_score==0 or user_score>21:
            game = False
        else:
            deal = input(f"Do you want to draw a card your cards {user_cards} ,sum is {calculate_score(user_cards)}").lower()
            if deal=='y':
                user_cards.append(draw_card())
            else:
                game = False

    while computer_score != 0 and computer_score<17:
        computer_cards.append(draw_card())
        computer_score=calculate_score(computer_cards)

    print(f"Computer cards {computer_cards} ,score is {computer_score}")

    compare(user_score,computer_score)
    start = input("Do you want to play Blackjack?'y' or 'n'").lower()
    print("\n"*20)
