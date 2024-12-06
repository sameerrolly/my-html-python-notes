#1. for loop 
#2.  while loop 

# while loop:
# i=1
# while(i<6):
#     print(i , "harry")
#     i+=1

# # always remeber to make condition false at the end 
# name=1
# while(name<10):
#     print(name,"sameer")
#     name+=1

# 1. wap to print numbers from 1 to 100

i=1
while i<=10:
    print(i,end=" ")
    i+=1

# 2. wap to print 10 to 1 numbers 
i=10
while i>=1:
    print(i,end=" ")
    i-=1

# wap to print table of n takes input from user

n=int(input("enter a number n : "))
i=1
while i<=10:
    print(n ,"X",i,"=",n*i)
    i+=1