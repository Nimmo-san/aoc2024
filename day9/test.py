filename = 'day9/day9.txt'

with open(filename, mode='r') as file:
    disk_map = file.read()


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


def move_whole_files(disk_mapped, file_lengths):
    for file_id in sorted(file_lengths.keys(), reverse=True):
        file_length = file_lengths[file_id]

        current_positions = [i for i, block in enumerate(disk_mapped) if block == str(file_id)]
        if not current_positions:
            continue

        print(f"File ID {file_id}, Current positions: {current_positions}")

        current_start = current_positions[0]

        for i in range(len(disk_mapped) - file_length + 1):
            if i >= current_start:
                break
            
            if all(disk_mapped[j] == '.' for j in range(i, i + file_length)):
                print(f"File ID {file_id} moving to position: {i}")
                for pos in current_positions:
                    disk_mapped[pos] = '.'

                disk_mapped[i:i + file_length] = [str(file_id)] * file_length
                break

        print(f"Disk after moving File ID {file_id}: {''.join(disk_mapped)}")
    return disk_mapped


def calculate_checksum(blocks):
    return sum(pos * int(block) for pos, block in enumerate(blocks) if block != ".")


blocks, file_lengths = disk_mapping(disk_map)

print(''.join(blocks))
compacted_blocks = move_whole_files(blocks, file_lengths)

print(''.join(compacted_blocks))
checksum = calculate_checksum(compacted_blocks)

print(f"Resulting checksum: {checksum}")
