import re

with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

pattern = r'(\d+)\|(\d+)'

def get_nums(text: str):
    match = re.search(pattern, text)
    return [int(match.group(1)), int(match.group(2))]

sum = 0

rules = {}
jobs_lines = []
for line in lines:
    if '|' in line:
        [n1, n2] = get_nums(line)
        if rules.get(n1):
            rules[n1].append(n2)
        else:
            rules[n1] = [n2]
    elif ',' in line:
        jobs_lines.append(line)

for job in jobs_lines:
    nums = [int(num) for num in job.split(',')]
    accept = True
    for i, num in enumerate(nums):
        #print(nums[:i])
        #print(rules.get(int(num)))
        if rules.get(int(num)) and len(set(nums[:i]).intersection(set(rules.get(int(num))))) != 0:
            accept = False
    if accept:
        num = nums[len(nums)//2]
        sum += num

print(sum)

