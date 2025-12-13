
class P1:                                                               #grandparent class 1
    s="this is an early defined attribute in Class P1"
    s="this is a later defined attribute in Class P1"
    def __init__(self):                                               #can use other words instead of self, create an object
        print("this is an early defined __init__ method in Class P1")
    def __init__(self):
        print("this is a later defined __init__ method in Class P1")   #override the early defined ___init___ method
    def m(self):
        print("this is an early defined method 1 call in Class P1")


class P2:
    s="this is an early defined attribute in Class P2"
    s="this is a later defined attribute in Class P2"
    def __init__(self):                                               #can use other words instead of self, create an object
        print("this is an early defined __init__ method in Class P2")
    def __init__(self):
        print("this is a later defined __init__ method in Class P2")   #override the early defined ___init___ method
    def m(self):
        print("this is an early defined method 1 call in Class P2")


class P11(P1):                                                          #parent class 1                              
    s="this is an early defined attribute in Class P11"
    s="this is a later defined attribute in Class P11"
    def __init__(self):                                               #can use other words instead of self, create an object
        print("this is an early defined __init__ method in Class P11")
    def __init__(self):
        print("this is a later defined __init__ method in Class P11")   #override the early defined ___init___ method
    def m(self):
        print("this is an early defined method 1 call in Class P11")

class P21(P2):
    s="this is an early defined attribute in Class P21"
    s="this is a later defined attribute in Class P21"
    def __init__(self):                                               #can use other words instead of self, create an object
        print("this is an early defined __init__ method in Class P21")
    def __init__(self):
        print("this is a later defined __init__ method in Class P21")   #override the early defined ___init___ method
    def m(self):
        print("this is an early defined method 1 call in Class P21")

class P(P11, P21):
    s="this is an early defined attribute in Class P"
    s="this is a later defined attribute in Class P"
    def __init__(self):                                               #can use other words instead of self, create an object
        print("this is an early defined __init__ method in Class P")
    def __init__(self):
        print("this is a later defined __init__ method in Class P")   #override the early defined ___init___ method
    def m(self):
        print("this is a later defined method call in Class P")
    def m1(self):
        print("this is inner method call in Class P")
    def m2(self):
        print("this is outer method call in Class P")
        print(self.s)                                                   #self represents the instance/object itself
        self.m1()                                                       #call inner method via self
    def m3(self):
        print(P.s)
        P.m2(self)
    #pass
#if we comment out all the later defined methods and attributes, the earlier defined methods and attributes in the class and parent classes will be used
#if we comment out P(P11, P21), the first parent class P11 will be used, because first father has higher priority than second father. Priority order: class itself > first parent class > second parent class > first grandparent class > second grandparent class.
#if we comment out P11(P1), the first grandparent class P1 will be used 
#if we comment out P21(P2), the second grandparent class P2 will be used
o1=P()
print(o1.s)                                                             #access attribute via object
o1.m()
"""o1.m2()                                                                 #call method via object, access method outside the class
o1.m3
print(P.s)
P.m2(o1)   """                                                             #method needs oject name, need to pass the object as parameter
#P.m2(self)                                                             #error, self is not defined outside the class, need to pass the object as parameter
