def part_2():
    pass

def part_1():
    pass


def parse(data):
    pass


def brute_force(data, end):
    i = len(data)
    seen = {v: k+1 for k, v in enumerate(data)}
    cur = data[-1]
    while i < end:
        if cur not in seen:
            seen[cur] = i
            cur = 0
        else:
            prev = cur
            cur = i - seen[prev]
            seen[prev] = i
        i += 1
    return cur


def part_one(data):
    return brute_force(data, 2020)


def part_two(data):
    return brute_force(data, 30000000)


with open('inputs.txt', 'r') as fh:
    data = fh.read().splitlines()
    parsed=[int(i) for i in data[0].split(',')]
    print(part_one(parsed))
    print(part_two(parsed))
