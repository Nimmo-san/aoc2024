
filename = "day19/input.txt"


words, targets = [line for line in open(filename).read().strip().split('\n\n')]
words = words.split(', ')

#print(words)
#print(targets)



check = {}
def find_target(target, words):
    if target in check:
        return check[target]
    ok = False

    if not target:
        ok = True

    for word in words:
        if target.startswith(word) and find_target(target[len(word):], words):
            ok = True

    check[target] = ok
    return ok



total = 0
for target in targets.split('\n'):
    
    if find_target(target, words):
        total += 1
    # print(target, words)

print(total)
