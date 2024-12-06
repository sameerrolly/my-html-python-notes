#Operator overloading :

class data:
      def __init__(self,a,b):
            self.a=a
            self.b=b
            
            
      def __add__(self, other):
        return data(self.a + other.a, self.b + other.b)

      def __str__(self):
        return f"({self.a}, {self.b})"
            
o1=data(10,20)
o2=data(30,40)
o3=data(50,60)
print(o1+o2+o3)
