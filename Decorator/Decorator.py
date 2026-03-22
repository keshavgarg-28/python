def deco(func):
    def inner():
        print("Start")
        func()
        print("End")
    return inner

@deco
def hello():
    print("Hi")

hello()