#Global and Local variables
# The variables create outside of function are called as global variables
# The variables create inside of the functions called as local variables

#Example-1-->
# global_var=20  #outside of the function--called global variable
# def fun():
#     local_var=10  #inside the function called local varible
#     print(local_var)
#     print(global_var)
# fun()
# # print(local_var)#invalid bcoz local_var is local variable of func()
# print(global_var)#valid becoz global_var is global variable

#Example-2-->
# xy=100 # this is a global variable
# def cool():
#     xy=200 #local variable
#     print(xy)
# cool()#200
#

# #Example-3--> using global variable in local variable and update value
# xy=100 # this is a global variable
# def cool():
#      global xy=200 #invalid syntax
#      xy=200 #global variable
#      print(xy)
# cool()#200
# print(xy)#200

#Example-4-->
# x=100
# def cool():
#     global x
#     x=500
#     print(x)
# # cool()#500
# print(x)#100

#Example-5-->#create global variable outside as well as inside the function but we have specify global keyword
# def cool():
#     global x
#     x=100
#     print(x)
# cool()#100
# print(x)#100 #able to access bcoz it is global variable

#Example-6-->

















