class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal")

    def speak(self):
        print("This is an animal speaking.")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Cat")

    def speak(self):
        print("The cat is meowing.")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Dog")

    def speak(self):
        print("The dog is barking.")


class CatDog(Cat, Dog):
    def __init__(self, name):
        super().__init__(name)
        print("CatDog")

    def speak(self):
        print("The CatDog is 汪汪汪")


print(CatDog.mro())

cat_dog = CatDog("猫狗")
cat_dog.speak()

"""
CatDog.__init__
    └── Cat.__init__
        └── Animal.__init__  # Prints "Animal"
    └── Dog.__init__         # Prints "Dog"
    └── Cat.__init__        # Prints "Cat"
    └── CatDog.__init__     # Prints "CatDog"
"""
