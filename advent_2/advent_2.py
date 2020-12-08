from collections import Counter
m = []
count = 0

with open('inputs.txt', 'rb') as fh:
    all_lines = fh.readlines()
    for i in all_lines:
        _range, _char, _value = i.split(' ')
        alpha = _char[:-1]
        start, end = _range.split('-')
        c = Counter(_value)
        # part 1
        if int(start) <= c[alpha] <= int(end):
            count += 1
        # part 2
        if _value[int(start) - 1] == alpha and _value[int(end) - 1] != alpha:
            count += 1
        elif _value[int(start) - 1] != alpha and _value[int(end) - 1] == alpha:
            count += 1
    print(count)