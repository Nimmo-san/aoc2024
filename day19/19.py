
filename = "day19/input.txt"


words, targets = [line for line in open(filename).read().strip().split('\n\n')]
words = words.split(', ')

#print(words)
#print(targets)



check = {}
def find_target(target: str, words):
    if target in check:
        return check[target]
    ok = 0

    if not target:
        ok = 1

    for word in words:
        if target.startswith(word):
            ok += find_target(target[len(word):], words)

    check[target] = ok
    return ok



total = 0
for target in targets.split('\n'):
    total += find_target(target, words)
    # print(target, words)

print(total)
