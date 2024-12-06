import numpy as np

with open('test_input.txt') as f:
    lines = f.read().splitlines()

input = np.array([list(l) for l in lines])

def rotate(direction):
    return np.array([-direction[1], direction[0]])

direction = np.array([0, 1])

position = np.where(input == '^')
y, x = position
position = np.array([x[0], y[0]])

print(position)

target_index = position + direction

if target_index[0] < 0 or target_index[0] > input.shape[1]:
    pass

if target_index[1] < 0 or target_index[1] > input.shape[0]:
    pass


