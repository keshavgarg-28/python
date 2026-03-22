names=["ram", "shyam", "hari"]
for i, names in enumerate(names):
    print(i, names)

for i, name in enumerate(names, start=1):
    print(i, name)

e= enumerate(["a","b","c"])
print(list(e))