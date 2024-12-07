
with open("input.txt", "r") as file:
    lines = file.readlines()

sum = 0
vals = []
for line in lines:
    [val, nums] = line.split(': ')
    val = int(val)
    nums = [int(num) for num in nums.split(' ')]
    #print(nums)
    b = 0
    while len(bin(b)[2:]) <= len(nums)-1:
        count = nums[0]
        #print(count)
        #print(bin(b)[2:])
        b_str = ('0' * ((len(nums)-1) -len(bin(b)[2:]))) + str(bin(b)[2:])
        #print(b_str)
        for i in range(len(nums)-1):
            #print(b_str[i] + ' ------')
            if b_str[i] == '0':
                count += nums[i+1]
            else:
                count *= nums[i+1]

        if count == val:
            sum += count
            break
        b += 1
        #print('--')



print('-----')
print(sum)
