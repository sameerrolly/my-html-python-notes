'''#while loops
"""
syntax:
    i=0
    while condition until fail:
        print("operation perform here ")
        i+=1 """# must use for increment the condition until failure

#1.Print numbers from 1 to 5

i=1
while i<=5:
    print(i, end="")
    i=i+1
print(" ")

#2. print numbers from 5 to 1

n=5
while n>=1:
    print(n,end="")
    n-=1


#3. Wap to print the table of a number n from user's input
   ''' '''
n=int(input("\n enter a number : "))
j=1
while j <=10:
    x=(f"{n}X{j}={n*j}")
    print(x)
    j+=1
    '''
'''
#4. print elements of a list
List=[1,4,9,16,25,36,49,64,81,100]
x=len(List)
i=0
while i<x:
    print("\t",List[i])
    i=i+1

#5. break and countinue statements

x=1
while x<=6:
    if x==3:
        break
    print(x,"x will break at 3")
    x+=1
    
print("this is break statement at 3 ")
 
#. countinue statement


x=1
while x<=6:
    if x==3:
        x+=1
        continue
    print(x,"x will pass  3")
    x+=1
print(" continue statement at 3 ")
'''
#6. for loop practice:
'''
num=(1,2,10,20,30,40,60,40,20)

x=20
idx=0
for el in num:
    if(el==x):
        print("value of x found at index:",idx)
    idx+=1
 

#7.wap to find sum of first n numbers
n=int(input("enter a number : "))
sum=1
for i in range(1,n+1):
    print(i)
    sum*=i
print("total is ", sum)


'''

#
'''
def sums(a,b):
    c=a+b
    print(c)
    pass
    return sum
x=sums(10,20)
sums(2,4)

def name(f,l="rolly"):
    print(f"hello {f} your sirname is {l}")
name("sameer")
'''
'''
def ret(a,b):
    c=a+b
    return c
x=ret(10,20)

while True:
    m=10
    n=int(input("enter number : "))
    
    print("choose between 1 to 2 for action")
    choice=int(input("enter a number to choice between 0 to 2: "))
    if choice==1:
        print("sum is  :",n,"+",m,"=",n+m)
    if choice==2:
        print("division is : ",n-m)
    if choice==0:
        print("end of the program")
        break
print("function return value is :  ",x)
'''

# classmethod is used for printing the actual instance value after new object instance is created.
class method:
    a=10   #class instance

    def old(self):
        print(f"value of a :{self.a}") #will print object instance
    @classmethod
    def classmethod(self):
        print("value of a after @classmethod decorator: ",self.a)  #will print actual value of class instance
    
x=method()
x.a=20     #object instance created
x.classmethod()
x.old()





     
 
