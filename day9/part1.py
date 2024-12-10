
with open("input.txt", "r") as file:
    lines = file.readlines()

data = lines[0].strip('\n')

def find_next_empty(arr):
    for i, item in enumerate(arr):
        if item[0] == -1:
            return i
    return -1


blocks = []
block_id = 0

empty = False

for ch in data:
    num = int(ch)
    if not empty:
        blocks.append([block_id, num])
        block_id += 1
    else:
        blocks.append([-1, num])
    empty = not empty

print(blocks)

comp_blocks = []

done = False
next = find_next_empty(blocks)
while not done:
    if blocks[0][0] != -1:
        for i in range(blocks[0][1]):
            comp_blocks.append(blocks[0][0])
    else:
        for e in range(blocks[0][1]):
            while len(blocks) != 0 and (blocks[-1][0] == -1 or blocks[-1][1] <= 0):
                blocks = blocks[:-1]
            if len(blocks) > 0:
                comp_blocks.append(blocks[-1][0])
                blocks[-1][1] -= 1
    blocks = blocks[1:]
    next = find_next_empty(blocks)
    #print(blocks)
    #print(comp_blocks)
    if next == -1 and len(blocks) == 0:
        done = True

print(comp_blocks)

sum = 0
for i, num in enumerate(comp_blocks):
    sum += i * num

print(sum)
