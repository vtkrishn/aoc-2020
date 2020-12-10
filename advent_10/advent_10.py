def part_2(adapters, start, end):
    key = start
    if key in cache:
        return cache[key]

    count = 0
    if end - start <= 3:
        count += 1
    if not adapters:
        return count

    current, remaining = adapters[0], adapters[1:]
    if current - start <= 3:
        count += part_2(remaining, current, end)
    count += part_2(remaining, start, end)

    cache[key] = count
    return count


def part_1(adapters):
    adapters.sort()
    prev = 0
    one, three = 1, 1
    for index in range(1, len(adapters)):
        diff = abs(adapters[index] - adapters[prev])
        if diff == 3: three += 1
        elif diff == 1: one += 1
        prev += 1
    return (three * one), (adapters[prev] + 3)

def parse(data):
    return [int(adapter) for adapter in data]


with open('inputs.txt', 'r') as fh:
    data = fh.read().splitlines()
    adapters = parse(data)
    part1,last_value = part_1(adapters)
    cache = {}
    part2 = part_2(adapters, 0, last_value)
    print(part1, part2)
