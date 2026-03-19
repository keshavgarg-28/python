try:
    x=int(input())
    print(10/x)
except ValueError as e:
    print(e)
finally:
    print("Success")