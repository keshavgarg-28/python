## Double every element
lst=[1,2,3,4]
result=map(lambda x:x*2, lst)
print(list(result))


## Square of every element
result=map(lambda x:x*x, lst)
print(list(result))

## Convert to Upper Case
names = ["ram", "shyam", "hari"]
result=map(lambda x: x.upper(), names)
print(list(result))