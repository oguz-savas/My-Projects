
class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print("Making sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def make_sound(self):
        print("woof")
    def fetch(self):
        print("Dog is fetching")
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def make_sound(self):
        print("meow")
    def climb(self):
        print("Cat is climbing")

dog = Dog("Dog", "Dog")
cat = Cat("Cat", "Cat")
dog.make_sound()
cat.make_sound()

