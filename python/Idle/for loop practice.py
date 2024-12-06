#For loop Practice sets :
'''
#1.wap to print multiplication on a given number:

num=int(input("enter a number  : "))
for i in range(1,11):
      print(num*i)
print("DONE")

#Using while loop:
n=int(input("enter a number  : "))
i=1
while i<=10:
      print(i*n)
      i+=1

#2.greet with names starting with S

L=["Sam","rolly","lUCKY","Sameer"]
for name in L:
      if name.startswith("S"):
            print("hello",name)
'''
#3. star pattern n=3

num=int(input("enter a number  : "))
for i in range(num):
      for j in range(num):
            print("*")
      
 
