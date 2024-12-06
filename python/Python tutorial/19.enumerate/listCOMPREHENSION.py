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