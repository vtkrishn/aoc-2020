def part_1(trees, right, down):
    row,col = len(trees), len(trees[0])
    count,i,j  = 0,0,0
    while i < row - down:
        i += down
        j = (j + right) % col
        if trees[i][j] == '#':
            count += 1
    return count

def part_2(trees):
    return part_1(trees, 1, 1) * part_1(trees, 3, 1) * part_1(trees, 5, 1) * part_1(trees, 7, 1) * part_1(trees, 1, 2)

with open('inputs.txt', 'rb') as fh:
    data = [l for l in fh.read().splitlines()]
    # part 1
    print(part_1(data, 3, 1))

    # part 2
    print(part_2(data))


