data = [list(line) for line in open('AOC2024/in.txt').read().splitlines()]

def matchingFrequency(frequency):
    matching = []
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == frequency:
                matching.append([row, col])
    
    return matching


def an_in_boundary(an):
    if an[0] < 0 or an[1] < 0 or an[0] > len(data) - 1 or an[1] > len(data[0]) - 1:
        return False
    
    return True


def part1():
    anti_nodes = []

    for row in range(len(data)):
        for col in range(len(data[0])):
            #DONE: Find antenna (locations on map that are not marked with '.')
            if data[row][col] == '.':
                continue
            
            #Get locations of antenna with same frequency
            antenna_on_frequency = matchingFrequency(data[row][col])
            #add anti-nodes for each pair of antenna on the same frequency, using the distance between the antenna
            for ant in antenna_on_frequency:
                for others in antenna_on_frequency[antenna_on_frequency.index(ant):]:
                    if ant == others:
                        continue

                    #list anti-node locations and check for already existing anti-node locations
                    delta = [others[0] - ant[0], others[1] - ant[1]]
                    anti_nodeA = [ant[0] - delta[0], ant[1] - delta[1]]
                    anti_nodeB = [others[0] + delta[0], others[1] + delta[1]]
                    
                    if an_in_boundary(anti_nodeA) and anti_nodeA not in anti_nodes:
                        anti_nodes.append(anti_nodeA)

                    if an_in_boundary(anti_nodeB) and anti_nodeB not in anti_nodes:
                        anti_nodes.append(anti_nodeB)              

    #return number of anti-node locations (length of list)
    return len(anti_nodes)


def iter_an(start, delta, polarity):
    ret = []
    bol = True
    multiplier = 1

    ret.append(start)

    while bol:
        match polarity:
            case '+':
                anti = [start[0] + (delta[0] * multiplier), start[1] + (delta[1] * multiplier)]
            case '-':
                anti = [start[0] - (delta[0] * multiplier), start[1] -  (delta[1] * multiplier)]

        if not an_in_boundary(anti):
            bol = False
            continue

        multiplier += 1

        ret.append(anti)
    
    return ret



def part2():
    anti_nodes = []

    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == '.':
                continue

            antenna_on_frequency = matchingFrequency(data[row][col])

            for ant in antenna_on_frequency:
                for others in antenna_on_frequency[antenna_on_frequency.index(ant):]:
                    if ant == others:
                        continue

                    #list anti-node locations and check for already existing anti-node locations
                    delta = [others[0] - ant[0], others[1] - ant[1]]

                    for an in iter_an(ant, delta, '-'):
                        if an not in anti_nodes:
                            anti_nodes.append(an)

                    for an in iter_an(ant, delta, '+'):
                        if an not in anti_nodes:
                            anti_nodes.append(an)            

    #return number of anti-node locations (length of list)
    return len(anti_nodes)


print(part1())
print(part2())