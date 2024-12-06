# conditional expression

#1. IF 

a=int(input("enter your age to vote:  "))
if a >=18:
    print("ELIGIBLE TO VOTE")
else:
    print("NOT ELIGIBLE")

# -------------------------------------------------------------------------------

# 2. IF-ELIF-ELSE LADDER:

a=int(input("enter your age to vote:  "))
if (a>=18):
    print("ELIGIBLE TO VOTE")
elif (a<0):
    print("invalid input I.E -ve")
elif(a==0):
    print("invalid input I.E zero")
else:
    print("NOT ELIGIBLE")

# -------------------------------------------------------------------------------
# RELATIONAL OPERATORS 

# <= less than equal to  
# >= greater than equal to 
# == equals to 

#  LOGICAL OPERATOR 

# and = if a and b are true then True
# or  = if atleast one is true from a and b then True
# not = inverts (true into false )

