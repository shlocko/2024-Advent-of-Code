
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

comp_blocks = blocks[:]

done = False

for ob in reversed(blocks):
    if ob[0] == -1: continue
    for k, block in enumerate(comp_blocks):
        if block[0] == -1 and block[1] >= ob[1]:
            comp_blocks.insert(k, ob)
            comp_blocks[k+1][1] -= ob[1]
            break


del_blocks = []
found_ids = []

sum = 0
index = 0
for block in comp_blocks:
    if block[1] <= 0: continue
    if block[0] in found_ids:
        block[0] = -1
    else:
        found_ids.append(block[0])
    for i in range(block[1]):
        if block[0] != -1:
            sum += block[0] * (index)
        index += 1


print(sum)

