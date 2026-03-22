def counter(n):
    i=1
    while i<=n:
        yield i
        i+=1
g=counter(5)
for i in g:
    print(i)