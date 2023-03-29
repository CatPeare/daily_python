'''super() is a built-in Python function that allows you to call a method in a parent class from a subclass. 
It is used to enable inheritance and method overriding.'''
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "meow")

    def speak(self):
        super().speak()
        print("purr")

my_cat = Cat("Fluffy")
my_cat.speak()   # Output: Fluffy says meow \n purr

# another example
class Parent:
    def __init__(self):
        self.parent_attribute = 'Hello from Parent'
        
    def greeting(self):
        print(self.parent_attribute)

class Child(Parent):
    def __init__(self):
        super().__init__() # calls Parent's __init__()
        self.child_attribute = 'Hello from Child'

    def greeting(self):
        super().greeting() # calls Parent's greeting()
        print(self.child_attribute)

c = Child()
c.greeting() # Output: Hello from Parent
            #         Hello from Child
