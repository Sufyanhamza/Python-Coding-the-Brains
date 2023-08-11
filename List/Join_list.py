# mylist1 = ["a", "b", "c"]
# mylist2 = [1, 2, 3]
# mylist3 = mylist1 + mylist2
# print(mylist3)


#Append list2 into list1
# mylist1 = ["a", "b", "c"]
# mylist2 = [1, 2, 3]

# for x in mylist2:
#     mylist1.append(x)

# print(mylist1)

#Use the extend() method to add list2 at the end of list1
mylist1 = ["a", "b", "c"]
mylist2 = [1, 2, 3]

mylist1.extend(mylist2)
print(mylist1)