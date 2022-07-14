with open('input2') as txt:
    data = [(command,int(value)) for command, value in (line.split() for line in txt)]
    
#--- day2 part 1 ---#

def part1():
    horizontal,depth= 0,0

    for command,value in data:
        if command == 'forward':
            horizontal += value
        elif command == 'down':
            depth += value
        else:depth -= value
    print(depth*horizontal)

#--- day2 part 2 ---#

def part2():
    depth,horizontal,aim =0,0,0

    for command, value in data:
        if command == 'forward':
            horizontal += value
            depth += value * aim
        elif command == 'down':
            aim += value
        else:aim -= value
    print(depth * horizontal)
