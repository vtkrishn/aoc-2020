def part_2():
    pass

def part_1():
    pass


def parse(data):
    pass

# with open('inputs.txt', 'r') as fh:
#     data = fh.read().splitlines()
#
#     processed_data = parse(data)

from collections import defaultdict

FILE_NAME = "inputs.txt"

fields = defaultdict(list)
your_ticket = []
other_tickets = defaultdict(list)

with open(FILE_NAME, 'r') as file:
    fieldos = True
    your = False
    other = False
    other_index = 0
    for line in file:
        if line == "\n":
            continue
        if "your" in line:
            fieldos = False
            your = True
            continue
        if "nearby" in line:
            other = True
            your = False
            continue
        if fieldos:
            value = line.strip().split(": ")
            key, ranges = value
            first_range, second_range = ranges.split(" or ")
            fields[key].append(first_range)
            fields[key].append(second_range)
        else:
            value = line.strip().split(",")
            if your:
                your_ticket = list(map(int, value))
            if other:
                other_tickets[other_index] = list(map(int, value))
                other_index += 1

invalids = 0
new_others = defaultdict(list)
bad = False

for key, value in other_tickets.items():   #PART 1
    bad = False
    for val in value:
        some_good = False
        for _, conditions in fields.items():
            if some_good:
                break
            for cond in conditions:
                lower, upper = map(int, cond.split("-"))
                if lower <= val <= upper:
                    some_good = True
                    break
        if not some_good:
            invalids += val
            bad = True
    if not bad:
        new_others[key] = value

print(invalids)
