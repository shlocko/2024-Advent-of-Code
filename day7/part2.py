
with open("input.txt", "r") as file:
    lines = file.readlines()

def to_base3(n):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % 3))
        n //= 3
    return ''.join(reversed(digits))

sum = 0
vals = 0
for line in lines:
    [val, nums] = line.split(': ')
    val = int(val)
    nums = [int(num) for num in nums.split(' ')]
    #print(nums)
    b = 0
    while len(to_base3(b)) <= len(nums)-1:
        count = nums[0]
        #print(count)
        #print(bin(b)[2:])
        b_str = ('0' * ((len(nums)-1) -len(to_base3(b)))) + str(to_base3(b))
        #print(b_str)
        for i in range(len(nums)-1):
            #print(b_str[i] + ' ------')
            if b_str[i] == '0':
                count += nums[i+1]
            elif b_str[i] == '1':
                count *= nums[i+1]
            else:
                count = int(str(count)+str(nums[i+1]))

        if count == val:
            sum += count
            vals+=1
            print(vals)
            break
        b += 1
        #print('--')



print('-----')
print(sum)
