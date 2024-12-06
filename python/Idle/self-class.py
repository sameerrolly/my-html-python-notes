# self in method  :

class emp:
    name="sameer"
    age=23
    def intro(self):
          self.hobby="gym"
          self.work="programmer"
          print(f"I am {self.name} and age is {self.age} ,my hobby is {self.hobby}and i work as a {self.work}")
    def greet(self):
          print(f"welcome {self.name} to AI tech")





id=emp()
print("\tself with classes and Objects :")
id.intro()     #method call with object (id is object and intro is method/functionName)

greets=emp()
print("\t \n greets as object 2")
greets.greet()
