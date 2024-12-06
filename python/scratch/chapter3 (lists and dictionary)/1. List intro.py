#List  : sequential collection of values

l=["a","b","c"]
m=[1,2,3,4,5]
n=["a",1,"b",2,"c",3,-4,20.3,"unorder"]
print("string list  : ",l)
print("number list : ",m)
print("mixed list : ",n)
print(" ")
print("--------------------------------------------")

#list inside list or nested list  :
print(" ")
x=[[1,2,3],["a","b","c"],["new","nested","list"]]
print(x)
print("x[0] : ",x[0])
print("x[2] : ",x[2])
print("x[2][2] :",x[0][2])
print("x[-1] : ",x[-1])
print("reverse a list using[::-1] ",x[::-1])



#Operating list  :

#1.add , 2.Multiply ,3.update  ,4.delete


print("addition of list l and m :",l+m)
print("multiplication of list : ",m*2)

#Update list  :

new=[1,2,3]
new[2]="new added"
print("new list updated : ",new)

#delete the list  : remove() used to delete the list

a=[1,2,3,4,6,7,9]
del a[2]
print(a)

