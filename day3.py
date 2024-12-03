import re



filename = "day3.txt"

final = []
mul_enabled = True

with open(filename, mode='r') as file:
    lines  = file.read()
    match = re.findall(r"mul\(\d{1,3},\d{1,3}\)|\bdo\(\)|\bdon't\(\)", lines)

    for instruction in match:
        if instruction.startswith("mul"):
            left = int(instruction.split(',')[0].split('(')[1])
            right = int(instruction.split(',')[1].split(')')[0])

            if mul_enabled:
                final.append(left * right)
        
        elif instruction.startswith("do()"):
            mul_enabled = True
        
        elif instruction.startswith("don't"):
            mul_enabled = False
            
print(sum(final))