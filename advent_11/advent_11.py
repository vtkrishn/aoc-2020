def allocate(seats, row, col, puzzle):
    def valid(x, y, row, col):
        return 0 <= x < row and 0 <= y < col

    def run_for(puzzle, step):
        if step == 1:
            return True if puzzle == 1 else False
        return 4 if puzzle == 1 else 5

    def print_result(seats, row, col):
        result = 0
        for i in range(row):
            for j in range(col):
                if seats[i][j] == '#':
                    result += 1
        print(result)

    def check_filled(seats, i, j, row, col, puzzle):
        result = 0
        for ni, nj in dir:
            x, y = i + ni, j + nj
            if run_for(puzzle, 1):
                if valid(x,y,row, col) and seats[x][y] == '#':
                    result += 1
            else:
                while valid(x,y,row, col):
                    if seats[x][y] == '#':
                        result += 1
                        break
                    elif seats[x][y] == 'L':
                        break
                    x += ni
                    y += nj
        return result

    while True:
        flip = True
        seat_copy = [copy.copy(seat) for seat in seats]
        for i, r in enumerate(seat_copy):
            for j, c in enumerate(r):
                count = check_filled(seat_copy, i, j, row, col, puzzle)

                if c == 'L' and count == 0:
                    seats[i][j] = '#'
                elif c == '#' and count >= run_for(puzzle, 2):
                    seats[i][j] = 'L'
                flip = flip and (r[j] == seats[i][j])
        if flip:
            break

    print_result(seats, row, col)

def part_2(seats, row, col):
    allocate(seats, row, col, 2)


def part_1(seats, row, col):
    allocate(seats, row, col, 1)

def parse(data):
    seats = []
    for row in data:
        seats.append([seat for seat in row])
    return seats

import copy
dir = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
with open('inputs.txt', 'r') as fh:
    data = fh.read().splitlines()
    seats = parse(data)
    row, col = len(seats), len(seats[0])
    part_1(seats, row, col)

    seats = parse(data)
    part_2(seats, row, col)

