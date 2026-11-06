# import csv
#
# # with open("weather_data.csv") as file:
# #     temperature = []
# #     for data in csv.reader(file):
# #         if data[1]!= "temp":
# #             temperature.append(int(data[1]))
# #     print(temperature)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data[data["day"]== "Monday"])
# print(data[data.temp==data.temp.max()].temp)

# import pandas
#
# dict = {
#     "students":["Dhanya","Raahul"],
#     "age":[20,21]
# }
#
# df = pandas.DataFrame(dict)
# print(df)

# import pandas
#
# df=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# gray = len(df[df["Primary Fur Color"] == "Gray"])
# black = len(df[df["Primary Fur Color"] == "Black"])
# cinnamon = len(df[df["Primary Fur Color"] == "Cinnamon"])
# dict = {
#     "color": ["Gray","Black","Cinnamon"],
#     "number": [gray,black,cinnamon]
# }
#
# data = pandas.DataFrame(dict)
# data.to_csv("squirrel.csv")
# print(data)

import turtle
import pandas

list = []
screen = turtle.Screen()
screen.title("USA States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.tracer(0)

data = pandas.read_csv("50_states.csv")
while len(list)<50:
    screen.update()
    answer = screen.textinput(f"{len(list)}/50","What is the state name:")
    answer = answer.title()
    states = data["state"].tolist()
    if answer == "Exit":
        list2=[i for i in states if i not in list]
        missing = pandas.DataFrame(list2)
        missing.to_csv("missing.csv")
        break
    if answer in states:
        if answer not in list:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            x = int(data[data["state"] == answer].x)
            y = int(data[data["state"] == answer].y)
            t.setpos(x,y)
            t.write(answer,False,"left",("Arial",8,"normal"))
            list.append(answer)
