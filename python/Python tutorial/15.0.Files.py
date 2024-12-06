# #1.  Open() and read():
# f=open("15.1 demo.txt","r")   #open
# print(f.read())               #read
# f.close()                     #close

# #2.write():
# msg="Demo file msg"
# f=open("15.1 demo.txt","w")  #open with w(write) mode
# print(f.write(msg))          #write
# f.close()                    #close


# # 3. readlines and readline function
# f=open("demo1.txt","w")
# msg1="creating a new file using open and write "
# # print(f.write(msg1))
# # f.close()

# f=open("demo1.txt")
# # print("1st line using readline() function: ",f.readline())
# line=f.readlines()
# print(line,type(line))
# f.close()

# # append
# f=open("demo1.txt","a")
# m="new lines added using append \n now use read()"
# print(f.write(m))
# f.close()

# with statement no need to use  close(): 

with open("demo1.txt") as files:
    # msgs="with statement is useful and no need to explicitily close the file"
    print(files.read())

