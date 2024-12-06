# # def func(a,b):
# #     c=a+b
# #     print(c)
# # func(10,20)

# # def sum(a,b,d):
# #     c=a+b+d
# #     print(c)
# # sum(10,20,30)

# # -----------------------------------------------Basic function

# def myName():  #FUNCTION DEFINITION
#     print("HELLO WORLD! : Basic function")
# myName()       #FUNCTION CALLING

# # -----------------------------------------------Argument function: 
# def arg(a):
#     print("Welcome !",a)
# arg("Sameer Rolly")
# arg("MCA GRADUATE")
# arg("WEB DEVELOPER")
# print("argument passed in calling of function")
# print(" ")

# #------------------------------------------------Multiple arguments:
# def multiArg(fname,lname,rollNo):
#     print(f"Name is {fname} {lname} and my class roll number is : {rollNo}")
# multiArg("Sameer","Rolly",21)
# print(" ")

# #------------------------------------------------argument Declared in function definition
# def my_function(country = "Norway"):
#   print("I am from " + country)
# my_function("Sweden")
# my_function("India")
# my_function()


# return function :
print("Return function ")

def returnFun(fname,lname):
    print(f"My AI name is {fname} {lname},HOW CAN I HELP YOU")
    return "done"
    
q=returnFun("sameer","ai")
print(q)
