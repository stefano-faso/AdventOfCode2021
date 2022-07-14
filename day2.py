#--- day2 part 1 ---#

with open('input2') as txt:
    data = [(command,int(value)) for command, value in(line.split() for line in txt)]

horizontal,depth = 0,0

for command in data:
    if command[0] == 'forward':
        horizontal+= int(command[1])
    elif command[0] == 'down':
        depth += int(command[1])
    else:
        depth -= int(command[1])
position = horizontal * depth
print(horizontal,depth, position)