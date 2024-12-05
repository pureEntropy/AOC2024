import re

puzzleInput = """

"""
exampleInput = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
regex = "mul\((\d{1,3}),(\d{1,3})\)"

def part1(text):
    regex = "mul\((\d{1,3}),(\d{1,3})\)"
    data = re.findall(regex, text)
    return sum([int(pair[0]) * int(pair[1]) for pair in data])


def part2(text):
    total = 0
    do = True
    newRegex = "(don't\(\))|(do\(\))|mul\((\d{1,3}),(\d{1,3})\)"
    array = re.findall(newRegex, text)

    for item in array:
        if item[0]:
            do = False
            continue

        if item[1]:
            do = True
            continue

        if not do:
            continue

        total += int(item[2]) * int(item[3])

    return total


print(f"Part 1 answer: {part1(puzzleInput)}")
print(f"Part 2 answer: {part2(puzzleInput)}")