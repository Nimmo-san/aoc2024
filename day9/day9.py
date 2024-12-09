
filename = 'day9/day9.txt'

with open(filename, mode='r') as file:
    disk = file.read()


def disk_mapping(fragment):
    disk_mapped = []
    file_lengths = {}
    file_id = 0
    for i in range(0, len(fragment), 2):
        file_length = int(fragment[i])
        free_space = int(fragment[i + 1] if i + 1 < len(fragment) else 0)

        disk_mapped.extend([str(file_id)] * file_length)
        file_lengths[file_id] = file_length
        disk_mapped.extend(['.'] * free_space)
        file_id += 1
    return disk_mapped, file_lengths


def compact_part1(fragment):
    while '.' in fragment:
        leftmost = fragment.index('.')
        num = fragment[::-1].index(next(c for c in reversed(fragment) if c != '.'))
        rightmost = len(fragment) - 1 - num

        if rightmost > leftmost:
            fragment[leftmost], fragment[rightmost] = fragment[rightmost], '.'
        else:
            break
    return fragment


def compact_part2(fragment, file_lengths):
    for file_id in sorted(file_lengths.keys(), reverse=True):
        print("each fragment iteration", ''.join(fragment))

        file_length = file_lengths[file_id]

        for i in range(len(fragment)):
            if fragment[i] == str(file_id):
                fragment[i] = '.'

        free_spans = []
        start = None
        for i, frag in enumerate(fragment):
            if frag == '.':
                if start is None:
                    start = i
            else:
                if start is not None:
                    if i - start >= file_length:
                        free_spans.append((start, i))
                    start = None

        if start is not None and len(fragment) - start >= file_length:
            free_spans.append((start, len(fragment)))

        free_spans.sort()

        print(f"file {file_id} (length {file_length}): Free spans {free_spans}")
        
        if free_spans:
            start, _ = free_spans[0]
            
            for i in range(file_length):
                fragment[start + i] = str(file_id)

            print(f"after moving file {file_id}: {''.join(fragment)}")
        else:
            print(f"file {file_id} could not be moved")
    return fragment


total = 0
fragment, file_lengths = disk_mapping(disk)
print("initial fragment", ''.join(fragment))
print("file_lengths", file_lengths)


# PART 1
# result = compact_part1(fragment)

# PART 2
compact_part2(fragment, file_lengths)

print("final fragment", ''.join(fragment))

for i, num in enumerate(fragment):
    if num != '.':
        total += i * int(num)

print(total)