import re

with open("input.txt", "r") as file:
    lines = file.read()
    input = lines.split('\n\n')

pattern = r'(\d+)'

matches_reg = re.findall(pattern, input[0])
reg_a = int(matches_reg[0])
reg_b = int(matches_reg[1])
reg_c = int(matches_reg[2])

ins: list[int] = []
out: list[int] = []
pointer: int = 0
run = True
matches_ins = re.findall(pattern, input[1])
for match in matches_ins:
   ins.append(int(match))

def get_combo(operand):
    match operand:
        case 4:
            return reg_a
        case 5:
            return reg_b
        case 6:
            return reg_c
        case _:
            return operand

def process_ins(opcode: int, operand: int, pointer: int, reg_a, reg_b, reg_c):
    match opcode:
        case 0:
            reg_a = reg_a // (2 ** get_combo(operand))
        case 1:
            reg_b = reg_b ^ operand
        case 2:
            reg_b = get_combo(operand) % 8
        case 3:
            if reg_a != 0:
                return operand, reg_a, reg_b, reg_c
        case 4:
            reg_b = reg_b ^ reg_c
        case 5:
            out.append(get_combo(operand)%8)
        case 6:
            reg_b = reg_a // (2 ** get_combo(operand))
        case 7:
            reg_c = reg_a // (2 ** get_combo(operand))
    return (pointer + 2, reg_a, reg_b, reg_c)


while run:
    if pointer >= len(ins): break
    print(pointer)
    [pointer, reg_a, reg_b, reg_c] = process_ins(ins[pointer], ins[pointer+1], pointer, reg_a, reg_b, reg_c)
    
    
strout = ''
for num in out:
    strout += str(num) + ','

print(strout)
