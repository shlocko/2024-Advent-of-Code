
with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip('\n') for line in lines]

height = len(lines)
width = len(lines[0])

pos = tuple[int, int]

def fill(start: pos, region:set[pos]):
    x = start[0]
    y = start[1]
    plot_type = lines[y][x]
    if y > 0 and lines[y-1][x] == plot_type and (x, y-1) not in region:
        region.add((x, y-1))
        fill((x, y-1), region)
    if y < height-1 and lines[y+1][x] == plot_type and (x, y+1) not in region:
        region.add((x, y+1))
        fill((x, y+1), region)
    if x > 0 and lines[y][x-1] == plot_type and (x-1, y) not in region:
        region.add((x-1, y))
        fill((x-1, y), region)
    if x < width-1 and lines[y][x+1] == plot_type and (x+1, y) not in region:
        region.add((x+1, y))
        fill((x+1, y), region)

regions = []

def in_region(loc: pos):
    found = False
    for region in regions:
        if loc in region: found = True
    return found

for y, line in enumerate(lines):
    for x, ch in enumerate(line):
        if not in_region((x, y)):
            region = set()
            region.add((x, y))
            fill((x, y), region)
            regions.append(region)

'''
.#.
.#.
...
'''
def get_dirs(x, y, region, plot_type):
    up = True if y > 0 and lines[y-1][x] == plot_type else False
    down = True if y < height-1 and lines[y+1][x] == plot_type else False
    left = True if x > 0 and lines[y][x-1] == plot_type else False
    right = True if x < width-1 and lines[y][x+1] == plot_type else False
    return up, down, left, right

def fill_dir(x, y, direction, edges, plot_type, region):
    [up, down, left, right] = get_dirs(x, y, region, plot_type)
    if direction == 0:
        if not up:
            edges.add((x, y))
            if right and (x+1, y) not in edges:
                fill_dir(x+1, y, direction, edges, plot_type, region)
            if left and (x-1, y) not in edges:
                fill_dir(x-1, y, direction, edges, plot_type, region)
    if direction == 1:
        if not right:
            edges.add((x, y))
            if up and (x, y-1) not in edges:
                fill_dir(x, y-1, direction, edges, plot_type, region)
            if down and (x, y+1) not in edges:
                fill_dir(x, y+1, direction, edges, plot_type, region)
    if direction == 2:
        if not down:
            edges.add((x, y))
            if left and (x-1, y) not in edges:
                fill_dir(x-1, y, direction, edges, plot_type, region)
            if right and (x+1, y) not in edges:
                fill_dir(x+1, y, direction, edges, plot_type, region)
    if direction == 3:
        if not left:
            edges.add((x, y))
            if up and (x, y-1) not in edges:
                fill_dir(x, y-1, direction, edges, plot_type, region)
            if down and (x, y+1) not in edges:
                fill_dir(x, y+1, direction, edges, plot_type, region)

sum = 0
for region in regions:
    [x, y] = list(region)[0]
    plot_type = lines[y][x]
    top_edges = set()
    right_edges = set()
    down_edges = set()
    left_edges = set()
    sides = 0
    for plot in region:
        #x = plot[0]
        #y = plot[1]
        [x, y] = plot
        [up, down, left, right] = get_dirs(x, y, region, plot_type)
        if not up and (x, y) not in top_edges:
            fill_dir(x, y, 0, top_edges, plot_type, region)
            sides += 1
        if not right and (x, y) not in right_edges:
            fill_dir(x, y, 1, right_edges, plot_type, region)
            sides += 1
        if not down and (x, y) not in down_edges:
            fill_dir(x, y, 2, down_edges, plot_type, region)
            sides += 1
        if not left and (x, y) not in left_edges:
            fill_dir(x, y, 3, left_edges, plot_type, region)
            sides += 1
             
    sum += sides * len(region)

print(sum)
