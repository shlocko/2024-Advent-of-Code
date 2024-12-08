
with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip('\n') for line in lines]

startx = 0
starty = 0

for i, line in enumerate(lines):
    if '^' in line:
        startx = line.index('^')
        starty = i

def to_tup(guard, dir):
    return (guard[0], guard[1], dir)

def to_tup_base(guard):
    return (guard[0], guard[1])

def turn(dir):
    new = (dir+1)%5
    if new == 0: new+=1
    return new

def check_move(guard, dir, lines):
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

# ---------------------------------------------------------------

guard = [0, 0]
for i, line in enumerate(lines):
    if '^' in line:
        guard[0] = line.index('^')
        guard[1] = i


locations = set({to_tup(guard, dir)})
locations_base = set({to_tup_base(guard)})

dir = 1


run = True

while run:
    if check_move(guard, dir, lines):
        move(guard, dir)
        locations_base.add(to_tup_base(guard))
    elif check_edge(guard, dir):
        run = False
    else:
        dir = turn(dir)
# ---------------------------------------------------------------

def simulate(x, y, lines_orig):

    lines = lines_orig[:]
    lines[y] = lines[y][:x] + '#' + lines[y][x+1:]
    dir = 1
    guard = [startx, starty]
    loop = False


    locations:list[tuple[int, int, int]] = [to_tup(guard, int(dir))]


    run = True

    while run and not loop:
        #print(guard)
        #print(dir)
        #print(check_move(guard, dir))
        if check_move(guard, dir, lines):
            move(guard, dir)
            #print('move')
            #print(to_tup(guard, int(dir)))
            #print(locations)
            if to_tup(guard, int(dir)) in locations:
                #print('loop')
                #print(x)
                #print(y)
                loop = True
                run = False
            locations.append(to_tup(guard, int(dir)))
        elif check_edge(guard, dir):
            run = False
        else:
            dir = turn(dir)
    #print(loop)
    #print(x)
    #print(y)
    return loop
sum = 0
guard_start = [0,0]
for i, line in enumerate(lines):
    if '^' in line:
        guard_start[0] = line.index('^')
        guard_start[1] = i
'''for i in range(len(lines)):
    for n in range(len(lines[0])):
        print(str(n) + ' - ' + str(len(lines[0])) + ' | ' + str(i) + ' - ' + str(len(lines)))
        if [n, i] != guard_start and simulate(n, i, lines):
            sum += 1'''
for i, loc in enumerate(locations_base):
    print(i)
    if [loc[0], loc[1]] != guard_start and simulate(loc[0], loc[1], lines):
        sum += 1
#print(len(lines[0]))
print(sum)

test = set({(1, 1, 1)})
#print((1,1,1) in test)
