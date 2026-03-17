s= "python"
print(s[::-1])
print(s[:3])

t="   hello  "
print(t.strip().upper())

a= "I love JAVA"
print(a.replace("JAVA", "Python"));

s = "apple,banana,grape"
lst=s.split(",")
print("-".join(lst))

s = "hello world python"
lst=s.split(" ")
lst=lst[::-1]
print((" ".join(lst)))

s = "  python is fun  "
s=s.strip().title()
print(s)
