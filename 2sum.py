import sys
nums = [2,7,11,15]
target = 9

found = False
for i in nums:
    for j in nums:
        temp = i + j
        if temp == target:
            found = True
            break
    if found:
        break

if found:
    print("Found")
else:
    print("Not found")