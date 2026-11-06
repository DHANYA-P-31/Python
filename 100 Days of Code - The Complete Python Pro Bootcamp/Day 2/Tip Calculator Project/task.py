print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_amount=tip*bill/100
Total = bill+tip_amount
split_up = round(Total/people,2)
print(f'Each person should pay: ${split_up}')
