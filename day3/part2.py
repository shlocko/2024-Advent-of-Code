import re

with open("input.txt", "r") as file:
    lines = file.read()

pattern_mul = r'mul\(\d+,\d+\)'
pattern_inner_mul = r'\((\d+),(\d+)\)'
pattern_do = r'do\(\)'
pattern_dont = r'don\'t\(\)'

print(lines)
matches_mul = re.finditer(pattern_mul, lines)

matches_do = list(re.finditer(pattern_do, lines))
matches_dont = list(re.finditer(pattern_dont, lines))

def find_prev_do(pos):
    recent = -1
    for match in matches_do:
        if(match.start() < pos): recent = match.start()
    return recent

def find_prev_dont(pos):
    recent = -1
    for match in matches_dont:
        if(match.start() < pos): recent = match.start()
    return recent

count = 0
for match in matches_mul:
    do = False
    recent_do = find_prev_do(match.start())
    recent_dont = find_prev_dont(match.start())
    print(match.start())

    if(recent_do == -1 and recent_dont == -1):
        do = True
    elif(recent_do > recent_dont):
        do = True
    elif(recent_do < recent_dont):
        do = False
    else:
        print("ERRORERRORERROR")
    print(recent_do)
    print(recent_dont)
    print(do)
    #print(do)
    if(do):
        nums = re.search(pattern_inner_mul, match.group())
        count += int(nums.group(1)) * int(nums.group(2))

print(count)
