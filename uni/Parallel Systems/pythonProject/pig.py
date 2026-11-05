'''
In a file named pig.py, implement a class named Pig that inherits from the class Animal. The
constructor should take the parameters name (str), age (int), and weight (float). The constructor
should first check whether the values of the parameters weight and age are greater than 0. If
not, raise an exception of type ValueError. If the values are valid, the constructor should call the
constructor from the class Animal to initialize the attributes name and age and then initialize the
instance variable weight. Also, override the speak method in a way that first the output of the
class Animal appears and afterwards the string I am a pig, my weight is <WEIGHT> kg..
'''
from animal import Animal


class Pig(Animal):

    weight : float

    def __init__(self, name, age, weight ):
        if age > 0:
            Animal.__init__(self, name, age)
        else:
            raise TypeError("Wrong data type or value age cannot be less than zero")
        if weight > 0:
            self.weight = weight
        else:
            raise TypeError("Wrong data type or value weight cannot be less than zero")


    def speak(self):
        Animal.speak(self)
        print(f"I am a pig, my weight is {self.weight} kg")