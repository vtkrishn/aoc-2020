def two_sum(sub_array, target):
    map  = {}
    for item in sub_array:
        value = int(item)
        key = int(target-value)
        if value in map:
            return (key,value)
        else:
            map[key] = value


def part_2(data, part1):
    strip_data = [int(i) for i in data if int(i) < part1]

    start, end = 0, 1
    while True:
        sum_k = sum(strip_data[start:end])
        if sum_k > part1:
            start += 1
            end = start + 1
            continue
        if sum_k == part1:
            ans_range = strip_data[start:end]
            return min(ans_range) + max(ans_range)
        end += 1


def part_1(data):
    map = parse(25, data)

    for k, v in map.items():
        value = two_sum(map[k][0], map[k][1])
        if not value:
            return map[k][1]


def parse(premble, data):
    m = {}
    start = 0
    for target in range(premble + 1, len(data) + 1):
        m[start] = [data[start:target - 1], int(data[target - 1])]
        start += 1
    return m


with open('inputs.txt', 'r') as fh:
    data = fh.read().splitlines()
    part1 = part_1(data)
    part2 = part_2(data, part1)
    print(part1, part2)


