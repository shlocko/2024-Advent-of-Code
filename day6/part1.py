
with open("input.txt", "r") as file:
    lines = file.readlines()

def to_tup(guard):
    return (guard[0], guard[1])

guard = [0, 0]
for i, line in enumerate(lines):
    if '^' in line:
        guard[0] = line.index('^')
        guard[1] = i


locations = set({to_tup(guard)})

dir = 1

def turn(dir):
    new = (dir+1)%5
    if new == 0: new+=1
    return new

def check_move(guard, dir):
    [x, y] = [guard[0], guard[1]]
    if dir == 1:
        if guard[1] > 0 and lines[y-1][x] != '#':
            return True
    if dir == 2 and guard[0] < len(lines[0])-1 and lines[y][x+1] != '#':
        return True
    if dir == 3 and guard[1] < len(lines)-1 and lines[y+1][x] != '#':
        return True
    if dir == 4 and guard[0] > 0 and lines[y][x-1] != '#':
        return True
    return False

def check_edge(guard, dir):
    [x, y] = [guard[0], guard[1]]
    if dir == 1 and guard[1] == 0 :
            return True
    if dir == 2 and guard[0] == len(lines[0])-1:
        return True
    if dir == 3 and guard[1] == len(lines)-1:
        return True
    if dir == 4 and guard[0] == 0:
        return True
    return False

def move(guard, dir):
    [x, y] = [guard[0], guard[1]]
    if dir == 1:
        guard[1]-=1
    if dir == 2:
        guard[0]+=1
    if dir == 3:
        guard[1]+=1
    if dir == 4:
        guard[0]-=1
    guard = [x, y]

run = True

while run:
    print(guard)
    print(dir)
    print(check_move(guard, dir))
    if check_move(guard, dir):
        move(guard, dir)
        locations.add(to_tup(guard))
    elif check_edge(guard, dir):
        run = False
    else:
        dir = turn(dir)

print(locations)
print(len(locations))
