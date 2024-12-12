from functools import cache

filename = "day11/input.txt"


with open(filename, mode='r') as file:
    input = file.read().strip().split()
    stones = [int(num) for num in input]


# for _ in range(25):
#     output = []
#     for stone in stones:
#         string_stone = str(stone)
#         size = len(string_stone)
#         if stone == 0:
#             output.append(1)
#             continue

#         if size % 2 == 0:
#             output.append(int(string_stone[:size // 2]))
#             output.append(int(string_stone[size // 2:]))
#         else:
#             output.append(2024 * stone)
#     stones = output
    # print(stones)

# print(len(stones))

@cache
def find_answer_recursively(num, steps):
    if steps == 0:
        return 1
    
    if num == 0:
        return find_answer_recursively(1, steps - 1)
    
    
    string_stone = str(num)
    size = len(string_stone)
    if size % 2 == 0:
        return find_answer_recursively(int(string_stone[:size // 2]), steps - 1) + find_answer_recursively(int(string_stone[size // 2:]), steps - 1)
    else:
        return find_answer_recursively(2024 * num, steps - 1)


result = 0
for stone in stones:
    result += find_answer_recursively(stone, 75)

print(result)


