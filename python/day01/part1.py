import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()

left_numbers, right_numbers = np.array([l.split() for l in lines]).astype('int').T

left_numbers.sort()
right_numbers.sort()

result = np.abs(left_numbers - right_numbers).sum()

print(result)

assert result == 2164381