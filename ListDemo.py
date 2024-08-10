#Example01:-how to create
#list=>a list is a collection which is ordered and changeable.
#in a python lists are written with square bracket[].
#list is mutable.

# myList1=[10,20,30,40,50]
# myList2=["apple","banana","cherry"]
# myList3=["apple",10,"banana",20]
# # myList=list()

# print(myList1)
# print(myList2)
# print(myList3)


# #Example02:-->accecing items from tje list
# myList=["apple","banana","cherry"] #index start from 0
# print(myList[0])
# print(myList[1])
# print(list[2])
# print(list[-1])
# print(myList[-2])

# #Example1:-->range of indexex
# myList=["apple","banana","cherry","orange","coco","mango"]
# print(myList[2:5])
# print(myList[-4:-1])

# #Example2:->change item value
# mylist=["apple","orange","banana"]
# print(mylist)
# mylist[0]="cherry"
# print(mylist)["cherry","orange", "banana"]

#Example3:->read the items using loop

# mylist=["apple","orange","mango"]
# for i in mylist:
#     print(i)

#example4:-->check the item is exist in the list or not
# mylist=["apple","mango","orange"]
# if "cherry" in mylist:
#     print("yrs apple is present")
# else:
#     print("apple is not present")

# #example5:-->list length (countin g number of items in a list)
# mylist=["apple","mango","orange"]
# print(len(mylist))#3

# #example6:--->add items append() insert()
# mylist=["apple","mango","orange"]
# mylist.append("cherry")
# mylist.insert(4,"banana")#['apple', 'mango', 'orange', 'banana']
# print(mylist)

#example6:--->remove items from the list
#using pop()
# mylist=['apple', 'mango', 'orange', 'banana']
# mylist.pop(1)
# print(mylist)

#del:-is a keyword have no bracket
# mylist=['apple', 'mango', 'orange', 'banana']
# del mylist[1]
# print(mylist)

#clear:->clear is a function()-->clear all value only veriable is avavilable
# mylist=['apple', 'mango', 'orange', 'banana']
# mylist.clear()
# print(mylist)#[]

#Example10:->>copy list
#list()
#approach1
# mylist1=['apple', 'mango', 'orange', 'banana']
# mylist2=list(mylist1)
# print(mylist1) #['apple', 'mango', 'orange', 'banana']
# print(mylist2) #['apple', 'mango', 'orange', 'banana']

# #copy()
# mylist1=['apple', 'mango', 'orange', 'banana']
# mylist2=mylist1.copy()
# print(mylist1) #['apple', 'mango', 'orange', 'banana']
# print(mylist2)

#Example10:-->combine/join lists
#using + operators
# list1=["a","b","c"]
# list2=[1,2,3]
# list3=list1+list2
# print(list3) #['a', 'b', 'c', 1, 2, 3]

#using looping statements
# list1=["a","b","c"]
# list2=[1,2,3]
# for i in list2:
#     list1.append(i)
# print(list1) #['a', 'b', 'c', 1, 2, 3]

#using extend()
# list1=["a","b","c"]
# list2=[1,2,3]
# list1.extend(list2)
# print(list1) #['a', 'b', 'c', 1, 2, 3]







