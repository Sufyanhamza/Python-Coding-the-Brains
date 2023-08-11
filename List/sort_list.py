#List objects have a sort() method that will sort the list alphanumerically, ascending, by default
# mylist = ["Apple", "Banana", "Orange", "Cherry"]
# mylist.sort()
# print(mylist)

#Sort the list numerically
# list = [100, 50, 30, 60, 70, 10]
# list.sort()
# print(list)


#To sort descending, use the keyword argument reverse = True    
# a = [12, 1, 90, 34, 66, 98]
# a.sort(reverse=True)
# print(a)

#Customize Sort Function
# def myfunc(n):
#     return abs(n - 50)
# a = [20, 10, 50, 60, 80]
# a.sort(key = myfunc)
# print(a)


#Case Insensitive Sort
# b = ["kiwi", "orange", "Cherry", "Mango"]
# b.sort()
# print(b)

#if you want a case-insensitive sort function, use str.lower as a key function
# mylist = ["Kiwi", "Orange", "cherry", "Mango"]
# mylist.sort(key = str.lower)
# print(mylist)


#The reverse() method reverses the current sorting order of the elements
mylist = ["Apple", "Banana", "Cherry", "Mango"]
mylist.reverse()
print(mylist)




