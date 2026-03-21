def print_n(x):
    if x==0:
        return
    print_n(x-1)
    print(x)

print_n(5)