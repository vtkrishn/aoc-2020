def part_2(box):
    def dfs(box, content):
        global count
        for item, quantity in content.items():
            for x in range(quantity):
                count += 1
                dfs(box, box[item])
        return count

    return dfs(box, box['shiny gold bags'])


def part_1(box):
    def dfs(box, contents, found=False):
        for item in contents.keys():
            if 'shiny gold' in item:
                found = True
            found = dfs(box, box[item], found)
        return found

    total = 0
    for item, quantity in box.items():
        if dfs(box, quantity): total += 1
    return total


def sanitize(bags):
    box = {}
    for bag in bags:
        bag[1] = bag[1].replace('bag.', 'bags.').replace('bag,', 'bags,').strip('.')
        content = {}
        items = bag[1].split(', ')
        for item in items:
            if not item[0].isalpha():
                key, value = item[2:], int(item[0])
                content[key] = value
        box[bag[0]] = content
    return box


def parse(data):
    bags = []
    for bag in data:
        content = []
        for item in bag.split(' contain '):
            content.append(item)
        bags.append(content)
    return bags


with open('inputs.txt', 'r') as fh:
    data = fh.read().splitlines()
    bags = parse(data)
    box = sanitize(bags)
    count = 0
    part_1, part_2 = part_1(box) ,part_2(box)
    print(part_1)
    print(part_2)
