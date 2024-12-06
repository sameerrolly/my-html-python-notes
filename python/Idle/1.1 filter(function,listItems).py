#filter :
aL=[1,2,3,4,6,7,8,9]
def even(n):
    if n%2==0:
        return True
    return False

onlyEven=filter(even,aL)
print("even number from a list using filter  : ",list(onlyEven))


#NOTE :  mainly used in true or false conditions :

a=[2,4,6,8,10,11]
def greater(a):
      if a==11:
            return True
      return False

newList=filter(greater,a)
print(list(newList))

