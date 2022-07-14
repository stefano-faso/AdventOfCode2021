#----day1 part 1-----#

depth = []
P1_increase = 0
P2_increase = 0

with open('input1','r') as txt:
    for val in txt.read().split():
        depth.append(int(val))

for i in range(0,len(depth)):
    if depth[i] > depth[i-1]:
        P1_increase += 1
print(f'part1:{P1_increase}')

#---- day1 part 2 ----#

for i in range(0,len(depth)):
    if depth[i] > depth[i-3]:
        P2_increase += 1
print(f'part2:{P2_increase}')