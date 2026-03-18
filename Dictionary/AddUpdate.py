d={}
d["a"]=10
d["b"]=20  ## Add
print(d)
d["a"]=100   ## Update
print(d)

for key, value in d.items():   ## Iteration
    print(key, value)  