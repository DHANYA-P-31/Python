class Car:
    def __init__(self, name):#This is a constructor,name is a constructor parameter
        self.name = name#class attributes takes value of parameter
        self.seats = 4 #This is default attribute

    def seat(self,):#This is a function
        """Increases car seats by 1 whenever called"""
        self.seats +=1

car1 = Car("Maruti")#Pass the parameter
print(car1.name)

print(car1.seats)
car1.seat()#call the function for object
print(car1.seats)