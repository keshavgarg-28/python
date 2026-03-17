s= "python"
print(s[::-1]) ## reverse a string
print(s[:3]) 

t="   hello  "
print(t.strip().upper()) ##strip-> to remove leading and trailing spaces

a= "I love JAVA"
print(a.replace("JAVA", "Python"));

s = "apple,banana,grape"
lst=s.split(",") ##split-> to convert str into list
print("-".join(lst)) ## join-> to join list using any character

s = "hello world python"
lst=s.split(" ")
lst=lst[::-1]
print((" ".join(lst)))

s = "  python is fun  "
s=s.strip().title()
print(s)

## Concatenation
s="abc"
s+="10"   
print(s)

s="abc"
a=10
s+=str(a) ##typecasting a  into str
print(s)

a="abc"
b="10"
print(a+b)