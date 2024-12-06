#init function practice

#1.create class programmer of storing info of few programmer:

class programmer:
      def __init__(self,n,o):
            self.name=n
            self.occ=o
      def intro(self):
            print(f"Hello! , my name is {self.name} and i work as {self.occ}")
a=programmer("sameer","python programmer")
a.intro()
b=programmer("sahil","java developer")
b.intro()
print("we have two programmers i.e:",a.occ,",",b.occ)

#2. class cal capable of findinf squareroot ,cube and square of a number  :

class calculate:
      def __init__(self,int):
            self.int=int

      def sqr(self):
            print(f"square of given integer is : {self.int**self.int}")
      def cube(self):
            print(f"cube of given integer is: {self.int*self.int*self.int}")
x=calculate(2)
x.cube()
x.sqr()
 
