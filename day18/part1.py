import math
import sys
sys.setrecursionlimit(6000)

with open("input.txt", "r") as file:
    lines = file.readlines()

walls: list[tuple[int, int]] = []
for line in lines:
    [x, y] = line.split(',')
    walls.append((int(x), int(y)))

height = 71
width = 71
paths = []

pos = [0, 0]

for y in range(height):
    str = ""
    for x in range(width):
        if (x, y) in walls: str = str + "#"
        else: str = str + "."
    print(str)


def find_dist(x1, y1):
    return math.sqrt((width - x1)**2 + (height - y1)**2)

def walk(x, y, path):
    #print(len(path))
    new_path = set(path)
    new_path.add((x, y))
    #print(x, y)
    if (x, y) == (width, height): 
        paths.append(new_path)
        return
        #return new_path
    if (x, y-1) not in walls and (x, y+1) not in walls and (x-1, y) not in walls and (x+1, y) not in walls:
        min = find_dist(x, y-1)
        dir = (0, -1)
        if x > 0 and find_dist(x-1, y) < min:
            dir = (-1, 0)
            min = find_dist(x-1, y)
        if x < width-1 and find_dist(x+1, y) < min:
            dir = (1, 0)
            min = find_dist(x-1, y)
        if y < height-1 and find_dist(x, y+1) < min:
            dir = (0, 1)
            min = find_dist(x, y+1)
        walk(x+dir[0], y+dir[1], new_path)
        
    else:
        if y > 0 and (x, y-1) not in walls and (x, y-1) not in path:
            walk(x, y-1, new_path)
        if x > 0 and (x-1, y) not in walls and (x-1, y) not in path:
            walk(x-1, y, new_path)
        if y < height and (x, y+1) not in walls and (x, y+1) not in path:
            walk(x, y+1, new_path)
        if x < width and (x+1, y) not in walls and (x+1, y) not in path:
            walk(x+1, y, new_path)
walk(0, 0, set())
print(paths)
short = 99999
for path in paths:
    if len(path) < short: short = len(path)
print(short-1)

'''run = True
count = 0
path: list[list[int]]= []
while run:
    [x, y] = pos
    dir = [0, 0]
    min_dist = 999
    if [x, y] not in path: path.append([x, y])
    else:
        x = path[-2][0]
        y = path[-2][1]
    if y > 0 and [x, y-1] not in walls and [x, y-1] not in path:
        dist = find_dist(x, y-1)
        if dist < min_dist:
            min_dist = dist
            dir = [0, -1]
    if x < width and [x+1, y] not in walls and [x+1, y] not in path:
        dist = find_dist(x+1, y)
        if dist < min_dist:
            min_dist = dist
            dir = [1, 0]
    if y < width and [x, y+1] not in walls and [x, y+1] not in path:
        dist = find_dist(x, y+1)
        if dist < min_dist:
            min_dist = dist
            dir = [0, 1]
    if x > 0 and [x-1, y] not in walls and [x-1, y] not in path:
        dist = find_dist(x-1, y)
        if dist < min_dist:
            min_dist = dist
            dir = [-1, 0]

    x += dir[0]
    y += dir[1]
    pos = [x, y]
    count += 1
    print(path)

    if [x, y] == [width, height]:
        run = False

print(count)

'''
