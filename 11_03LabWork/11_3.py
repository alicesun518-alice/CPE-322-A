#while loops
i = 1
while i <= 5:
    print(i)
    i += 1

i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop completed")

#stop loop with break if i equals 3
i = 1
while i <= 5:
    if i == 3:
        print("Breaking at", i)
        break
    print(i)
    i += 1
else:
    print("This will not run because loop ended with break")

i = 1
while i <= 5:
    i += 1
    if i == 2:
        continue  # skip this iteration
    print(i)
    
i = 1
while i <= 5:
    i += 1
    if i == 2:
        continue  # skip this iteration
    print(i)



#For Loop
for i in range(1, 6):
    if i == 2:
        continue
    print(i)
    if i == 4:
        break
else:
    print("Loop completed")
