data = open('AOC2024/in.txt').read().splitlines()

def part1():
    result = 0
    getBin = lambda x, n: format(x, 'b').zfill(n)

    for line in data:
        testValue = int(line[:line.index(': ')])
        numbers = line[line.index(': ') + 2:].split(' ')

        for i in range(2 ** (len(numbers) - 1)):
            ops = getBin(i, len(numbers) - 1)
            localTotal = int(numbers[0])
            
            for o in range(len(ops)):
                match ops[o]:
                    case '0':
                        localTotal += int(numbers[o + 1])
                    case '1':
                        localTotal *= int(numbers[o + 1])

            if testValue == localTotal:
                result += testValue
                break

    return result


def trianry(n):
    if n == 0:
        return '0'
    
    base3 = []
    isNeg = n < 0
    n = abs(n)

    while n > 0:
        base3.append(str(n % 3))
        n //= 3

    if isNeg:
        base3.append("-")

    return ''.join(reversed(base3))


def part2():
    result = 0
    getTri = lambda x, n: trianry(x).zfill(n)

    for line in data:
        testValue = int(line[:line.index(': ')])
        numbers = line[line.index(': ') + 2:].split(' ')

        for i in range(3 ** (len(numbers) - 1)):
            ops = getTri(i, len(numbers) - 1)
            localTotal = int(numbers[0])

            for o in range(len(ops)):
                match ops[o]:
                    case '0':
                        localTotal += int(numbers[o + 1])
                    case '1':
                        localTotal *= int(numbers[o + 1])
                    case '2':
                        localTotal = int(str(localTotal) + numbers[o + 1])

            if testValue == localTotal:
                result += testValue
                break

    return result


print(part1())
print(part2())