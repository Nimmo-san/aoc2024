
filename = 'day9/day9.txt'

with open(filename, mode='r') as file:
    disk = file.read()



def disk_mapping(fragment):
    disk_mapped = []
    file_id = 0
    for i in range(0, len(fragment), 2):
        file_length = int(fragment[i])
        free_space = int(fragment[i + 1] if i + 1 < len(fragment) else 0)

        disk_mapped.extend([str(file_id)] * file_length)
        disk_mapped.extend(['.'] * free_space)
        file_id += 1
    return disk_mapped


def compact(fragment):
    while '.' in fragment:
        leftmost = fragment.index('.')
        num = fragment[::-1].index(next(c for c in reversed(fragment) if c != '.'))
        rightmost = len(fragment) - 1 - num

        if rightmost > leftmost:
            fragment[leftmost], fragment[rightmost] = fragment[rightmost], '.'
        else:
            break
    return fragment


total = 0
fragment = disk_mapping(disk)
result = compact(fragment)

for i, num in enumerate(result):
    if num != '.':
        total += i * int(num)
    
print(total)

