
with open("input.txt", "r") as file:
    lines = file.readlines()

input = lines[0].strip('\n')

nums = [int(num) for num in input.split(' ')]

print(nums)

for k in range(11):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = 1
        elif len(str(nums[i])) % 2 == 0:
            strnum = str(nums[i])
            midpoint = len(strnum) // 2
            [first, second] = [strnum[:midpoint], strnum[midpoint:]]
            nums[i] = int(first)
            nums.append(int(second))
        else:
            nums[i] = nums[i] * 2024
    print(nums)

print(len(nums))
