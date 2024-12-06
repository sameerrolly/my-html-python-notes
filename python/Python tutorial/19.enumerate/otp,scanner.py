import random 
while True:
    otp=random.randrange(100000 , 1000000)
    print(otp)
    user=int(input("enter a otp "))

    if otp==user:
        print("otp verified ! ")
        break
    else:
        print("denied")