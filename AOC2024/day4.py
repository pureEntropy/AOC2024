puzzleInput = """"""
data = [list(line) for line in puzzleInput.splitlines()]
numRows = len(data)
numCols = len(data[0])

def part1():
    totalXMAS = 0
    pos = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    for row in range(numRows):
        for col in range(numCols):
            if data[row][col] != 'X':
                continue
            
            #print(f" {row}, {col}:")
            for i in range(8):
                #print(f"trying direction {i}")
                if row + pos[i][0] not in range(numRows) or col + pos[i][1] not in range(numCols):
                    continue

                if row + (pos[i][0] * 2) not in range(numRows) or col + (pos[i][1] * 2) not in range(numCols):
                    continue

                if row + (pos[i][0] * 3) not in range(numRows) or col + (pos[i][1] * 3) not in range(numCols):
                    continue

                if data[row + pos[i][0]][col + pos[i][1]] != 'M':
                    continue

                if data[row + (pos[i][0] * 2)][col + (pos[i][1] * 2)] != 'A':
                    continue

                if data[row + (pos[i][0] * 3)][col + (pos[i][1] * 3)] != 'S':
                    continue
                
                totalXMAS += 1
                #print("found a match")
    
    print(f"part 1 answer: {totalXMAS}")


def part2():
    totalX_MAS = 0
    for row in range(1, numRows - 1):
        for col in range(1, numCols - 1):
            if data[row][col] != 'A':
                continue

            #print(f"{row}, {col}:")

            if 'X' in [data[row - 1][col - 1], data[row - 1][col + 1], data[row + 1][col - 1], data[row + 1][col + 1]]:
                continue

            if 'A' in [data[row - 1][col - 1], data[row - 1][col + 1], data[row + 1][col - 1], data[row + 1][col + 1]]:
                continue

            if data[row - 1][col - 1] == data[row + 1][col + 1]:
                continue

            if data[row + 1][col - 1] == data[row - 1][col + 1]:
                continue

            totalX_MAS += 1
            #print(f"""found a match
#{data[row - 1][col - 1]}-{data[row - 1][col + 1]}
#-A-
#{data[row + 1][col - 1]}-{data[row + 1][col + 1]}""")

    print(f"part 2 answer: {totalX_MAS}")


part1()
part2()