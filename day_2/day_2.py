import fileinput

reports = []

for line in fileinput.input("test"):
    reports.append(list(map(int, line.replace('\n', '').split(' '))))

def isBad(diff):
    return diff < 1 or diff > 3

def isGoodReport(report):
    isBad1 = any([isBad(report[i] - report[i-1]) for i in range(1, len(report))])
    isBad2 = any([isBad(report[i-1] - report[i]) for i in range(1, len(report))])
    
    return (not isBad1) or (not isBad2)


# ---- Part 1 ----
ansPart1 = 0
        
for report in reports:
    isGood = isGoodReport(report)
    
    if isGood:
        ansPart1 += 1

print(ansPart1)


# ---- Part 2 ----
ansPart2 = 0

for report in reports:
    isGood = False

    for i in range(len(report)):
        newReport = report[:]
        newReport.pop(i)
        if isGoodReport(newReport):
            isGood = True
    
    if isGood:
        ansPart2 += 1
    
print(ansPart2)
        
        
        