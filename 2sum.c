nums = [2,7,11,15]
target = 9

for i in nums:
    for j in nums:
        temp = 0
        temp = i+j
        print("1. ",temp)
        if(temp == target):
            break
print("2. ",temp)