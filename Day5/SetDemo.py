#A set is a collection wich is unordered and unindexed.in pthon sets are written with curly bracket{}

#Example1:->creating set
# myset={"apple","banana","cherry"}
# print(myset) #{'cherry', 'banana', 'apple'}

#Example2:->Accesing items from set
# myset={"apple","banana","cherry"}
# for i in myset:
#     print(i)

#Example3:-> value is exist in set or not
# myset={"apple","banana","cherry"}
# print("apple" in myset)#true
# print("banana2" in myset)#false

#Example4:->adding items to set
#methods->1)-add()-->add single item
# 2)-update()--->add multiple item
# myset={"apple","banana","cherry"}
# # myset.add("orange")
# myset.update(["mango","graphes"])
# print(myset)#{'banana', 'mango', 'cherry', 'apple', 'graphes'}

#Example5:->find numbers of items in a set
# myset={"apple","banana","cherry"}
# print(len(myset))#3

#Example6:->remove item from the set
#remove()
#discard()
# myset={"apple","banana","cherry"}
# myset.remove("apple")
# print(myset)#{'banana', 'cherry'}
# myset.remove("xyz")
# print(myset)#KeyError: 'xyz'

#discard()-->
# myset.discard("banana")
# print(myset) #{'cherry', 'apple'}
# myset.discard("xyz")#will not throug error

#Example7:->clear all items from set
# myset={"apple","banana","cherry"}
# myset.clear()
# print(myset)
# del myset
# print(myset)#NameError: name 'myset' is not defined --bcoz alredy deleted

#Example8:->joining 2 sets-unioon()
# set1={"a","b","c"}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3) #{1, 2, 3, 'c', 'b', 'a'}

#2 sets update()
set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1) #{1, 2, 3, 'a', 'b', 'c'}











