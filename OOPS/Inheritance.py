class Animal:
    def walks(self):
        print("Walking")
class Dog(Animal):
    def sound(self):
        print("Barks")
d=Dog()
d.walks()
d.sound()