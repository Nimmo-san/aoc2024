from itertools import product

filename = "day7/day7.txt"

with open(filename, mode='r') as file:
    data = [line for line in file]


total = 0

for line in data:
    # eval_num = int(num[0].split(':')[0])
    eval_num, *numbers = map(int, line.replace(':', '').split())
    # print(eval_num, numbers)

    operator_combinations = product(['*', '+', '||'], repeat=len(numbers)-1)
    match = False
    # print(list(operator_combinations))
    result = 0
    for operator in operator_combinations:
        result = numbers[0]
        for i in range(len(operator)):
            if operator[i] == '+':
                result += numbers[i+1]
            elif operator[i] == '*':
                result *= numbers[i+1]
            elif operator[i] == '||':
                result = int(str(result) + str(numbers[i+1]))
        
        # print(result)
        if result == eval_num:
            match = True
            break
        
    if match:
        total += eval_num

print(total)

