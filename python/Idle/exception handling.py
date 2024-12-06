#Exception handling: error handling

#Try: when we think we will have error in program 
#except: to print a message as an error

'''
try:
      m=int(input("enter a number: "))
      n=10
      print("value of n + m : ",n+m)
except:
      print("ERROR! enter valid input")
      
print("--------------------------------------------------------------")
print("exception as a message using (except Exception as e)")

try:
      m=int(input("enter a number: "))
      n=10
      print("value of n + m : ",n+m)
except Exception as e:
      print(e)
finally:
      print("this code will always run even your whole code has bugs ")
      print("Try,Except,finally")
'''

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





m=[1,2,3,4,5]
squarem=[]

for i in m:
    squarem.append(i*i)
print(squarem)

 

#using list comprehension :

squarem=[i*i for i in m ]
print(squarem)

