#advance topics of python : newly added:

#1. Walrus operator (:=) : Assignment expression , sign of walrus is this :=
'''
if (n:=len([1,2,3,4,5]))>3:
      print(n)

      '''

#02.Type definition in python : help to identify the variable type

#syntax is :
a : int =10
print(a)
b:str="sam"
print(b)

def sumIs(x:int,y:int):
      return x+y

a=sumIs(10,20)
print(a)

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merge=dict1|dict2
print(merge)


#enumerated function : 

l=[10,20,12,1212]
index=0
for i in l:
    print(f"index is {index} and values in list is {i}")
    index+=1
print("---------------------------------------------------------------")
#same using enumerate function:

for index,i in enumerate(l):
        print(f"using enumerate function: index is {index} and values in list is {i}")



#list comprehension:

m=[1,2,3,4,5]
squarem=[]

for i in m:
    squarem.append(i*i)
print(squarem)
    

#using list comprehension :

squarem=[i*i for i in m ]
print("using comprehension of list : ",squarem)


print("----------------------------------------------------------------------------------")
#exception handling : used for error handling  :  try except else finally 
try:
    def sum(a,b):
        return a+b
    a=sum(10,20)
    print(a)
except Exception as e:
    print(e)
else:
    print("else will print if try runs successfully")
    
finally:
    print("finally is always used to run even if the bugs occur in try")
    print("only differnce occur when function is used then we should go for finally beacuse iin function finally is used to print always even if function get bug")
