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

def correct_update(update: list[int]) -> tuple[bool, list[int]]:
    new_update = []
    reordered_update = False # stays false if we do not change the update

    # Move the first page from update to new_update that has no missing dependencies.
    # Repeat until update is empty
    # This is far from optimal but it works...
    # Instead we could build some kind of dependency graph.
    while len(update) > 0:
        for i, page in enumerate(update):
            relevant_rules = parsed_rules[np.isin(parsed_rules[:, 0], update)]
            page_dependencies_count = len(relevant_rules[relevant_rules[:, 1] == page][:, 0])
            if page_dependencies_count == 0:
                new_update.append(page)
                update.remove(page)
                if i > 0: reordered_update = True
                break
    
    return reordered_update, new_update

result = 0

for update in updates:
    changed_update, update = correct_update(update)
    if not changed_update: continue
    
    result += update[len(update) // 2]

print(result)

assert result == 6085