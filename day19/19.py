
filename = "day19/input.txt"


words, targets = [line for line in open(filename).read().strip().split('\n\n')]
words = words.split(', ')

print(words)
print(targets)
