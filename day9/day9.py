from collections import defaultdict

filename = 'day9/day9.txt'

with open(filename, mode='r') as file:
    disk = file.read()


fragment = []
renewed = False
index = 0

for i, char in enumerate(disk):
    # print(i, char)
    for j in range(int(char)):
        if i % 2 == 0:
            renewed = True
            fragment.append(index)
        else:
            fragment.append('.')

    if renewed:
        index += 1
        renewed = False



while '.' in fragment:
    leftmost = fragment.index('.')
    num = fragment[::-1].index(next(c for c in reversed(fragment) if c != '.'))
    rightmost = len(fragment) - 1 - num

    if rightmost > leftmost:
        fragment[leftmost], fragment[rightmost] = fragment[rightmost], '.'
    else:
        break

total = 0

for i, num in enumerate(fragment):
    if num != '.':
        total += i * int(num)
    
print(total)

