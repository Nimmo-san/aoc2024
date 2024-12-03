import re



filename = "day3.txt"

final = []


with open(filename, mode='r') as file:
    lines  = file.read()
    match = re.findall(r'mul\(\d{1,3},\d{1,3}\)', lines)

    for num in match:
        left = num.split(',')[0].split('(')[1]
        right = num.split(',')[1].split(')')[0]
    
        final.append(int(left) * int(right))

print(sum(final))