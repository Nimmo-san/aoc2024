

filename = "daytwo.txt"

lines = []

with open(filename, mode='r') as file:
    for line in file:
        lines.append(line.split())



increasing = []
decreasing = []

def report(inner):
    increasing = decreasing = True
    for current, next_val in zip(inner, inner[1:]):
        difference = int(next_val) - int(current)
        
        if abs(difference) < 1 or abs(difference) > 3:
            return False
    
        if difference > 0:
            increasing = False
        elif difference < 0:
            decreasing = False
    
    return increasing or decreasing


def report_with_dapmner(inner):
    if report(inner):
        return True
    
    for i in range(len(inner)):
        modified = inner[:i] + inner[i+1:]

        if report(modified):
            return True
    
    return False

sum_reports = sum([1 for inner in lines if report_with_dapmner(inner)])
print(sum_reports)
