import numpy as np
import re

with open('input.txt') as f:
    lines = f.read().splitlines()

def as_numpy(lines):
    return np.array([list(l) for l in lines])

def is_x_subgrid(subgrid, word='MAS'):
    diagonal = ''.join(np.diag(subgrid))
    anti_diagonal = ''.join(np.diag(np.fliplr(subgrid)))
    
    diagonal_backwards = diagonal[::-1]
    anti_diagonal_backwards = anti_diagonal[::-1]

    is_diagonal_valid = diagonal == word or diagonal_backwards == word
    is_anti_diagonal_valid = anti_diagonal == word or anti_diagonal_backwards == word

    return is_diagonal_valid and is_anti_diagonal_valid

def grid_window(lines, window_size=3):
    lines_numpy = as_numpy(lines)
    height, width = lines_numpy.shape
    for x in range(width - window_size + 1):
        for y in range(height - window_size + 1):
            subgrid = lines_numpy[y:y+window_size, x:x+window_size]
            yield subgrid

def count_x_grids(lines):
    count = 0

    for subgrid in grid_window(lines):
        if is_x_subgrid(subgrid):
            count += 1
    
    return count

x_mas_count = count_x_grids(lines)

print(x_mas_count)

assert x_mas_count == 2005