## Sum of elements
from functools import reduce
lst=[1,2,3,4,5]
result=reduce(lambda x,y: x+y, lst)
print(result)

## Sum of squares
lst=[1,2,3]
result=map(lambda x:x*x, lst)
finalresult=reduce(lambda x,y:x+y, result)
print(finalresult)
