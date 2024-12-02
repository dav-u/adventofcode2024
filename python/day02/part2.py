import numpy as np

def check_report(report):
    diffs = np.diff(report)

    # each difference is either strictly positive or negative
    is_strictly_monotonic = np.all(diffs < 0) | np.all(diffs > 0)

    # the absolute differences have to lie between 1 and 3 (including)
    abs_diffs = np.abs(diffs)
    correct_diffs = (abs_diffs.max() <= 3) & (abs_diffs.min() >= 1)

    is_correct = is_strictly_monotonic & correct_diffs

    return is_correct

with open('input.txt') as f:
    lines = f.read().splitlines()

reports = [np.array(l.split(), dtype='int') for l in lines]

correct_count = 0

for report in reports:
    if check_report(report):
        correct_count += 1
        continue

    # problem dampener
    for i in range(len(report)):
        # remove i-th index from (unchanged) report and check again
        candidate = np.delete(report, i)
        if check_report(candidate):
            correct_count += 1
            break

print(correct_count)

assert correct_count == 488