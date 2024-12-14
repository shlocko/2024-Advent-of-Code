import re

with open("input.txt", "r") as file:
    lines = file.readlines()

width = 101
height = 103

pattern = r'(-?\d+)'

robots = []

for line in lines:
    matches = re.findall(pattern, line)
    robots.append([[int(matches[0]), int(matches[1])], [int(matches[2]), int(matches[3])]])


for i in range(100):
    for robot in robots:
        robot[0][0] += robot[1][0]
        robot[0][1] += robot[1][1]
        if robot[0][0] > width - 1:
            robot[0][0] -= width
        if robot[0][0] < 0:
            robot[0][0] += width
        if robot[0][1] > height - 1:
            robot[0][1] -= height
        if robot[0][1] < 0:
            robot[0][1] += height

q1 = 0
q2 = 0
q3 = 0
q4 = 0
for robot in robots:
    x = robot[0][0]
    y = robot[0][1]
    if x < width//2 and y < height//2: q1 += 1
    elif x > (width//2) and y < height//2: q2 += 1
    elif x < width//2 and y > (height//2): q3 += 1
    elif x > (width//2) and y > (height//2): q4 += 1

print(q1 * q2 * q3 * q4)
