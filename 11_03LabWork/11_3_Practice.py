colors = ["red", "blue", "green", "yellow"]
for c in colors:
    if c == "green":
        print("Found green")
        break
    print(c)
else:
    print("Green not found")   #will not run


nums = [3, 6, 9, 12]
i = 0
while i < len(nums):
    if nums[i] == 9:
        print("Found 9")
        break
    i += 1
else:
    print("9 not found")   # will NOT run because of break
