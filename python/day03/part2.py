import re

with open('input.txt') as f:
    memory = f.read()

matches = re.findall(r"(don't)|(do)|mul\((\d{1,3}),(\d{1,3})\)", memory)

result = 0
active = True

for match in matches:
    dont, do, a, b = match

    if len(do) > 0:
        active = True
        continue

    if len(dont) > 0:
        active = False
        continue

    if not active:
        continue

    result += int(a) * int(b)

print(result)

assert result == 80747545