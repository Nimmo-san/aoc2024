

filename = "day11/input.txt"


with open(filename, mode='r') as file:
    input = file.read().strip().split()
    stones = [int(num) for num in input]


for _ in range(25):
    output = []
    for stone in stones:
        string_stone = str(stone)
        size = len(string_stone)
        if stone == 0:
            output.append(1)
            continue

        if size % 2 == 0:
            output.append(int(string_stone[:size // 2]))
            output.append(int(string_stone[size // 2:]))
        else:
            output.append(2024 * stone)
    stones = output
    # print(stones)

print(len(stones))


