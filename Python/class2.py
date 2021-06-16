class Dogs():
    # Class variables applt to all instances of a class. ie: kind
    # instance variables apply to a particular instance of a class. denoted with"self.*"
    # If same name occurs in both instance and class, name lookup prioritiezes the instance 
    # name(the one with self.*)
    # Inheritance
    # class DerivedClassName(modulename.BaseClassName):
    # DerivedClassName() would create a new instance of the derived class
    # When methds of derived class references, it first checks derived class and then base class and then where the
    # base class was derived from and so on
    # Derived classes may override methods of their base classes.
    # To check instances type: isinstance(obj, int) will be True only if obj.__class__ is int or some class 
    # derived from int.
    # to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, 
    # issubclass(float, int) is False since float is not a subclass of int.
    # Private variables dont exist in python classes but by convention, names prefixed 
    # with an underscore (e.g. _spam) should be treated as a non-public part of the API.
    kind  = "canine"
    def __init__(self):
        self.dog1 = "Fido"
        self.dog2 = "Elmo"
    def print3(self):
        print(f"Print3 function in class to print dog3s name: {self.dog3}")

    def printdogs(self):
        print(f"Dogs names for {self} are {self.dog1} and {self.dog2}")
    def namechange(self, newname, num):
        if (num ==1):
            self.dog1 = newname
        else:
            self.dog2 = newname
        

def main():
    # families get assigned dog object
    family1 = Dogs()
    family2 = Dogs()
    print("Before change: Main family1 print dogs: ")
    family1.printdogs()
    print("Before Change: Main family2 print dogs: ")
    family2.printdogs()
    
    family1.namechange("F1Fido",1)
    family2.namechange("F2Elmo", 2)
    print("After change: family1 print dogs: ")
    family1.printdogs()
    print("After change: family2 print dogs: ")
    family2.printdogs()
    Dogs.printdogs(family2)
    family1.printdogs()
    family1.dog3 = "F1Dog3"
    print ("family 1 dog 3:",family1.dog3)
    family1.print3()
    Dogs.printdogs(family2)

    




if __name__ == "__main__":
    main()