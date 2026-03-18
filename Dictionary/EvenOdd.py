
list=[1,2,3,4,5,6,7,8]
res={}
for i in list:
    if i%2==0:
        res[i]="even"
    else:
        res[i]="odd"
print(res)