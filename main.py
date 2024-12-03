


filename = "data.txt"
left = []
right = []

with open(filename, mode='r') as file:
    for line in file:
        values = line.split()
        left.append(int(values[0]))
        right.append(int(values[1]))



distance = []
similarityScore = 0
left.sort()
right.sort()

for key, val in enumerate(left):
    distance.append(abs(val - right[key]))

    for num in right:
        if num == val:
            similarityScore += num

print(sum(distance))
print(similarityScore)