#random module :

'''

1.random()
2.randint()
3.choice()
4.randrange()

'''

import random as rd

print(rd.random())


print(rd.randrange(1,20,2))

x=["sam","rolly","gym"]
y=(1,2,3)
print(rd.choices(x,y))

print(rd.sample(x,k=1))
