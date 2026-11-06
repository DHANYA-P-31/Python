# import turtle
#
# rocky = turtle.Turtle()
# print(rocky)
# rocky.shape("turtle")
# rocky.color("Red")
# rocky.forward(100)
#
# screen = turtle.Screen()
# print(screen.canvheight)
# screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon",["Pikachu","Infernape","Greninja","Lucario"])
table.add_column("Type",['Electric','Fire','Water','Fighting'])
table.align="l"
print(table)