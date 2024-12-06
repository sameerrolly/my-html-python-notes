#1. nested if :
#syntax:
'''
if c1:
      if c2:
            print("s1c2")
      else:
            print("s2c2")
else:
      print("sc1")
'''

#wap.if num is positive,-ve or zero

num=int(input("enter a number :"))
if num>=0:
      if num==0:
            print("zero")
      else:
            print("+ve")
else:
      print("-ve")


#2. Multiple nested  if elif :
#wap for team A and team B with their grades using multiple nested if  :
      
team=input("enter your team : ").upper()
score=int(input("enter the grades : "))

if team=='A':
      if score>=100:
            print(team,"THE SCORE IS GOOD ")
      elif score>=75:
            print(team,"score is average")
      elif score>=55:
            print(team,"below avg")
      else:
            print(team,"poor score")
elif team=='B':
      if score>=100:
            print(team,"THE SCORE IS GOOD ")
      elif score>=75:
            print(team,"score is average")
      elif score>=55:
            print(team,"below avg")
      else:
            print(team,"poor score")
else:
      print("enter correct team!")
