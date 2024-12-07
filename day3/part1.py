import re

with open("input.txt", "r") as file:
    lines = file.readlines()


pattern = r'mul\(\d+,\d+\)'
pattern2 = r'\((\d+),(\d+)\)'

matches = []
for line in lines:
    matches.append(re.findall(pattern, line))

count = 0
for matchlist in matches:
    for match in matchlist:
        nums = re.search(pattern2, match)
        count += int(nums.group(1)) * int(nums.group(2))


print(count)
