
filename = 'day5/day5.txt'


with open(filename, mode='r') as file:
    sections = file.read().strip().split("\n\n")

    rules = [tuple(map(int, rule.split('|'))) for rule in sections[0].split('\n')]

    updates = [list(map(int, update.split(',')))  for update in sections[1].split('\n')]


valid_updates = []
invalid_updates = []

for update in updates:
    valid = True
    for rule in rules:
        num1, num2 = rule
        if num1 in update and num2 in update:
            pos_num1 = update.index(num1)
            pos_num2 = update.index(num2)

            if pos_num1 > pos_num2:
                valid = False
                break


    if valid:
        valid_updates.append(update)
    
    if not valid:
        invalid_updates.append(update)
    
# print(valid_updates)


# middle_pages = [update[len(update) // 2] for update in valid_updates]
# print(sum(middle_pages))

precedence = {}
for _ in range(len(rules)):
    for a, b in rules:
        precedence[a] = precedence.get(a, 0)
        precedence[b] = max(precedence.get(b, 0), precedence[a] + 1)


updated_invalid = [sorted(update, key=lambda x: precedence.get(x, float('inf'))) for update in invalid_updates]

# print(updated_invalid)
middle_updated_pages = [update[len(update) // 2] for update in updated_invalid]
print(sum(middle_updated_pages))
        
            