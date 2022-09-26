class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Fish(Animal):
    def Swim(self):
        print("swim")


class Mammal(Animal):
    def walk(self):
        print("walk")


Elephant = Mammal()
Elephant.eat()
Elephant.walk()
print(Elephant.age)

fish = Fish()
fish.Swim()
