
with open("input.txt", "r") as file:
    input = file.read()
    [map, actions] = input.split('\n\n')

actions = actions.replace('\n', '')
map = map.split('\n')

pos = list[int]

walls: list[pos] = []
boxes: list[pos] = []
robot: pos = [0, 0]

for y, line in enumerate(map):
    for x, ch in enumerate(line):
        if ch == '#': walls.append([x, y])
        if ch == 'O': boxes.append([x, y])
        if ch == '@': robot = [x, y]

def check_boxes(x, y, dir, box_line):
    if [x, y] in boxes:
        box_line.append([x, y])
        return check_boxes(x+dir[0], y+dir[1], dir, box_line)
    elif [x, y] in walls:
        return False
    else:
        return True

def move(dir, box_line):
    robot[0] += dir[0]
    robot[1] += dir[1]
    for box_pos in box_line:
        box = boxes.index(box_pos)
        boxes[box][0] += dir[0]
        boxes[box][1] += dir[1]

for ch in actions:
    box_line: list[pos] = []
    if ch == '^':
        if check_boxes(robot[0], robot[1]-1, (0, -1), box_line):
            move((0, -1), box_line)
    if ch == '>':
        if check_boxes(robot[0]+1, robot[1], (1, 0), box_line):
            move((1, 0), box_line)
    if ch == 'v':
        if check_boxes(robot[0], robot[1]+1, (0, 1), box_line):
            move((0, 1), box_line)
    if ch == '<':
        if check_boxes(robot[0]-1, robot[1], (-1, 0), box_line):
            move((-1, 0), box_line)

print(walls)
print(boxes)
print(robot)

sum = 0
for box in boxes:
    sum += ((box[1])*100) + (box[0])

print(sum)
print(len(boxes))
