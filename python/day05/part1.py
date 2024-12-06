import re
import numpy as np

with open('input.txt') as f:
    input = f.read()

ordering_section, update_section = input.split('\n\n')

def parse_rules(rule_lines: list[str]):
    rules = []
    for rule_line in rule_lines:
        match = re.match(r'(\d+)\|(\d+)', rule_line)
        dependency = int(match.group(1))
        dependant = int(match.group(2))

        rules.append((dependency, dependant))

    return np.array(rules)

parsed_rules = parse_rules(ordering_section.splitlines())

updates = [list(map(int, l.split(','))) for l in update_section.splitlines()]

def is_valid_update(update: list[int]) -> bool:
    # extract relevant rules (only where with x|y x is contained in update)
    relevant_rules = parsed_rules[np.isin(parsed_rules[:, 0], update)]

    printed_pages = set()
    for page in update:
        page_dependencies = set(relevant_rules[relevant_rules[:, 1] == page][:, 0])
        if not page_dependencies.issubset(printed_pages):
            return False
        printed_pages.add(page)
    
    return True

result = 0

for update in updates:
    if not is_valid_update(update): continue

    result += update[len(update) // 2]

print(result)

assert result == 4924