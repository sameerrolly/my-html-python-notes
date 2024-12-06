#Reduce funtion  : must import from functools

from functools import reduce

n=[1,2,3,4,5]

def sum(x,y):
      return x+y
def min(x,y):
      return x-y
def mul(x,y):
      return x*y

total=reduce(sum,n)
print("sum of total items from a list is: ",total)
print("min of total items from a list is: ",reduce(min,n))
print("mul of total items from a list is: ",reduce(mul,n))
