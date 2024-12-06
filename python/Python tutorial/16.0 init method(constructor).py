#initialization in classes and method using __init__() function.
'''
This is also known as CONSTRUCTOR
'''

#1. BASIC CLASS SYNTAX:
'''
class person:
      name="rolly"
      job="python programming"

      def intro(self):
            print("object1 : ",f"Welcome! {self.name} with skills of {self.job}")
      def praise(new):
            print("object2 : ",f"we are greatful to have you {new.name} Sir!.")
obj=person()
obj.intro()

obj2=person()
obj2.name="SAMEER"
obj2.praise()

#2. __init__() function /dunder method : PRINT EVERYTIME WHEN OBJECT IS CREATED .

class new:
      def __init__(self):
            print(" Dunder method __init__() function :Print every time when an object is created ")      
a=new()
b=new()
'''
#3.__init__() function  WITH attributes:

class emp():
      def __init__(self,n,s):   # n and s are attributes initialized with self.name and self.salary
            self.name=n
            self.salary=s
      def intro(self):
            print(f"Welcome {self.name} in webtech your salary is {self.salary}")
a=emp("Lucky","1 million") #class emp()with arguments n="lucky" and s="1 million"  arguments in intialization will be placed when an object is created
a.intro()
b=emp("sahil",1000000)
b.intro()

print("\n Note:  when an object is created, pass the arguments which are placed in dunder method ")
