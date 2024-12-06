#Lambda function :

def sqr(n):
      print("square of ",n," is ",n*n)
n=int(input("enter a number  : "))
sqr(n)

print("--------------------------------------")
def cubes(m):
      return (m*m*m)
m=int(input("enter a number  : "))
print("cubes of ",m,"is :  ",cubes(m))


#now using lambda function :

#------------------------------------syntax is  : (lambda arg:expression )

#1.square using lambda :
print("--------------------------------------")

squares=lambda x:x*x
x=int(input("enter a number  : "))
print("using lambda function : ", squares(x))
print("--------------------------------------")


#sum of three numbers using lambda  :

sum=lambda x,y,z:x+y+z
print("sum of three number is : ",sum(10,20,30))
print("--------------------------------------")
