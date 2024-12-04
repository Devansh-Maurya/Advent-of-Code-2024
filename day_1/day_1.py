import fileinput
from collections import Counter

locations = []

for line in fileinput.input("test"):
    locations.append(list(map(int, line.replace('\n', '').split('   '))))
    
l1 = sorted([location[0] for location in locations])
l2 = sorted([location[1] for location in locations])

# ---- Part 1 ----
ansPart1 = 0

for i in range(len(l1)):
    ansPart1 += abs(l1[i] - l2[i])

print(ansPart1)

# ---- Part 2 ----
l1Counts = Counter(l1)
l2Counts = Counter(l2)

ansPart2 = sum([ k * l1Counts[k] * l2Counts[k] for k in l1Counts])

print(ansPart2)