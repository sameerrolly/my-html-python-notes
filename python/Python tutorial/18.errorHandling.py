#exception handling : used for error handling  :  try except else finally 
try:
    def sum(a,b):
        return a+b
    a=sum(10,20)
    print(a)
except Exception as e:
    print(e)
else:
    print("else will print if try runs successfully")
    
finally:
    print("finally is always used to run even if the bugs occur in try")
    print("only differnce occur when function is used then we should go for finally beacuse iin function finally is used to print always even if function get bug")
