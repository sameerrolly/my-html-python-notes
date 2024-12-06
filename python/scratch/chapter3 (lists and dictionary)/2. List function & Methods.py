#List Functions : mainly there are 4 = len(),min(),max(),list()


print("---------------------------functions--------------------------------------")

print(" ")
#1.len() : gives the no. of items in list

l=[1,2,3,4,6]
print("no. of items of list using len() function : ",len(l))

m=[2,3,1,3,1,12,12,11,11,11,222,222,2,22,11,1111,11,11,1,11]
print(len(m))

#2. min(),max()

print("min is ",min(m))
print("max is ",max(m))


#list() : convert tuple into list

tuples=(1,2,30)
print("befor list():",type(tuples))
print("after list()",type(list(tuples)))
print(tuples)
tupleNew=list(tuples)
print(tupleNew)
print(" ")
print("-----------------------end of list functions------------------------------------------")


#Methods of list :

#1. APPEND(): ADD NEW ELEMENTS TO THE LIST  , takes only one argument at a time 

print(l)
l.append(122)
l.append("append")
print(l)
#make a new list using null list 
newList=[]
newList.append(1)
print(newList)

#2.COUNT() : how many times a elemet occur in the list

x=[1,2,2,2,2,12,12,22,122,12,2]
print("2 occurs in list ",x.count(2),"times")
print(x)

#extend(): extends the list with another
fruits=["apple","mango"]
shakes=["banana","lichi"]
print(fruits.extend(shakes))
print("")
print("reverse using reverse() function:",x.reverse())
print(x)
print("")
print("reverse using x[::-]",x[::-1])
print("sort using x.sort()",x.sort())
