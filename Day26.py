import random
import pandas
numbers = [1,2,3]
#[newitem for item in list]
new = [n+1 for n in numbers]
print(new)

name = "Dhanya"
letter = [letter for letter in name]
print(letter)

n = [2*i for i in range(5)]
print(n)

names = ["Alex","barley","Caroline","Gary","Ash"]
li =  [word for word in names if len(word)<5 ]
print(li)

cap = [word.upper() for word in names if len(word)>4]
print(cap)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(i) for i in list_of_strings]
result = [i for i in numbers if i%2==0]
print(result)
#
# with open ("file1.txt") as file1:
#     with open ("file2.txt") as file2:
#
#         result = [int(i) for i in file2 and file1]
#
# print(result)

dict = { item:random.randint(1,100) for item in names}
print(dict)

passes = {item:value for (item,value) in dict.items() if value>60}
print(passes)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence=sentence.split()
result = { word:len(word) for word in sentence}

res = {
    "stu":["Dhanya","Raahul"],
    "age":[20,21]
}
print(res)

df = pandas.DataFrame(res)

for (key,value) in df.items():
    print(value)

for (index,row) in df.iterrows():
    print(row)