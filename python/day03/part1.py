import re

with open('test_input.txt') as f:
    memory = f.read()

print(re.match(r"mul\((\d{1,3}),(\d{1,3})\)", memory))