#Grandparent classes
class ABC:
    s = "Attribute from ABC"
    def __init__(self):
        print("ABC __init__ called")
    def greet(self):
        print("from class ABC")

class XYZ:
    s = "Attribute from XYZ"
    def __init__(self):
        print("XYZ __init__ called")
    def greet(self):
        print("from class XYZ")

#Parent classes
class ABC1(ABC):
    s = "Attribute from ABC1"
    def __init__(self):
        print("ABC1 __init__ called")
    def greet(self):
        print("from class ABC1")

class XYZ1(XYZ):
    s = "Attribute from XYZ1"
    def __init__(self):
        print("XYZ1 __init__ called")
    def greet(self):
        print("from class XYZ1")

#Child class
class ChildXYZ(ABC1, XYZ1):
    s = "Attribute from ChildXYZ"
    def __init__(self):
        print("ChildXYZ __init__ called")
    def greet(self):
        print("Hello from ChildXYZ")
    def inner(self):
        print("Inner method in ChildXYZ")
    def outer(self):
        print("Outer method called")
        print("Child attribute:", self.s)
        self.inner()
    def call_parent(self):
        print("Access ABC1 attribute:", ABC1.s)
        ABC1.greet(self)

obj = ChildXYZ()
print(obj.s)        
obj.greet()         
obj.outer()        
obj.call_parent()   
