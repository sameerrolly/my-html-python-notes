#Map,filter and reduce : these are used with list , takes function and a list 

#1. Map (function,list) :

a=[1,2,3,4,5]
def sqr(a):
    return a*a

sqrs=list(map(sqr,a))
print(sqrs)
