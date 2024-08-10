# name="john"
# age=24
# sal=6000.90
name,age,sal="john",24,6000.90

#approach1
print(name)
print(age)
print(sal)
print(name,age,sal)

#approach2
print("name is:",name)
print("age is:",age)
print("sal is:",age)

#approach3
print("name is:%s  age is:%d  sal is:%g" %(name,age,sal))

#approach4{}
print("name is{} age is:{}  sal is:{}" .format(name,age,sal))
print("sal is:{} age is:{}  name is:{}" .format(sal,age,name))

