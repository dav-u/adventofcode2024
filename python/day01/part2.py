import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()

left_numbers, right_numbers = np.array([l.split() for l in lines]).astype('int').T

left_counts = np.unique(left_numbers, return_counts=True)
right_counts = np.unique(right_numbers, return_counts=True)
left_counts_dict = {number: count for number, count in np.array(left_counts).T}
right_counts_dict = {number: count for number, count in np.array(right_counts).T}

similarity_score = 0

for number, left_count in left_counts_dict.items():
    right_count = right_counts_dict.get(number, 0)
    value = right_count * left_count * number

    similarity_score += value

print(similarity_score)

assert similarity_score == 20719933