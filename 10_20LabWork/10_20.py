a = "A String"
b = "A String"
print(a is b)          #True, because of string interning, variables point to the same memory location

a = [0,1,2]
print(0 in a)
print(2.0 in a)         #True, because 2.0 is considered equal to 2 in Python
print([0,1] in a)       #False, because [0,1] is a list and not an element of a

print(list(range(10)))
print(list(range(-10)))       #if one parameter, the stop value needs to be greater than start value (0 by default)
print(list(range(5,10)))
print(list(range(5,-2)))
print(list(range(5,-2,-1)))
print(list(range(3,20,2)))
print(list(range(3,20,-2)))  #empty list, because step is negative but start < stop

print(list(range(20, 3,-2)))

print(2&3)
print(2|3)
print(2^3)
print(2<<3)
print(2>>3)
print(-2<<3)



