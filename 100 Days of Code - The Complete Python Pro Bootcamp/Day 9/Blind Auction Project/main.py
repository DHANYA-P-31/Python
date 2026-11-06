from art import logo
print(logo)
# TODO-1: Ask the user for input
while True:
    name=input("Enter your name:")
    price = int(input("Enter your bid price:"))
    # TODO-2: Save data into dictionary {name: price}
    dictionary = {}
    dictionary[name]=price
    # TODO-3: Whether if new bids need to be added
    new_bid = input("Are there any other bidders:(yes or no)").lower()
    if new_bid=="no":
        break
    print("\n" * 20)

# TODO-4: Compare bids in dictionary
max_bid = 0
winner=""
for key in dictionary:
    if dictionary[key]>max_bid:
        max_bid=dictionary[key]
        winner = key

print(f"{winner} won the bid with price {max_bid}")
