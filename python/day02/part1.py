import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()

reports = [np.array(l.split(), dtype='int') for l in lines]

correct_count = 0

for report in reports:
    diffs = np.diff(report)

    # each difference is either strictly positive or negative
    is_strictly_monotonic = np.all(diffs < 0) | np.all(diffs > 0)

    # the absolute differences have to lie between 1 and 3 (including)
    abs_diffs = np.abs(diffs)
    correct_diffs = (abs_diffs.max() <= 3) & (abs_diffs.min() >= 1)

    is_correct = is_strictly_monotonic & correct_diffs
    # print(report, diffs, is_strictly_monotonic, correct_diffs, is_correct)

    if is_correct:
        correct_count += 1

print(correct_count)

assert correct_count == 432