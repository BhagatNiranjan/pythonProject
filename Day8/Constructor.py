
#Example8--->
# class myclass:
#     name="Niranjan"
#     def __init__(self,name):  #constructing excpecting one arg
#         print(name)
#         print(self,name)
# mc=myclass("david")#david   # passing parameter to the constructor

#Example9----> # self.a=10  #self consider this is class variables
#constructor: eid,ename,esal
#display() : print eid,ename,esal
# class Emp:
#
#     def __init__(self,eid, ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#     def display(self):
#          print(self.eid,self.ename,self.sal)
# e1=Emp(101,"john",60000)
# e1.display()   #101 john 60000

#Example10---->

class Emp:
#req:emp

     def __init__(self,eid, ename,sal):
         self.eid=eid
         self.ename=ename
         self.sal=sal
     def __str__(self):
         return (self.ename)
     def display(self):
          print(self.eid,self.ename,self.sal)
e1=Emp(101,"john",60000)
e1.display()
e2=Emp(102,"johnii",70000)
e2.display()
e3=Emp(103,"Niranjan",80000)
e3.display()
print(e1)















