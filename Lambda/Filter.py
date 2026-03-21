## No. greater than 5
lst=[2,4,3,7,8,1]
result=filter(lambda x: x>5, lst)
print(list(result))

## Odd Numbers
result=filter(lambda x: x%2!=0, lst)
print(list(result))

## length greater than 3
names = ["hi", "hello", "hey", "python"]
result=filter(lambda x:  len(x)>3, names)
print(list(result))