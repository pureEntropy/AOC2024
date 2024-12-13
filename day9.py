inputA = list(open('AOC2024/in.txt').read())
example = list('2333133121414131402')
data = inputA
uncompressedData = ''
data1 = ''
ii = 0

for i in range(len(data)):
    if i % 2 == 0:
        uncompressedData += str(ii) * int(data[i])
        data1 += str(ii) * int(data[i])
        ii += 1
    else:
        uncompressedData += '.' * int(data[i])

data1 = data1[::-1]

currIndex = 0
uncompressedData = list(uncompressedData)
num_dot = uncompressedData.count('.')
for iii in range(len(uncompressedData) - num_dot):
    if uncompressedData[iii] != '.':
        continue
    else:
        uncompressedData[iii] = data1[currIndex]
        currIndex += 1

smashed = ''.join(uncompressedData[: - num_dot])

total = 0
for iiii in range(len(smashed)):
    total += (iiii * int(smashed[iiii]))
    print(f"{iiii} * {int(smashed[iiii])} = {iiii * int(smashed[iiii])}")

print(total)