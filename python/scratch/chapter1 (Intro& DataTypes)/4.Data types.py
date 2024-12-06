#Data types :

'''
1.Number : int,float,complex
2.string
3.list ["list","is","in square","brackets"]
4.tuple ["tuple","is","in round","brackets"]
5.dictionary  :  {"name":"sam","age":20}
'''

#Number :
print("Numbers")
x=10
y=-20
z=20.32
print(x,y,z)
print("x is",type(x))
print("y is",type(y))
print("z is",type(z))
print("")
print("------------------------------")

#String :
print("String")

a="hello world!, this is a string"
print(a)
print(len(a))
print(a.count('l'))
print(a.upper())
print("")
print("------------------------------")

#list :
print("List")
l=["sam","rolly",10,"abc",201,30]
print(l)
print(l[0])
print(l[2:4])
print(l[-1])
print(l[::-1])
print("------------------------------")

#Tuple :
print("Tuple")

T=("tuple","is","non-mutable")
print(T)
print(T[2:3])
print(T*2)
print("------------------------------")

#Dictionary :
print("Dictionary")

d={'name':'sameer',
   'rollNo.':20,
   "age":24}
print(d)
print(d["age"])
print(d.keys())
print(d.values())
print(len(d))
