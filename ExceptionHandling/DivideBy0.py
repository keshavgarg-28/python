try:
    x=int(input())
    print(10/x)
except:
    print("Division By 0")
else:
    print("Valid Operation")
finally:
    print("Success")