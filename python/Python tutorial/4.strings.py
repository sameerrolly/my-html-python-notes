# STRINGS : are not changebale/ mutable
# print("Strings are data types in python")
# print('three types to print string ')
# a='single quote string'
# b="double quote string"
# c='''triple quote string'''
# print(a)
# print(b)
# print(c)


# Methods / actions perform on strings : slicing
name="SAMEER"
print(name[0:4]) 
print(name[-1:]) 

# slicing with skiping a value
skip="0123456789"  
print(skip[0:9:4])

# function in strings
# 1.len()
print(len(name))
print(name.endswith("EER"))
print(name.startswith("SAM"))
print(name.lower())
sirname="rolly"
print(sirname.title())
fname="sameer  rolly"
print(fname.replace("sameer","SAM"))


# PRACTICE

gdm=input("enter your name")
print(f"good morning{gdm} , welcome to learn python")  
