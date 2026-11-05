'''
In a file named giraffe.py, implement a class named Giraffe that inherits from the class
Animal. The constructor should take the parameters name (str), age (int), and height (float).
The constructor should first call the constructor from the class Animal to initialize the attributes
name and age and then initialize the instance variable height. Also, override the speak method
in a way that first the output of the class Animal appears and afterwards the string I am a
giraffe, my height is <HEIGHT> meters..
'''
from animal import Animal


class Giraffe(Animal):
    height: float

    def __init__(self, name, age, height):
        Animal.__init__(self,name , age)
        self.height = height


    def speak(self):
        Animal.speak(self)
        print(f"I am a giraffe, my height is {self.height} meters")

