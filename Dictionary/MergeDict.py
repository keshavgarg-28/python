d1 = {"a":1, "b":2}
d2 = {"b":3, "c":4}
for k,v in d2.items():
    if k in d1:
        d1[k]+=v
    else:
        d1[k]=v 
print(d1)