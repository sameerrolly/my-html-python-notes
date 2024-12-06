# classmethod is used for printing the actual instance value after new object instance is created.
class method:
    a=10   #class instance

    def old(self):
        print(f"value of a :{self.a}") #will print object instance
    @classmethod
    def classmethod(self):
        print("value of a after @classmethod decorator: ",self.a)  #will print actual value of class instance
    
x=method()
x.a=20     #object instance created
x.classmethod()
x.old()

