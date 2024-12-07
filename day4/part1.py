with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

def check_dir(x: int, y: int, dx: int, dy: int):
    return lines[y][x] == 'X' and lines[y+dy][x+dx] == 'M' and lines[y+(2*dy)][x+(2*dx)] == 'A' and lines[y+(3*dy)][x+(3*dx)] == 'S'

count = 0

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if x < len(lines[y])-3: # Check right
            if check_dir(x, y, 1, 0): # right stright
                count += 1
            if y > 2:
                if check_dir(x, y, 1, -1): # right up
                    count += 1
            if y < len(lines) - 3:
                if check_dir(x, y, 1, 1): # right down
                    count += 1
        if x > 2: # check left
            if check_dir(x, y, -1, 0): # straight
                count += 1
            if y > 2:
                if check_dir(x, y, -1, -1): # left up
                    count += 1
            if y < len(lines) - 3:
                if check_dir(x, y, -1, 1): # left down
                    count += 1
        if y > 2:
            if check_dir(x, y, 0, -1): # up
                count += 1
        if y < len(lines) - 3:
            if check_dir(x, y, 0, 1): # down
                count += 1

print(count)
