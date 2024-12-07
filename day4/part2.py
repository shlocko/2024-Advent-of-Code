with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

def check_m_m(x: int, y: int):
    return lines[y+1][x+1] == 'A' and lines[y+2][x+2] == 'S' and lines[y+2][x] == 'S'

def check_m_s(x: int, y: int):
    return lines[y+1][x+1] == 'A' and lines[y+2][x+2] == 'S' and lines[y+2][x] == 'M'

def check_s_m(x: int, y: int):
    return lines[y+1][x+1] == 'A' and lines[y+2][x+2] == 'M' and lines[y+2][x] == 'S'

def check_s_s(x: int, y: int):
    return lines[y+1][x+1] == 'A' and lines[y+2][x+2] == 'M' and lines[y+2][x] == 'M'

count = 0

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if x < len(lines[y])-2 and y < len(lines) - 2:
            char1 = lines[y][x]
            char2 = lines[y][x+2]
            if char1 == 'M':
                if char2 == 'M':
                    if check_m_m(x, y): count += 1
                if char2 == 'S':
                    if check_m_s(x, y): count += 1
            if char1 == 'S':
                if char2 == 'M':
                    if check_s_m(x, y): count += 1
                if char2 == 'S':
                    if check_s_s(x, y): count += 1

print(count)
