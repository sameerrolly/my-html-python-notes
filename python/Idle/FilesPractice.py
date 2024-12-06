#file input output in python Practice set:

#Problem 1 : wap to read the text from file'poem.txt' and fing twinkle word .
#creating file using write()
p="hey new file practice set \n twinkle little star \n new lines added using write and \creating new file using open and write then |we will append these lines using a(append)mode"
poem=open("poem.txt","w")
print(poem.write(p))
poem.close()

#Now read file
#two ways to read and open :
#1.1st WAY
'''
poem=open("poem.txt")
print(poem.read())
poem.close()'''

#2. 2nd Way : using with statement  to not explicitily close the file 
'''
with open("poem.txt") as poem :
          print(poem.read())
          '''
#find twinkle word apnd print if exist yes or no:

with open("poem.txt") as poem:
    x=poem.read()
    if "twinkle" in x:
        print("yes twinkle exist")
    else:
        print("no , twinkle word not exists")
        
