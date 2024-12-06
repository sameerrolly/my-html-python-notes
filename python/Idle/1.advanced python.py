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


#3. Match case :
'''
def https(status):
      match status:
                  case 100:
                        return "ok"
                  case 200:
                        return "not ok"
                  case :
                        return "not found"

print(https(100))
'''

#4. merge dictionary : using |
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merge=dict1|dict2
print(merge)
