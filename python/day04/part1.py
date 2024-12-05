import numpy as np
import re

with open('input.txt') as f:
    lines = f.read().splitlines()

def horizontal(lines):
    return lines

def backward(lines):
    return [l[::-1] for l in lines]

def vertical(lines):
    return as_lines(as_numpy(lines).T)

def diagonal(lines):
    lines_numpy = as_numpy(lines)
    height, width = lines_numpy.shape
    for k in range(-height+1, width):
        yield ''.join(np.diag(lines_numpy, k=k))

def anti_diagonal(lines):
    return diagonal(backward(lines))

def as_numpy(lines):
    return np.array([list(l) for l in lines])

def as_lines(numpy_arr):
    return [''.join(n) for n in numpy_arr]

def count_word_in_lines(lines, word='XMAS'):
    count = 0
    for line in lines:
        count += len(re.findall(word, line))

    return count
    
result = count_word_in_lines(horizontal(lines)) + \
    count_word_in_lines(backward(horizontal(lines))) + \
    count_word_in_lines(vertical(lines)) + \
    count_word_in_lines(backward(vertical(lines))) + \
    count_word_in_lines(diagonal(lines)) + \
    count_word_in_lines(backward(diagonal(lines))) + \
    count_word_in_lines(anti_diagonal(lines)) + \
    count_word_in_lines(backward(anti_diagonal(lines)))

print(result)

assert result == 2639