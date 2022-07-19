#--- day3 part 1 ---#


data = []
with open('input3') as txt:
    for i in txt.read().split():
        data.append(i)


gamma = ''
epsilon = ''

length = len(data[0])

for digit in range(length):
    count0 = sum(1 for i in data if i[digit] == '0')
    count1 = len(data) - count0
    if count0 < count1:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
pwrCons = int(gamma,2) * int(epsilon,2)
print(pwrCons)

