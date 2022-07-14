#--- day2 part 1 ---#

with open('input2') as txt:
    data = [(command,int(value)) for command, value in(line.split() for line in txt)]

horizontal,depth = 0,0

for command,value in data:
    if command == 'forward':
        horizontal+= value
    elif command == 'down':
        depth += value
    else:
        depth -= value
position = horizontal * depth
print(horizontal,depth, position)
