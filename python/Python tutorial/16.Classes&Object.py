
#1.Class : Blueprint for creating an object or Object constructor.

class className:       #class created using class keyword : class anyName:
      x="classes are object constructor"
objectNew=className()  #object constructed i.e :    obj=className()
print(className.x)


# basic : employye class example : 
class emp:
      lang="python"
      salary="10k"

Sameer=emp()
print(f"work in {Sameer.lang} and salary is {Sameer.salary} ")

# Instance vs Class attribute:

# Instance attribute : attribute(name,class etc) that is Created inside the object 
# class attribute : attribute(name,class etc) that is Created inside the class

class stu:
      sub="Maths"
      result="pass"
stu1=stu()
print(f" Subject is {stu1.sub} and i {stu1.result}")
stu1.name="Sameer"
print(f"my name is {stu1.name}")

print("Class attribute: sub and result ")
print("Instance/object attribute: stu1.name ")

