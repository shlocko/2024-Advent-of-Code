
with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip('\n') for line in lines]

height = len(lines)
width = len(lines[0])

antennas = {}
antinodes: set[tuple[int, int]] = set({})

for i, line in enumerate(lines):
    for k, ch in enumerate(line):
        if ch == '.':
            continue
        if ch in antennas:
            antennas[ch].append((k, i))
        else:
            antennas[ch] = [(k, i)]

print(antennas)

for signal, locs in antennas.items():
    if len(locs) > 1:
        for loc in locs:
            antinodes.add(loc)
    for loc in locs:
        for loc2 in locs:
            if loc == loc2: continue
            dx = loc2[0] - loc[0]
            dy = loc2[1] - loc[1]
            ax = loc2[0] + dx
            ay = loc2[1] + dy
            while ax >= 0 and ax < width and ay >= 0 and ay < height:
                antinodes.add((ax, ay))
                ax += dx
                ay += dy
                print(str(ax) + ', ' + str(ay))

print(len(antinodes))
