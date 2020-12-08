def do_bs(rows, start, end):
    for index in range(len(rows)):
        mid = start + (end - start) // 2
        ch = rows[index]
        if ch == 'B' or ch == 'R':
            start = mid+1
        else:
            end = mid
    return start


with open('inputs.txt', 'r') as fh:
    boarding_passes = fh.read().splitlines()
    max_seat = float('-inf')
    pouch = set()

    for ticket in boarding_passes:
        rows, cols = ticket[:-3], ticket[-3:]
        row_found , col_found = do_bs(rows, 0, 127), do_bs(cols, 0, 7)
        seat_id = ((row_found * 8) + col_found)
        pouch.add(seat_id)
        max_seat = max(max_seat, seat_id)

    # part 1
    print(max_seat)
    seat, missing_seat = 0,0
    while seat < max_seat:
        if seat not in pouch:
            missing_seat = seat
        seat += 1

    # part 2
    print(missing_seat)
