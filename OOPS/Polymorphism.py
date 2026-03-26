## Method Overriding
class Animal:
    def speak(self):
        print("Animal speaks.")
class Dog(Animal):
    def speak(self):
        print("Dog Barks")
d=Dog()
d.speak()

## Duck Typing
class Cat():
    def talk(self):
        print("Meow")
class Dog():
    def talk(self):
        print("Bark")
def get_sound(Animal):
    Animal.talk()
get_sound(Cat())
get_sound(Dog())

## Operator Overloading
print(5 + 3)        
print("a" + "b")  