#x = "Awesome"

#def myfunc():
#   print("Python is", x)

#myfunc()

#x = "Awesome"

#def myfunc():
#    x = "Fantastic"
#   print("Python is", x)
#myfunc()
#print("Python is " , x)


#def myfunc():
#    global x
#    x = "Fantastic"
#myfunc()
#print("Python is ", x)

x = "Awesome"
def myfunc():
    global x
    x = "Fantastic"
myfunc()
print("Python is ", x)
