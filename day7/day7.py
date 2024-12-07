from itertools import product

filename = "day7/day7.txt"

with open(filename, mode='r') as file:
    data = [line for line in file]


total = 0

for line in data:
    # eval_num = int(num[0].split(':')[0])
    eval_num, *numbers = map(int, line.replace(':', '').split())
    # print(eval_num, numbers)

    operator_combinations = product(['+', '*'], repeat=len(numbers)-1)
    result = 0
    if result == eval_num:
        for operator in operator_combinations:
            result = numbers[0]
            for i in range(len(operator)):
                if operator[i] == '+':
                    result += numbers[i+1]
                elif operator[i] == '*':
                    result *= numbers[i+1]
        
        total += eval_num

print(eval_num)

