def Count(str):
    c=0
    s="aeiouAEIOU"
    for i in str:
        if i in s:
            c+=1
    
    return c
print(Count("qweqweqwe"))