# def part_2():
#     pass
#
# def part_1():
#     pass
#
# def parse(data):
#     return [[i[0], int(i[1:])] for i in data]
#
# with open('inputs.txt', 'r') as fh:
#     data = fh.read().splitlines()
#     command = parse(data)
#
#     directions = ('N', 'E', 'S', 'W')
#     curr_direction = 'E'
#     curr_index = directions.index(curr_direction)
#
#     distance = {i: 0 for i in directions}
#
#     for direction, value in command:
#         if direction in directions:
#             distance[direction] += value
#         elif direction in ('L', 'R'):
#             index_offset = (value // 90) * (-1 if direction == 'L' else 1)
#             curr_index += index_offset
#             curr_index %= len(directions)
#             curr_direction = directions[curr_index]
#         elif direction == 'F':
#             distance[curr_direction] += value
#
#     print(abs(distance['N'] - distance['S']) + abs(distance['E'] - distance['W']))
#
#     from collections import deque
#     dist = {i: 0 for i in directions}
#     waypoint = {i: 0 for i in directions}
#     waypoint['N'] = 1
#     waypoint['E'] = 10
#
#     for direction, value in command:
#         if direction in directions:
#             distance[direction] += value
#         elif direction in ('L', 'R'):
#             vals = deque(waypoint.values())
#             index_offset = (value // 90) * (-1 if direction == 'L' else 1)
#             vals.rotate(index_offset)
#             waypoint = {k: v for k, v in zip(waypoint.keys(), vals)}
#         elif direction == 'F':
#             for k, v in waypoint.items():
#                 dist[k] += value * v
#
#     print(abs(distance['N'] - distance['S']) + abs(distance['E'] - distance['W']))


#
# from collections import deque
#
#
# def main():
#     with open("inputs.txt", "r") as f:
#         lines = [(l[0], int(l[1:])) for l in f.read().strip().splitlines()]
#
#     print(solve1(lines))
#     print(solve2(lines))
#
#
# def solve1(lines):
#     directions = ("N", "E", "S", "W")
#     curr_direction = "E"
#     curr_index = directions.index(curr_direction)
#
#     dist = {i: 0 for i in directions}
#
#     for d, m in lines:
#         if d in ("N", "S", "E", "W"):
#             dist[d] += m
#         elif d in ("L", "R"):
#             index_offset = (m // 90) * (-1 if d == "L" else 1)
#             curr_index += index_offset
#             curr_index %= len(directions)
#             curr_direction = directions[curr_index]
#         elif d == "F":
#             dist[curr_direction] += m
#
#     return abs(dist["N"] - dist["S"]) + abs(dist["E"] - dist["W"])
#
#
# def solve2(lines):
#     directions = ("N", "E", "S", "W")
#     dist = {i: 0 for i in directions}
#     waypoint= {i: 0 for i in directions}
#     waypoint["N"] = 1
#     waypoint["E"] = 10
#
#     for d, m in lines:
#         if d in directions:
#             waypoint[d] += m
#         elif d in ("L", "R"):
#             vals = deque(waypoint.values())
#             index_offset = (m // 90) * (-1 if d == "L" else 1)
#             vals.rotate(index_offset)
#             waypoint = {k: v for k, v in zip(waypoint.keys(), vals)}
#         elif d == "F":
#             for k, v in waypoint.items():
#                 dist[k] += m * v
#
#     return abs(dist["N"] - dist["S"]) + abs(dist["E"] - dist["W"])
#
#
# if __name__ == "__main__":
#     main()


import math
from collections import deque

with open('inputs.txt') as f:
    data = [(i[0], int(i[1:])) for i in f.read().splitlines()]

direction = deque(['East', 'South', 'West', 'North'])

def change_direction(instruction, n):
    turns = n // 90
    if instruction == 'L':
        direction.rotate(turns)
    elif instruction == 'R':
        direction.rotate(-turns)
    return direction

def rotate(origin, point, angle):
    # source: https://stackoverflow.com/a/34374437
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(round(qx)), int(round(qy))

def part1():
    coord = {'x': 0, 'y': 0}
    for line in data:
        instruction, n = line
        if instruction == 'N':
            coord['y'] += n
        elif instruction == 'S':
            coord['y'] -= n
        elif instruction == 'E':
            coord['x'] += n
        elif instruction == 'W':
            coord['x'] -= n
        elif instruction == 'F':
            facing = direction[0]
            if facing == 'North':
                coord['y'] += n
            elif facing == 'South':
                coord['y'] -= n
            elif facing == 'East':
                coord['x'] += n
            elif facing == 'West':
                coord['x'] -= n
        elif instruction in ['L', 'R']:
            direction = change_direction(instruction, n)
    return abs(coord['x']) + abs(coord['y'])

def part2():
    coord = {'x': 0, 'y': 0}
    waypoint = {'x': 10, 'y': 1}
    for line in data:
        instruction, n = line
        if instruction == 'N':
            waypoint['y'] += n
        elif instruction == 'S':
            waypoint['y'] -= n
        elif instruction == 'E':
            waypoint['x'] += n
        elif instruction == 'W':
            waypoint['x'] -= n
        elif instruction == 'F':
            coord['y'] += waypoint['y'] * n
            coord['x'] += waypoint['x'] * n
        elif instruction in ['L', 'R']:
            if instruction == 'R':
                n = -n
            waypoint['x'], waypoint['y'] = rotate(
                (0, 0), (waypoint['x'], waypoint['y']), math.radians(n)
            )
    return abs(coord['x']) + abs(coord['y'])

print(part1())
print(part2())