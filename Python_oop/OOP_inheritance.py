class Animal():
    def __init__(self) -> None:
        print("Animal Created")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        # Animal.__init__(self)
        print("Dog Created")
    
    def speak(self):
        print("Woof!")


class Cat (Animal):
    def __init__(self):
        super().__init__()
        # Animal.__init__(self)
        print("Cat Created")
    
    def speak(self):
        print("Meow!")



d = Cat()
d.eat()
d.speak()