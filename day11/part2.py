
with open("input.txt", "r") as file:
    lines = file.readlines()

input = lines[0].strip('\n')

numsplit = [int(num) for num in input.split(' ')]

nums = {}

for num in numsplit:
    if num in nums:
        nums[num] += 1
    else: nums[num] = 1

print(nums)
for i in range(75):
    new_nums = {}
    for k, v in nums.items():
        if k == 0:
            if 1 in new_nums: new_nums[1] += v
            else: new_nums[1] = v
        elif len(str(k)) % 2 == 0:
            numstr = str(k)
            midpoint = len(numstr) // 2
            [first, second] = [numstr[:midpoint], numstr[midpoint:]]
            first = int(first)
            second = int(second)
            if first in new_nums:
                new_nums[first] += v
            else:
                new_nums[first] = v
            if second in new_nums:
                new_nums[second] += v
            else:
                new_nums[second] = v
        else:
            newnum = k * 2024
            if newnum in new_nums: new_nums[newnum] += v
            else: new_nums[newnum] = v
    nums = new_nums.copy()
    print(nums)


total = 0
for k, v in nums.items():
    total += v
print(total)
