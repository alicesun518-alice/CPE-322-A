def f1():
    print("this is f1()")
f1()
print("###################")
def f2(a, b, c, d):
    print(a, b, c, d)
    print("this is f2(a,b,c,d)")
f2('a', 'b', 'c', 'd')              #positional arguments, order matters
f2(d="d", b="b", a="a", c="c")      #keyword arguments, order can be changed
f2("a", "b", d="d", c="c")   #mix positional and keyword arguments, positional need to be first
print("###################")
def f3(*t):
    for x in t:
        print(x)
    #print(t[0])
    print(t)
f3()                     #no argument, empty tuple
f3('a', 'b', 'c', 'd')   #pack multiple arguments into a tuple
#f3(d="d", b="b", a="a", c="c")      
#f3("a", "b", d="d", c="c")
print("###################")
def f4(**d):
    for x in d:
        print(x)
    print(d)                        #output whole dictionary
f4()
#f4('a', 'b', 'c', 'd')             #no keyword arguments, error
#f4("a", "b", d="d", c="c")         #mix positional and keyword arguments, error
f4(d="d", b="b", a="a", c="c")      #pack multiple keyword arguments into a dictionary
print("###################")
def f5(a,b,c,d,*t):
    print(a,b,c,d)
    for x in t:
        print(x)
    print(t)
f5('a', 'b', 'c', 'd')                     #no extra arguments, empty tuple, at least 4 positional arguments/values are needed
f5("a", "b", d="d", c="c")         #mix positional and keyword arguments, positional need to be first
f5(d="d", b="b", a="a", c="c")      #pack multiple keyword arguments into a dictionary
#f5("a", "b", 'e', 'f', "d", c="c")  #mix positional and keyword arguments, positional need to be first
f5('e', 'f', "b", "a", "d", "d")   #mix positional and keyword arguments, positional need to be first
print("###################")
def f6(a,b,c,d,**dic):
    print(a,b,c,d)
    for x in dic:
        print(x)
    print(dic)
f6('a', 'b', 'c', 'd', e='e', f='f')                     #no extra keyword arguments, empty dictionary, at least 4 positional arguments/values are needed
def f7(*t,**dic):
    for x in t:
        print(x)
    print(t)
    for x in dic:
        print(x)
    print(dic)
f7('a', 'b', 'c', 'd', e='e', f='f')
print("###################")
def f8(a,b,c,d,*t,**dic):
    print(a,b,c,d)
    print(t)
    print(dic)
f8(1,2,3,4,5,6,7,8,9, e=1, f=2, g=3)