#Inheritance:-->Aquiring all the attributr()variables &(behaviours )& behaviour(methods )
# from one class to another class is called as ineheritance
#Class A--->a,b,c m1 ()  m2()-> Ais parent of b class (base class / super class)
#Class B(A)--->x,y,z   M3()-->It is child of A class (sub class/derived class)

#Objectives of ineheritance:>
#1> code re-usibility
#2>avoid duplication

#Types of Inheritance
# 1>single inheritance--->only one parent one child called single inheritance
# -----------------------
# 2>Multilevel Ineheritance-->c4> is a child class of c3>is a child class ofc2>is a child class ofc1>.
# ----------------------------
# 3>hierachycal  Inheritance-->one parent ---two child
# -----------------------------
# 4>Multiple Ineheritance--> two parents one child
# -----------------------------

# Example 1-->
# class A:
#     def m1(self):
#         print("This is m1 method from class A")
# class B(A):
#     def m2(self):
#         print("This is m2 method from class B")
# b=B()
# b.m1()   #This is m1 method from class A
# b.m2()  #This is m2 method from class B

# Example 2-->Single inheritance
class A:
    x,y=10,20
    def m1(self):
        print()











