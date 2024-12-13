from sympy import Matrix
import re

with open("input.txt", "r") as file:
    lines = file.read()

data = lines.split('\n\n')
pattern = r'(\d+)'

sum = 0

for line in data:
    match = re.findall(pattern, line)
    A = Matrix([
        [match[0], match[2], match[4]],
        [match[1], match[3], match[5]]
    ])
    rref_matrix, pivot_columns = A.rref()
    sol = rref_matrix.col(2)
    if sol[0] == round(sol[0]) and sol[1] == round(sol[1]):
        sum += (sol[0] * 3) + (sol[1])

print(sum)
