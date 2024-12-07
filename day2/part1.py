import math
with open("input.txt", "r") as file:
    lines = file.readlines()
count = 0
for line in lines:
    nums = []
    numstrs = line.split(" ")
    for numstr in numstrs:
        nums.append(int(numstr))
    safe = True
    diffs = []
    for i in range(len(nums)-1):
        diffs.append(nums[i+1] - nums[i])
    safe = len(list(filter(lambda num: abs(num) > 3, diffs))) == 0
    if(not safe): continue
    init_diff = diffs[0]
    safe = len(list(filter(lambda num: (math.copysign(1, num) != math.copysign(1, init_diff)) or (num == 0), diffs))) == 0
    if(safe): count+=1


print(count)


