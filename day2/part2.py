import math
with open("input.txt", "r") as file:
    lines = file.readlines()
count = 0
def is_safe(nums, init_check):
    diffs = []
    for i in range(len(nums)-1):
        diffs.append([nums[i+1] - nums[i], i])
    bad_diffs_i = []

    init_diff = diffs[0][0]
    for i, diff in enumerate(diffs):
        if((math.copysign(1, diff[0]) != math.copysign(1, init_diff)) or (diff[0] == 0) or abs(diff[0]) > 3):
            bad_diffs_i.append(diff[1])
    #print(bad_diffs_i)
    if(len(bad_diffs_i) == 0):
        return True
    if(init_check):
        for i in range(len(nums)):
            newnums = nums[:]
            del newnums[i-1]
            check = is_safe(newnums, False)
            if(check): return True
    return False

for line in lines:
    nums = []
    numstrs = line.split(" ")
    for numstr in numstrs:
        nums.append(int(numstr))
    if(is_safe(nums, True)): count+=1


print(count)


