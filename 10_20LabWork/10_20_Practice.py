x = "Python"
y = "Python"
print(x is y)          #True

numbers = [5, 10, 15, 20]
print(10 in numbers)       #True
print(15.0 in numbers)     #True, float equal to int
print([5,10] in numbers)   #False, list is not an element

print(list(range(3)))      #[0, 1, 2]
print(list(range(2,8)))    #[2,3,4,5,6,7]
print(list(range(8,3,-2))) #[8,6,4]

print(5 & 3)    #1 (0101 & 0011)
print(5 | 3)    #7 (0101 | 0011)
print(5 ^ 3)    #6 (0101 ^ 0011)
print(1 << 4)   #16 (shift left)
print(16 >> 2)  #4  (shift right)
print(-3 << 2)  #-12 (shift left negative)
