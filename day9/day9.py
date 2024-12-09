

import copy

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

        file_length = file_lengths[file_id]

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

        if free_spans:
            start, _ = free_spans[0]
            
            for i in range(file_length):
                fragment[start + i] = str(file_id)

                # couldn't get removing files to work :D
    return fragment


def adjust_fragment(new_fragment, file_lengths):
    adjusted_fragment = list('.' * len(new_fragment))
    for file_id, length in file_lengths.items():
        positions = [i for i, char in enumerate(new_fragment) if char == str(file_id)]

        for i in range(length):
            if i < len(positions):
                adjusted_fragment[positions[i]] = str(file_id)
            else:
                for j, char in enumerate(adjusted_fragment):
                    if char == '.':
                        adjusted_fragment[j] = str(file_id)
                        break

    return ''.join(adjusted_fragment)

total = 0
fragment, file_lengths = disk_mapping(disk)
compact_part2(fragment, file_lengths)
final_frag = adjust_fragment(fragment, file_lengths)

total = 0
total = sum(i * int(num) for i, num in enumerate(final_frag) if num != '.')

print(total)