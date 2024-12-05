from functools import cmp_to_key

#data = puzzleInput.splitlines()
rules, updates = open('AOC2024/in.txt').read().split('\n\n')
cmp = cmp_to_key(lambda x,y: 1-2*(x+'|'+y in rules))
ruless = [line.split('|') for line in rules.split()]
updates = [line.split(',') for line in updates.split()]

def outOfOrder(upd):
    for page in upd:
        for rule in ruless:
            if page not in rule:
                continue

            if rule[0] not in upd or rule[1] not in upd:
                continue

            if rule[0] == page and upd.index(page) > upd.index(rule[1]):
                return True
                
            if rule[1] == page and upd.index(page) < upd.index(rule[0]):
                return True
            

def sortedUpdate(update):
    corrected = sorted(update, key=cmp)

    return corrected[len(corrected) // 2]
                

def part1():
    total = 0
    for update in updates:
        if outOfOrder(update):
            continue

        total += int(update[len(update) // 2])

    print(total)

                
def part2():
    total = 0
    for update in updates:
        if outOfOrder(update):
            total += int(sortedUpdate(update))

    print(total)


part1()
part2()