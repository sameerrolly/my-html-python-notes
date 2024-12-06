#virtual environment:  install : pip install virtualenv :this will install package

#1. lambda functions : [ variable = lambda aeguments a,b,c : a+b+c expression ] 
from functools import reduce

min= lambda x , y : x-y
print(min(10,20)) 



#2. join method :used for the strings :  to add between an string in list

l=["harry","rolly","sameer"]

j=":".join(l)
print("add icons or anything  using join method between string of a list:",j)

m=("a","b","c")
s="+".join(m)
print("sum of three strings using join method : ",s)

#map,filter,reduce :

#a. map : applies a function to all items in a input list 
# map(function,l)   :  to print the list form of a function  

aL=[1,2,3,4,5]
sqrs=lambda al:al*al

sqList=map(sqrs,aL)
print(list(sqList))


#filter : use in true or false conditions  
def even(n):
    if n%2==0:
        return True
    return False

onlyEven=filter(even,aL)
print("even number from a list using filter  : ",list(onlyEven))



#reduce function : 
num=[1,2,3,4,6]
def sums(a,b):
    return a+b

print("list is",num,"reduce function for sum of list items  :",reduce(sums,num))