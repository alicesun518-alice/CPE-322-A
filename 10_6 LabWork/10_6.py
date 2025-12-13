# This is inline comment
"""This is also inline comment"""
"""This 
        is 
            a multi line 
                comment"""
a=1
print(a)            #declaration
print(type(a))
b=int(2)            #constructor
print(b)
print(type(b))
c=1.2
print(c)
print(type(c))
d=float(2.3)
print(d)
print(type(d))
e=4+5j              #connector, complex number
print(e)
print(type(e))
f=complex(5+6j)     #give value directly
print(f)
print(type(f))
g=complex(6, 7)     #don't have to give j, first value is real part, second is imaginary part
print(g)
print(type(g))

h=None              #null value, note: None is case sensitive
print(h)
print(type(h))
i=True              #boolean value, Truth or False
print(i)
print(type(i))
j=bool(False)
print(j)
print(type(j))
j=bool()
print(j)
print(type(j))
j=bool(0)            #0 is false, any non zero value is true
print(j)
print(type(j))
j=bool(" ")          #string not empty, has a space so: true
print(j)
print(type(j))
j=bool('')           #empty string is false
print(j)
print(type(j))

k="This is a string"
print(k)
print(type(k))
k=str("from the function str()")        #can also be single quote ' ' 
print(k)
print(type(k))      

l=[1, 1.2, 1+1j, None, False, 1.2]      #list
l[3] = "new value"
print(l[3])                             #accessing the 4th element
print(type(l[3]))
print(l)
print(type(l))

t = (1, 1.2, 1+1j, None, False, 1.2)     #tuple
print(t[4])
print(type(t[4]))
print(t)
print(type(t))

s = {int(1), 1.2, 1+1j, None, True, 1.2}     #set of unique elements, unordered! unindexed!!! true is merged with 1***
    # print(s[4])                            Illegal! cannot access by index, will give error
print(s)                                 #duplicate 1.2 is merged
print(type(s))

d= {1:False, 1:False, 1:"New String", 2:False, True:"String"}           #dictionary, key:value pair
# duplicate keys are merged, only last value is kept, values are updated
print(d)
print(type(d))
