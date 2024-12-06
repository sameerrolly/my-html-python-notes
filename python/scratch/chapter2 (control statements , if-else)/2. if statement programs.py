#if statement  : syntax:--    (if condition : statement)

#1.wap if person is minor
'''
age=int(input("enter your age:"))
if age<=18:
      print("Minor")

print("----------------------------------------- ")
#2. wap to authentication of a user

name=(input("enter your name : "))
password=input("enter your password: ").lower()

if password=="sam123":
      print("welcome to insta *",name)
else:
      print("password incorrect!,try again")
'''

#3.wap to check entered year is leap or not

year=int(input("enter a year to check leap or not:"))
if (year%4)==0:
      print("Leap year !")
else:
      print("not leap year")

