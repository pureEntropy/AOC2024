puzzleInput = """

"""
unsafe = 0


def isSafe(row):
    delta = {row[i + 1] - row[i] for i in range(len(row) - 1)}
    return delta <= {1, 2, 3} or delta <= {-1, -2, -3}

out = [[int(num) for num in line.split(' ')] for line in puzzleInput.splitlines()]

unsafe = sum([isSafe(row) for row in out])
print(unsafe)

unsafe = sum([any([isSafe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in out])
print(unsafe)