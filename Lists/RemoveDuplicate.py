list=[1,2,3,2,1,3,4,5,6,7,8]
result=[]
for i in list:
    if i not in result:
        result.append(i)
print(result)