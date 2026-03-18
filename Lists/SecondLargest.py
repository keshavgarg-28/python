list=[10,5,8]
max=0
s_max=0
for i in list:
    if i>max:
        s_max=max
        max=i
    elif i>s_max and i!=max:
        s_max=i
print(s_max)

