# s="welcome"
# s='welcome'
# s=str("welcome")
# s=str('welcome')


# #creating empty string
# name=str()
# name=""
# name=''

#mutable can change the value of the variable
#immutable---> cannot change the value of variable
#string is mutable or inmutable----> ans is immutable
#if the value is changed after updation thenn it is immutable

# str1="welcome"
# print(id(str1))     #id of variable1500669432944
# str1=str1+"python"
# print(id(str1))  #2071448525040

#Different ways to create a String
#ex3-->+and =with string
# str="welcome"
# print(str+"programming")
# print(str*3)

#Example4---> slicing####3[]
#starting index 0 AND ending index 1
# str="welcome"
# print(str[1:3])#lcom
# print(str[:6])#welcom here starting indes is 0 by default
# print(str[2:])#lcome
# print(str[1:-1]) #elcom
# print(str[1:-2]) #elco

#Example5-->ord() and chr()
# print(ord('A'))#65---->return  The ASCII code of the Character
# print(chr(65))#A------>return the character represented by the a number

#Example6-->min() len() max()
# print(max("abc"))#c
# print(min("abc"))#a
# print(len("welcome"))#7

##Example7-->in, not in operators--returen true/false
# s="welcome"
# print("come"in s)#true
# print("lone"in s)#false
# print("lone" not in s)#true
# print("come" not in s)#false

##Example 8--> comparison
# print("tim"=="tie")
# print("tim"!="time")
# print("arrow">"aron")
# print("teeth"<"tee")

#Example9--> testing string functions True/False
# s="welcome to python"
# print(s.isalnum())#false
# print("welcome".isalpha())#true
# print("2012".isdigit())#true
# print("first number".isidentifier())#false
# print(s.islower())#true
# print("WELCOME".isupper())#true
# print(" ".isspace())#true

#Example10-->searching for substring
# s="welcome to python"
# print(s.endswith("thon"))#true
# print(s.startswith("good"))#false
# print(s.find("come"))#3
# print(s.find("become"))#-1
# print(s.count("o"))#3

#Example11-->converting string in different formats
# s="string in python"
# s1=s.capitalize()
# print(s1)
# s2=s.title()
# print(s2)
# s3=s.lower()
# print(s3)
# s4=s.swapcase()
# print(s4)
# s5=s.replace("in","on")
# print(s5)



#Example12---->reverse string
#method->1
# s="welcome"
# rev_str=""
# for i in s:
#     rev_str=i+rev_str
#     print("reversed string is:",rev_str)

  #method-->2
s="welcome"
rev_str=s[::-1]
print(rev_str)














