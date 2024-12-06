lab = [list(line) for line in open('AOC2024/in.txt').read().splitlines()]

class Guard:
    def __init__(self):
        self.direction = 0
        self.pos = [(i, row.index('^')) for i, row in enumerate(lab) if '^' in row][0]


    def facing(self):
        facingDelta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        return [self.pos[0] + facingDelta[self.direction][0], self.pos[1] + facingDelta[self.direction][1]]


    #return True if facing is out of bounds
    def leaving(self):
        if self.facing()[0] < 0 or self.facing()[1] < 0 :
            return True
        
        if self.facing()[0] >= len(lab) or self.facing()[1] >= len(lab[0]):
            return True
        
        return False
        

    def turn(self):
        self.direction = (self.direction + 1) % 4


    def move(self):
        #turn if facing obstacle
        if lab[self.facing()[0]][self.facing()[1]] == '#' or lab[self.facing()[0]][self.facing()[1]] == 'O':
            self.turn()
            return

        #change current positon to X
        lab[self.pos[0]][self.pos[1]] = 'X'

        #move forward 1 (change self.pos to self.facing)
        self.pos = self.facing()
        

def part1():
    guard = Guard()

    while not guard.leaving():
        guard.move()

    total = 1
    for row in lab:
        for element in row:
            if element == 'X':
                total += 1

    return total


def resetLab():
    global lab
    lab = [list(line) for line in open('AOC2024/in.txt').read().splitlines()]


def part2():
    global lab
    resetLab()
    loop = 0

    for i, row in enumerate(lab):
        for ii, col in enumerate(row):
            moves = 0
            resetLab()
            guard = Guard()

            if col == '#'or col == '^':
                continue

            lab[i][ii] = 'O'
            
            #Run through map and check for loop (move count is > 10000)
            while not guard.leaving() and moves < 10000:
                moves += 1
                guard.move()

            if moves >= 10000:
                loop += 1
            
    return loop
                    

print(part1())
print(part2())