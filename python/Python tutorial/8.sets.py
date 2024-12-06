set1={1,2,3,4,4,4,2,6}  #does'nt contain duplicate values
set2={"s1","s2","s3"}
print(set1,set2)

# empty set
EmpSet=set()
print(EmpSet)
print(type(EmpSet))

# methods in set

# 1. length of set
print(set1)
l=(len(set1))
print("length of set1 is : ",l)

# 2.add and remove
set1.add(200)
set1.remove(1)
print("after adding and removing: ",set1)

ed={}
name=input("enter name: ")
lang=input("enter language")

ed.update({name:lang})
name=input("enter name: ")
lang=input("enter language")

ed.update({name:lang})
name=input("enter name: ")
lang=input("enter language")

ed.update({name:lang})

print(ed)
