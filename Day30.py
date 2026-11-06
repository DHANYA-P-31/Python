# try:
#     file = open("fikj.txt")
#     dict = {
#         "hello":8
#     }
#     print(dict["hello"])
# except FileNotFoundError:
#     file = open("fikj.txt","w")
#     file.write("something")
# except KeyError as error:
#     print(error)
# else:
#     message = file.read()
#     print(message)
# finally:
#     raise KeyError
