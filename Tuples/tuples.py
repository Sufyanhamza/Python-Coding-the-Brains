#tuple
# mylist = ("Apple", "Cherry", "Apple", "Banana", "Cherry")
# print(mylist)

#Tuple Length
# mylist = ("Apple", "Cherry", "Apple", "Banana", "Cherry")
# print(len(mylist))

#To create a tuple with only one item, you have to add a comma after the item, 
# otherwise Python will not recognize it as a tuple

# mylist = ("Apple", )
# print(type(mylist))

#Not a Tuple
# list = ("Banana")
# print(type(list))

#Tuple items can be of any data type
# list1 = ("Apple", "Orange", "Banana")
# list2 = (5, 7, 9, 2)
# list3 = (True, False, True, False)

# print(list1)
# print(list2)
# print(list3)

#A tuple can contain different data types
# mylist = ("Apple", 12, True, "Orange")
# print(mylist)

#What is the data type of a tuple -- type()
# mylist = ("Orange", "Apple", "Banana")
# print(type(mylist))

#It is also possible to use the tuple() constructor to make a tuple
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)