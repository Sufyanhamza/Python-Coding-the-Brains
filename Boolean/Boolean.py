#print(10 > 9)
#print(10 == 9)
#print(10 < 0)

a = 100
b = 80

if(a > b):
    print("a is greater than b")
else:
    print("b is greater than a ")

#Evaluate Values and Variables
print(bool("Hello"))
print(bool(10))

#Evaluate two variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(bool("Hello"))
print(bool(450))
print(bool(["Apple","Orange","Mango"]))

def myfunc():
    return True
if myfunc():
    print("YES")
else:
    print("No")