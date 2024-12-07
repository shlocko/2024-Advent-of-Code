import re

with open("input.txt", "r") as file:
    lines = file.readlines()

pattern = r'(\d+)   (\d+)'

def get_nums(text: str) -> [int, int]:
    match = re.search(pattern, text)
    return [int(match.group(1)), int(match.group(2))]

#print(get_nums(lines[1])[0])

left_nums = []
right_nums = []
for line in lines:
    [n1, n2] = get_nums(line)
    left_loc = 0
    right_loc = 0
    inserted = False
    for i, num in enumerate(left_nums):
        if(num>n1):
            left_nums.insert(i, n1)
            inserted = True
            break
    if(inserted == False): left_nums.append(n1)
    inserted = False
    for i, num in enumerate(right_nums):
        if(num>n2):
            right_nums.insert(i, n2)
            inserted = True
            break
    if(inserted == False): right_nums.append(n2)

total = 0
for i in range(len(left_nums)):
    total += abs(left_nums[i-1] - right_nums[i-1])

print(total) # End Part 1

total = 0
for n1 in left_nums:
    times = 0
    for n2 in right_nums:
        if(n1 == n2): times += 1
    total += n1*times


print(total) # End Part 2
