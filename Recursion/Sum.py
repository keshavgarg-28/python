def sumdigits(x):
    if x==0:
        return 0
    return x%10 + sumdigits(x//10)
print(sumdigits(123132))