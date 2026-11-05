'''
k) Write a main method proofing that all of the previous implemente

'''
from typing import Union

from animal import Animal
from giraffe import Giraffe
from pig import Pig

number_of_animals = 0


def createGiraffe(name: str, age: int, height: float) -> Giraffe:
    global number_of_animals
    giraffe = Giraffe(name, age, height)
    number_of_animals += 1
    return giraffe


def createPig(name: str, age: int, weight: float) -> Pig:
    global number_of_animals
    pig = Pig(name, age, weight)
    number_of_animals += 1
    return pig


def readPigFromFile(path: str) -> list[Pig]:
    pigs = []
    global number_of_animals

    with open(path, "r") as file:
        for line in file:
            name, age, weight = line.split(",")

            name = name.strip()
            age = int(age.strip())
            weight = float(weight.strip())

            pig = Pig(name, age, weight)
            pigs.append(pig)
            number_of_animals += 1

    return pigs


def returnAnimalWithName(animals: list[Animal], name: str) -> str:
    for animal in animals:
        if animal.name == name:
            return name
    return None


def getAnimalsOderThan(animals: list[Animal], age: Union[str, int]) -> list[Animal]:
    animalsOlder = []
    if type(age) != int:
        age = int(age)

    for animal in animals:
        if animal.age > age:
            animalsOlder.append(animal)
        else:
            continue

    return animalsOlder

if __name__ == "__main__":

    # Create animals
    g1 = createGiraffe("Gary", 5, 3.2)
    p1 = createPig("Porky", 4, 120.5)
    p2 = createPig("Babe", 6, 98.3)

    # Store in list
    animals = [g1, p1, p2]

    # Test returnAnimalWithName
    found = returnAnimalWithName(animals, "Babe")
    print("Found animal:", found)

    # Test getAnimalsOlderThan
    older = getAnimalsOderThan(animals, 5)
    print("Animals older than 5:")
    for a in older:
        print(a.name, a.age)

    # Test file reading (if file exists)
    pigs_from_file = readPigFromFile("pigs.data")
    print("Pigs from file:")
    for p in pigs_from_file:
        print(p.name, p.age, p.weight)

    # Global counter check
    print("Total animals created:", number_of_animals)
