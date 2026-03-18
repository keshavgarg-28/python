s={1,2,3}
s.add(4)       ## Add element 
s.remove(3)    ## Remove an elemen
print(1 in s)

a={1,2,3}
b={3,4,5}
print(a | b)   ## Union
print(a & b)   ## Intersection
print(a - b)   ## Difference

a = {1,2}
b = {1,2,3,4}
print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint({5,6}))