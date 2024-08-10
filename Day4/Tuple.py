#A tuple is a collection which is ordered and unchangable.
#in python tuples are written with round brackets.()
#tuple is immutable.
#immutable:->1>we cannot modify existing value
   #2>we cannto append new value
   #3>we cannot insert a new value
   #4>we cannot remove a new value

# #Example 1:->Creating tuple
# mytuple=("apple","banana","mango")
# print(mytuple)#('apple', 'banana', 'mango')
# mytuple=()#empty tuple

# #Example 2:->access tuples items
# mytuple=("apple","banana","mango")
# print(mytuple[1])#banana
# print(mytuple[-1])#mango

#Example 3:-> range of index
# mytuple=("apple","banana","mango","cherry","melon","kiwi")
# print(mytuple[2:5])#('mango', 'cherry', 'melon')
# print(mytuple[-5:-1])

#exmple 4:->>changing tuples items
#by default tuples does not allowe you to change value because it is immutable
#but there is work arround
#tuple-->list(modify)-->tuple

# mytuple = ("apple", "banana", "100", "cherry", "88.00", "kiwi")
# mylist=list(mytuple)
# mylist[1]="orange"
# mytuple=tuple(mylist)
# print(mytuple)#('apple', 'orange', 'mango', 'cherry', 'melon', 'kiwi')

#Examples 5:--> reading tuple items using loop
# mytuple=('apple', 'orange', 'mango', 'cherry', 'melon', 'kiwi')
# for i in mytuple:
#  print(i)

#Examples 6:-->check if item exists (searching of item in tuple)
# mytuple=('apple', 'orange', 'mango', 'cherry', 'melon', 'kiwi')
# if "banana123" in mytuple:
#     print("yes,banana is present")
# else:
#     print("no,banana is not present")#no,banana is not present
#
# # Examples 7:-->type length-counting items in a tuple
# mytuple=('apple', 'orange', 'mango', 'cherry', 'melon', 'kiwi')
# print(len(mytuple))#6

# # Examples 8:-->add items in tuples--not possible bcoz tuple is immutable-cannot change value/items
# mytuple=('apple', 'orange', 'mango', 'cherry', 'melon', 'kiwi')
# mytuple[0]="orange"
# print(mytuple)#TypeError: 'tuple' object does not support item assignment

# Examples 9:-->copy tuple-yes we can copy
# mytuple1=('apple', 'orange', 'mango', 'cherry', 'melon', 'kiwi')
# mytuple2=mytuple1
# print(mytuple2)

# Examples 10:-->removing items from the tuple-->not possible bcoz tuple is immutable
# mytuple=('apple', 'orange', 'mango', 'cherry', 'melon', 'kiwi')
# mytuple.remove("apple")
# print(mytuple)#AttributeError: 'tuple' object has no attribute 'remove'

# Examples 11:-->join/combine tuple
tuple1=(10,20,30)
tuple2=("a","b","c")
tuple3=tuple1+tuple2
print(tuple3)#(10, 20, 30, 'a', 'b', 'c')

# Examples 12:-->tuples comparison
mylist1=(10,20,30)
mylist2=("a","b","c")
if mylist1==mylist2:
    print("mylist are equal")
else:
    print("mylist are not equal")#tuple are not equal








