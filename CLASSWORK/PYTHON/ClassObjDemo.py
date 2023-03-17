"""
    OOP :

    Features of OOP :

    1) Encapsulation
    2) Inheritance
    3) Polymorphism
    4) Abstraction


    Encapsulation : It is an another name of class.

    Class :  It is a collection of Member functions and Data Members.
 
             i.e variable and functions.

    Object : It is an instance of a class.

    Lifecycle of an object.

    1) Creation.
    2) Utilization.
    3) Destruction.

    e.g paper cup

    1) Create
    2) use
    3) destroy
    

"""

class Sample:

    x = 0       
    def __init__(self,f):
        self.x = f
        print()

    def demo(self):
        print("X : ",self.x)

    def evenOdd(self):
        if self.x%2==0:
            print("It is Even ")
        else:
            print("It is Odd")

n = int(input("Enter No. "))
obj = Sample(n)
obj.demo()
obj.evenOdd()














