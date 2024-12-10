
with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip('\n') for line in lines]

width = len(lines[0])
height = len(lines)

pos = tuple[int, int]
def travel_path(start: pos, ends: list[pos]):
    x = start[0]
    y = start[1]
    if start[0] > 0 and int(lines[y][x-1]) == int(lines[y][x]) + 1:
        if lines[y][x-1] == '9':
            ends.append((x-1, y))
        else:
            travel_path((x-1, y), ends)
    if start[0] < width-1 and int(lines[y][x+1]) == int(lines[y][x]) + 1:
        if lines[y][x+1] == '9':
            ends.append((x+1, y))
        else:
            travel_path((x+1, y), ends)
    if start[1] > 0 and int(lines[y-1][x]) == int(lines[y][x]) + 1:
        if lines[y-1][x] == '9':
            ends.append((x, y-1))
        else:
            travel_path((x, y-1), ends)
    if start[1] < height-1 and int(lines[y+1][x]) == int(lines[y][x]) + 1:
        if lines[y+1][x] == '9':
            ends.append((x, y+1))
        else:
            travel_path((x, y+1), ends)
sum = 0
for y, line in enumerate(lines):
    for x, ch in enumerate(line):
        if ch == '0':
            ends = []
            travel_path((x, y), ends)
            sum += len(ends)

print(sum)



