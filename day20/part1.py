import sys
sys.setrecursionlimit(10000)

with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]

start = (89, 87)
#print(lines[start[1]][start[0]])
height = 141
width = 141

#start =(1, 3)
#height = 15
#width = 15
end = (111, 85)


nums = {}
visited = []
cheats = []

count = 1
def race(x, y, count, visited):
    #print(nums)
    nums[(x, y)] = count
    visited.append((x,y))

    if y > 1 and lines[y-2][x] == '.':
        cheats.append([(x, y), (x, y-2)])
    if y < height-2 and lines[y+2][x] == '.':
        cheats.append([(x, y), (x, y+2)])
    if x > 1 and lines[y][x-2] == '.':
        cheats.append([(x, y), (x-2, y)])
    if x < width-2 and lines[y][x+2] == '.':
        cheats.append([(x, y), (x+2, y)])


    if lines[y-1][x] == '.' and (x, y-1) not in visited:
        race(x, y-1, count+1, visited)
    if lines[y+1][x] == '.' and (x, y+1) not in visited:
        race(x, y+1, count+1, visited)
    if lines[y][x-1] == '.' and (x-1, y) not in visited:
        race(x-1, y, count+1, visited)
    if lines[y][x+1] == '.' and (x+1, y) not in visited:
        race(x+1, y, count+1, visited)

race(start[0], start[1], count, visited)
#print(cheats)
cheat_dist = {}

for cheat in cheats:
    #print(cheat, nums[cheat[0]]-nums[cheat[1]])
    dist = nums[cheat[0]]-nums[cheat[1]] - 2
    #print(dist)
    if dist > 0:
        if dist in cheat_dist:
            cheat_dist[dist] += 1
        else:
            cheat_dist[dist] = 1

print(cheat_dist)

sum = 0
for dist, c in cheat_dist.items():
    if dist >= 100:
        sum += c
print(sum)
