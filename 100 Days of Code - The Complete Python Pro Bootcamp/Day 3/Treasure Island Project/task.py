print(r'''
______.........--=T=--.........______
      .             |:|
 :-. //           /""""""-.
 ': '-._____..--""(""""""()`---.__
  /:   _..__   ''  ":""""'[] |""`\\
  ': :'     `-.     _:._     '"""" :
   ::          '--=:____:.___....-"
                     O"       O" grp
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first=input("Left or right")
if first=="left":
    second=input("swim or wait")
    if second=="wait":
        third=input("Blue or green or yellow")
        if third=="yellow":
            print("YOU WON")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")