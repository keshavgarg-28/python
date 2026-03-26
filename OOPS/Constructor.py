class Person:
    def __init__(self,name):
        print("Constructor called.")
        self.name=name
p1=Person("John")
print(p1.name)
