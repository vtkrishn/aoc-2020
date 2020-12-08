def process(family):
    part_1, part_2 = 0,0
    for index in family:
        family_options_all = set()
        family_options_any = {chr(i) for i in range(97, 123)}
        for person in family[index]:
            family_options_any = family_options_any.intersection(set(person))
            for options in person:
                family_options_all.add(options)
        part_1 += len(family_options_all)
        part_2 += len(family_options_any)
    return part_1, part_2


def parse(data):
    family = {}
    person = []
    count = 0
    for i in data:
        if i == '':
            family[count] = person
            person = []
            count += 1
        else:
            person.append(i)
    family[count] = person
    return family


with open('inputs.txt', 'r') as fh:
    data = fh.read().splitlines()
    family = parse(data)
    output = process(family)
    print(output)