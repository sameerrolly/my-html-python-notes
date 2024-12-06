#Inheritance :  child class inherits all the datat and objects from parent class .
'''
class parent:
    x=10
    y=20
    z=x+y
class child(parent):
    c=10
r=child()
print(r.x)
print(r.z)
print(r.z+r.c)'''

#-----------------------------------
class emp:
      def __init__(self,fname,lname):
            self.fname=fname
            self.lname=lname
class coder(emp):
      def __init__(self,fname,lname,occ,salary):
            super().__init__(fname,lname)
            self.occupation=occ
            self.salary=salary
            
      def detail(self):
            print(f"my name is {self.fname}{self.lname} and i work as a'{self.occupation }' with salary of {self.salary}")
fname=input("enter first name: ")
lname=input("enter last name: ")
employe1=coder(fname,lname,"python","10k")
employe1.detail()


#--------------------------------------------------------------------------
