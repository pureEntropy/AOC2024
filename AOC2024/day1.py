inputList = """

"""

leftList = []
rightList = []

for line in inputList.splitlines():
    leftList.append(int(line[0:line.index('   ')]))
    rightList.append(int(line[line.index('   ')+3:]))


def part1():
    difference = 0
    leftList.sort()
    rightList.sort()

    for i in range(len(leftList)):
        difference += abs(leftList[i] - rightList[i])
    
    return(difference)


def part2():
    difference = 0

    for num in leftList:
        difference += num * rightList.count(num)

    return(difference)    


if __name__ == '__main__':
    #print(part1())
    print(part2())