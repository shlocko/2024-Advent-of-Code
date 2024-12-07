import re

with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

pattern = r'(\d+)\|(\d+)'

rules = {}
jobs_lines = []

def is_valid(job):
    accept = True
    nums = [int(num) for num in job.split(',')]
    for i in range(len(job.split(','))):
        #print(nums[:i])
        #print(rules.get(int(num)))
        if not char_is_valid(nums, i):
            accept = False
    return accept

def char_is_valid(nums, index):
    if rules.get(int(nums[index])) and len(set(nums[:index]).intersection(set(rules.get(int(nums[index]))))) != 0:
        return False
    return True

def get_nums(text: str):
    match = re.search(pattern, text)
    return [int(match.group(1)), int(match.group(2))]

sum = 0

for line in lines:
    if '|' in line:
        [n1, n2] = get_nums(line)
        if rules.get(n1):
            rules[n1].append(n2)
        else:
            rules[n1] = [n2]
    elif ',' in line:
        jobs_lines.append(line)

jobs = filter(lambda job: not is_valid(job), jobs_lines)
print(jobs)


for job in jobs:
    nums = [int(num) for num in job.split(',')]
    rules_count = {}
    for line in lines:
        if '|' in line:
            [n1, n2] = [int(num) for num in line.split('|')]
            if n1 in nums and n2 in nums:
                print([n1, n2])
                if rules_count.get(n1):
                    rules_count[n1][0] += 1
                else:
                    rules_count [n1] = [1, 0]
                if rules_count.get(n2):
                    rules_count[n2][1] += 1
                else:
                    rules_count[n2] = [0, 1]
    for num in nums:
        if rules_count[num][0] == rules_count[num][1]:
            sum += num
print(sum)
