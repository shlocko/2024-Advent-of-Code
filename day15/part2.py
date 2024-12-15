
with open("input.txt", "r") as file:
    input = file.read()
    [map, actions] = input.split('\n\n')

actions = actions.replace('\n', '')
map = map.split('\n')

pos = list[int]

walls: list[pos] = []
boxes: list[list[pos]] = []
robot: pos = [0, 0]

for y, line in enumerate(map):
    for x, ch in enumerate(line):
        if ch == '#':
            walls.append([x*2, y])
            walls.append([(x*2)+1, y])
        if ch == 'O':
            boxes.append([[x*2, y], [(x*2)+1, y]])
        if ch == '@': robot = [x*2, y]


def check_box(x, y):
    for box in boxes:
        if [x, y] == box[0] or [x, y] == box[1]:
            return box
    return False

def check_up(x, y, box_list):
    box = check_box(x, y)
    if box and box not in box_list:
        box_list.append(box)
        return check_up(box[0][0], box[0][1]-1, box_list) and check_up(box[1][0], box[1][1]-1, box_list)
    elif [x, y] in walls:
        return False
    else:
        return True


def check_down(x, y, box_list):
    box = check_box(x, y)
    if box and box not in box_list:
        box_list.append(box)
        return check_down(box[0][0], box[0][1]+1, box_list) and check_down(box[1][0], box[1][1]+1, box_list)
    elif [x, y] in walls:
        return False
    else:
        return True

def check_right(x, y, box_list):
    box = check_box(x, y)
    if box:
        box_list.append(box)
        return check_right(box[1][0]+1, box[1][1], box_list)
    elif [x, y] in walls:
        return False
    else:
        return True


def check_left(x, y, box_list):
    box = check_box(x, y)
    if box:
        box_list.append(box)
        return check_left(box[0][0]-1, box[0][1], box_list)
    elif [x, y] in walls:
        return False
    else:
        return True


def move(dir, box_list):
    robot[0] += dir[0]
    robot[1] += dir[1]
    for box_pos in box_list:
        box = boxes.index(box_pos)
        for half in boxes[box]:
            half[0] += dir[0]
            half[1] += dir[1]
            


for ch in actions:
    box_list: list[list[pos]] = []
    if ch == '^':
        if check_up(robot[0], robot[1]-1, box_list):
            move((0, -1), box_list)
    if ch == '>':
        if check_right(robot[0]+1, robot[1], box_list):
            move((1, 0), box_list)
    if ch == 'v':
        if check_down(robot[0], robot[1]+1, box_list):
            move((0, 1), box_list)
    if ch == '<':
        if check_left(robot[0]-1, robot[1], box_list):
            move((-1, 0), box_list)
print(walls)
print(boxes)
print(robot)

sum = 0
for box in boxes:
    sum += ((box[0][1])*100) + (box[0][0])

print(sum)
