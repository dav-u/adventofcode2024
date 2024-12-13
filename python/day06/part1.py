import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()

input = np.array([list(l) for l in lines])
visited_points = np.zeros(input.shape)

def rotate(direction):
    return np.array([-direction[1], direction[0]])

direction = np.array([0, -1])

position = np.where(input == '^')
y, x = position
position = np.array([x[0], y[0]])
visited_points[position[1], position[0]] = 1

print(position)

while True:
    target_index = position + direction

    if target_index[0] < 0 or target_index[0] >= input.shape[1]:
        break

    if target_index[1] < 0 or target_index[1] >= input.shape[0]:
        break

    if input[target_index[1], target_index[0]] == '#':
        direction = rotate(direction)
    else:
        position = target_index
        visited_points[position[1], position[0]] = 1

result = np.count_nonzero(visited_points)
print(result)

assert result == 5162