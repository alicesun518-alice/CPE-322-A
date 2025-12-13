#Variables
x = 10
y = 5.6
z = 1 + 4j
b = False
s = "Hi"
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(b, type(b))
print(s, type(s))


#List
my_list = [4, "hi", 2.1, False]
my_list[1] = "Python"
print(my_list)
print("First:", my_list[0], "Last:", my_list[-1])

#Tuple
my_tuple = (1, 2, "Hi")
print("Second element:", my_tuple[1])
print("Length:", len(my_tuple))

#Set
my_set = {1, 2, 2, 3}
my_set.add(4)
my_set.remove(2)
print(my_set)

#Dictionary
my_dict = {"name": "Alice", "age": 20}
my_dict["age"] = 21
my_dict["city"] = "NY"
print(my_dict)
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
