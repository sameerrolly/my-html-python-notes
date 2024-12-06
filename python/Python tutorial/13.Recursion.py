# RECURSION: It's a function which call itself.

def factorial(n):
    if (n==0 or n==1):
        return 1
    return n*factorial(n-1)
n=int(input("enter a number: "))
x=factorial(n)
print(x)

# 
def cnvrt(c):
    return 6*c
a=cnvrt(10)
print(a)