#A dictionary is a collection which is unordered, changable(mutable) and indexed.
#in python dictionaries are written with curly brackets, and they have keys and values.
#store kay and value

#Example1--->creating dictionary
# mydic={10:"x",201:"r",30:"u"}
# print(mydic)#{10: 'x', 201: 'r', 30: 'u'} // unordered

#Example2--->access items from dictionary
# mydic={
#     "brand":"hundaii",
#     "model":"i20k",
#     "year":"2021"
# }
# print(mydic["brand"])
# print(mydic["year"])
# print(mydic["model"])
#
# #using get()
# x=mydic.get("brand")
# print(x)  #hundaii

#Example3--->change value in dictionarry
# mydic={
#     "brand":"hundaii",
#     "model":"i20k",
#     "year":"2021"
# }
# print(mydic) #{'brand': 'hundaii', 'model': 'i20k', 'year': '2021'}
# mydic["year"]=2022
# print(mydic) #{'brand': 'hundaii', 'model': 'i20k', 'year': 2022}

#Example4--->readin items from dictionarry using loop
# mydic={
#     "brand":"hundaii",
#      "model":"i20k",
#      "year":"2021"
#  }
# for i in mydic:
#     print(i)# prints only keys from dictionarry ---brand ,model,year
#
#     print(mydic[i]) #prints only values from dictionarry---i20k, hundaii, 2021
# for i in mydic.values():
#     print(i)
# for x,y in mydic.items():
#     print(x,y) #print keys along with the value

#Example5--->check key is exist in dictionary or not
# mydic={
# "brand":"hundaii",
# "model":"i20k",
# "year":"2021"
# }
# if "model" in mydic:
#     print("exist")#true
# else:
#     print("not exist")
# print("model"in mydic)#true

#Example6--->find number of items in dictionary
# mydic={
# "brand":"hundaii",
# "model":"i20k",
# "year":"2021"
# }
# print(len(mydic))#3

#Example7--->adding items to dictionary
# mydic={
# "brand":"hundaii",
# "model":"i20k",
# "year":"2021"
# }
# mydic["color"]="red"
# print(mydic)

#Example8--->remove items to dictionary
# mydic={
# "brand":"hundaii",
# "model":"i20k",
# "year":"2021"
# }
# mydic.pop("year")
# print(mydic) #{'brand': 'hundaii', 'model': 'i20k'}
# del mydic["year"]
# print(mydic) #{'brand': 'hundaii', 'model': 'i20k'}

# del mydic
# print(mydic)#NameError: name 'mydic' is not defined--->bcoz alredy deleted

# mydic.clear()
# print(mydic) #{}

#Example9--->copy dictionary
# mydic1={
#  "brand":"hundaii",
#  "model":"i20k",
#  "year":"2021"
#  }
# #using copy()
# mydic2=mydic1
# print(mydic2) #{'brand': 'hundaii', 'model': 'i20k', 'year': '2021'}

#without using copy()
# mydic2=mydic1
# print(mydic2)#{'brand': 'hundaii', 'model': 'i20k', 'year': '2021'}


















