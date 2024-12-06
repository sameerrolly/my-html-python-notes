#Map,filter and reduce : these are used with list , takes function and a list 

#1. Map (function,list) : map is used when ,we have  to apply the function on every element of a list 


#using a simple function : 
a=[1,2,3,4,5]
def sqr(a):
    return a*a

sqrs=list(map(sqr,a))
print("using map with simple function :",sqrs)
print("------------------------------")
#using a lambda function : 

sum=lambda a:a*a*a
maps=list(map(lambda a:a*a*a,a))
print("using map with lambda function : ",maps)
 
