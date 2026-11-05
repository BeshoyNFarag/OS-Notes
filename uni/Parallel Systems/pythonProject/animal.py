'''
 In a file named animal.py, implement a class named Animal with the instance variables name
(type str) and age (type int). Implement a constructor that initializes the name and age variables
with values passed as parameters to the constructor. Also, implement an instance method named
speak that outputs the string I am <NAME> and I am <AGE> years old. to the console. done


'''

class Animal:
    name: str
    age: int

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def speak(self):
        print(f"I am {self.name} and i'm {self.age}  years old")
