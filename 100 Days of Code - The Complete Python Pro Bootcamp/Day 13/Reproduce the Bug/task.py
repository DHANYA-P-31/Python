from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])
#initrially the ranges is from 1 to 6 so there is index out of bounds
#We could modify it by change it from 0 to 5
