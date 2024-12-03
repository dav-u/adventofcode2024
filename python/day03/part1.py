import re

with open('input.txt') as f:
    memory = f.read()

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory)

result = 0
for match in matches:
    a, b = match
    result += int(a) * int(b)

print(result)

assert result == 182619815