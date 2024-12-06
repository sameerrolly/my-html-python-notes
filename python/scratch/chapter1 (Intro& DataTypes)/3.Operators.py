#Operators :

#1. arithmatic :

a=10
b=20
print("arithmatic operator :")
print(a+b,a-b,a*b,a/b,a%b,a**b,a//b)
print("------------------------------------")

#2.relational :
print("realtional operator:")
print(a==b,a!=b,a>b,a<b,a<=b,a>=b)
print("------------------------------------")


#3.assignment :
print("value of a is :" ,a)
#print(a+=b)#,a-=b,a/=b,a*=b)
a+=b
print(a)
print("------------------------------------")

#4. membership operator : in,not in

l=[1,2,3,30,23,122,331,]
x=30
print("a in list :",a  in l)
print("x not in list :",x not in l)
print("------------------------------------")

#5.identify operator : is ,is not

a=10
b=20
c=10
print("a=",a,"b=",b,"c=",c)
print("a is b: ",a is b)
print("a is not c",a is not c )
