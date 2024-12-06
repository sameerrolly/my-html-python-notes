#guess the number using random module , ask again if not found greater or higher untill found and take notes of win or loose;

import random

n=random.randint(1,10)

count=0
win=0
while True:
      print("random number is:",n)
      num=int(input("enter a number"))
      count+=1
      if num==n:
            print("found")
            win+=1
            break

      elif num<n:
            print("try greater number")
      else:
            print("try lower number")
      
print("attempts you've taken: ",count)
print(win,"times you win")
