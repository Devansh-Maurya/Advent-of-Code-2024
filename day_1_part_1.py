import fileinput

locations = []

for line in fileinput.input("test"):
    locations.append(list(map(int, line.replace('\n', '').split('   '))))
    
l1 = sorted([location[0] for location in locations])
l2 = sorted([location[1] for location in locations])

ans = 0

for i in range(len(l1)):
    ans += abs(l1[i] - l2[i])

print(ans)
