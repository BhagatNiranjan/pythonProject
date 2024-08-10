
#whenever u create function inside in a class we called method
#every method take 1 arg called self default function
#we should not remove the self
#self-->this perticular method belongs to upper perticular class

#Example-1->how to create a object and class
# class myclass:#how to create a class
#     def myfun(self):
#         pass # none
#     def display(self ,name):
#         print(name)
# mc1=myclass()#create a obj
# mc1.myfun()#through obj how we access the methods
# mc1.display("scott")

#Example-2->
#using static method -we can call using class
# class myclass:
#     def m1(self):
#         print("this is instance method.....")#this is instance method.....
#     @staticmethod
#     def m2(self,num):
#         print(self,num)
#
# mc=myclass()
# mc.m1()
# mc.m2(100,200)#100 200
# myclass.m2(10,20)#10 20

#Example-3->

#global ,class and local variables
#class variables-->
# class myclass:
#     a,b=10,20 #class variables
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#          print(self.a*self.b)
# mc=myclass()
# mc.add()#30
# mc.mul()#200

#Example-4->
# i,j=15,25 #global variables
# class myclass:
#     a,b=10,20 #class variables
#     def add(self,x,y): #x,y are local variables
#         print(x+y) #x,y are local variables
#         print(self.a+self.b) # a,b are class variabels
#         print(i+j) #i,j are global variables
#
# mc=myclass()
# mc.add(100,200) #300,30,40

#Example-5->
# a,b=15,25 #global variables
# class myclass:
#      a,b=10,20 #class variables
#      def add(self,a,b): #x,y are local variables
#         print(a+b) #local variables
#         print(self.a+self.b)
#         print(globals()["a"]+globals()["b"])#access global variables
#
# mc=myclass()
# mc.add(100,200)#300,30,40
#

#Example-6->once class can have a multiple object
#  class myclass:
#      def display(self,name):
#          print("this is display method....")
#          print(name)

  # obj1=myclass()
# obj1.display("john")
#
# obj2=myclass()
# obj2.display("Niranjan")

#Constructor
#method--->give any name,---return the values
# ---method can take arg/parameters
# method----we have to use an obj to invoke the method
#constructor-->constructor name should be __init__(self):
#constructor will not return any value
#constructor can also take arg /parameter
#constructor will be called at the time of obj creation itself.

#Example-7-> constructor ex-how to create a constructor
class myclass:
    def __init__(self):
        print("this is a constructor")
    def m1(selfself):
        print("hello...")
    def m2(selfself,x,y):
        return(x+y)
mc=myclass()#invoke constructor automatically
mc.m1() #method we have call explicitelly by using obj
print(mc.m2(10,20))
# O/P:this is a constructor
# hello...
# 30

































