#1.
'''
class demo:
      print("new class")
      a=10
      b=20
      c=a+b
obj=demo()
print(f"{obj.a}+{obj.b}={ obj.c}")
'''

#2.classes and object with function
'''
class fn:
      def sum(aelf,a,b):
           self=a+b
           print("sum of a + b  " ,self)
obj1=fn()
obj1.sum(10,20)
'''
#3.emp class object :

class emp:
      language="python"
      salary="10k"

Sameer=emp()
Sameer.name="rolly "
print(f"my name is {Sameer.name} and i do work in {Sameer.language} and get salary {Sameer.salary}") 
print("My name is ",Sameer.name)

rolly=emp()
print("work in :",rolly.language,"Name is :",Sameer.name,"salary is :",rolly.salary)
