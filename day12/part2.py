
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

sum = 0
for region in regions:
    [x, y] = list(region)[0]
    plot_type = lines[y][x]
    top_edges = set()
    right_edges = set()
    down_edges = set()
    left_edges = set()
    for plot in region:
        up = True if y > 0 and lines[y-1][x] == plot_type else False
        down = True if y < height-1 and lines[y+1][x] == plot_type else False
        left = True if x > 0 and lines[y][x-1] == plot_type else False
        right = True if x < width-1 and lines[y][x+1] == plot_type else False
