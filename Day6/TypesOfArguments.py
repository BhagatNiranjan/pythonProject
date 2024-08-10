#Example1:--->
# def fun(i,j):
#     print(i,j)
# # fun(10,20)  #positional arguments #10 20
# fun(j=20,i=10) #keywords arguments

#Example2:--->default arg
# def fun(i,j=10):
#     print(i,j)
# fun(100,200) #100 200
# fun(100) #100 10

#Example3:--->keyword arg
# def greetings(name,greetng):
#     print(greetng+" "+name)
# greetings(name="john",greetng="hello") #hello john--->#keyword arg
# greetings(greetng="hello",name="john") #hello john

#Example4:--->
# def my_fun(a,b,c):
#     print(a,b,c)
# my_fun(10,20,30) #positional parameter-->10 20 30
# my_fun(a=10,b=20,c=30)#keywords arguments--->10 20 30
# my_fun(b=20,a=10,c=30)#keyword argument///we can change the order in keyword arg-->10 20 30
# my_fun(10,20,c=30)#perfectly fine-->combintion of positional and keyword arg-->10 20 30
# my_fun(10,b=20,c=30)##perfectly fine-->10 20 30
# #my_fun(10,b=20,30)#incorrect statements positional arg must be before any keyword arg#this is logical error


#Example5:--->#how function can return the multiple value
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
# print(largest(100,200))
# print(largest(20,10))
res=largest(10,20)
print(res)
print(type(res))#type of reslt is tuples---tuples contain a multiple value









