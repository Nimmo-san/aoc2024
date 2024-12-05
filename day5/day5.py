from collections import defaultdict, deque


filename = 'day5/day5.txt'
with open(filename, mode='r') as file:
    sections = file.read().strip().split("\n\n")

    rules = [tuple(map(int, rule.split('|'))) for rule in sections[0].split('\n')]

    updates = [list(map(int, update.split(',')))  for update in sections[1].split('\n')]


# precedence = {}
# valid_updates = []
# invalid_updates = []

# for _ in range(len(rules)):
#     for a, b in rules:
#         precedence[a] = precedence.get(a, 0)
#         precedence[b] = max(precedence.get(b, 0), precedence[a] + 1)

# for update in updates:
#     valid = True
#     for num1, num2 in rules:
#         if num1 in update and num2 in update:
#             pos_num1 = update.index(num1)
#             pos_num2 = update.index(num2)

#             if pos_num1 > pos_num2:
#                 valid = False
#                 break
#     if valid:
#         valid_updates.append(update)
#     else:
#         invalid_updates.append(update)

# middle_pages = sum([update[len(update) // 2] for update in valid_updates])
# updated_invalid = [sorted(update, key=lambda x: precedence.get(x, float('inf'))) for update in invalid_updates]
# middle_updated_pages = [update[len(update) // 2] for update in updated_invalid]


def optimized_topological_sort(update):
    subgraph = defaultdict(list)
    sub_in_degree = defaultdict(int)
    
    for a, b in rules:
        if a in update and b in update:
            subgraph[a].append(b)
            sub_in_degree[b] += 1
            sub_in_degree[a]

    # Performing topological sort
    queue = deque([node for node in update if sub_in_degree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in subgraph[current]:
            sub_in_degree[neighbor] -= 1
            if sub_in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order

correct_updates = []
reordered_updates = []

for update in updates:
    allowed_order = optimized_topological_sort(update)
    if update == allowed_order:
        correct_updates.append(update)
    else:
        reordered_updates.append(allowed_order)

correct_middle_sum = sum(update[len(update) // 2] for update in correct_updates)
reordered_middle_sum = sum(update[len(update) // 2] for update in reordered_updates)

print(correct_middle_sum, reordered_middle_sum)
