def part_2():
    pass

def part_1():
    pass


def parse(data):
    pass

with open('samples.txt', 'r') as fh:
    data = fh.read().splitlines()
    time = int(data[0])
    buses = []
    for i in data[1].split(','):
        if i != 'x':
            buses.append(int(i))

    print(time, buses)

    early= []
    for i in buses:
        early.append([i - (time % i), i])
    op = sorted(early)[0]
    print(op[0] * op[1])

    one = buses[0]
    last = buses[-1]

    prod = 1
    for i in buses:
        prod *= i

    x = 0
    for i in buses:
        x += (prod / i)
    #print(x)

    k = prod
    s = set(buses[1:-1])
    for i in range(prod):
        first = i / one
        end = (i + len(data[1])) / last
        if (i % one == 0 and (i + len(data[1])) % last == 0):
            x = i+1
            for j in buses[1:-1]:
                if x % j == 0:
                    print(x, j)
                x += 1
            break




    # 100000000000000
    # 239870524100149
    #processed_data = parse(data)

    # data = []
    #
    # with open('samples.txt', 'r') as f:
    #     for cnt, line in enumerate(f):
    #         data.append(line.strip())
    # buses = data[1].split(',')
    #
    # index = -1
    # schedule = []
    # for bus in buses:
    #     index += 1
    #
    #     if bus == 'x':
    #         continue
    #     bus = int(bus)
    #     schedule.append((bus, index))
    # print(schedule)
    # #
    # b_index = 0
    # bus, time = schedule[b_index]
    # index = time
    # interval = bus
    # first_hit = -1
    # while b_index < len(schedule):
    #
    #     # Once we find a true one for the second index... then we know that will be interval to try for the third...
    #     # found = True
    #     my_l = (index + time) % bus
    #     if my_l == 0:
    #
    #         if first_hit == -1:
    #             #print('First Hit for bus {bus} at time {index} - Interval {interval}')
    #             first_hit = index
    #         else:
    #             b_index += 1
    #             interval = index - first_hit
    #             #print(f'Second Hit for bus {bus} at time {index} - new Interval {interval}')
    #             index = first_hit - interval
    #             first_hit = -1
    #             bus, time = schedule[b_index]
    #     index += interval
    #
    # print(first_hit)

    from functools import reduce
    import math


    def get_inverse(N_i, n_i):
        while N_i > n_i:
            N_i = int(N_i % n_i)
        x_i = 0
        while int((N_i * x_i) % n_i) != 1:
            x_i += 1
        return int(x_i)


    def main():
        filename = 'inputs.txt'
        # filename = 'example2'

        with open(filename, 'r') as infile:
            timestamp = int(infile.readline().strip())
            bus_IDs = [(int(i), (int(i) - index) % (int(i)), index)
                       for index, i in enumerate(
                    infile.readline().strip().split(",")) if i != 'x']
            print(bus_IDs)
        N = reduce(lambda x, y: x * y, [bus[0] for bus in bus_IDs])
        print(N)
        x = 0
        for n_i, b_i, i in bus_IDs:
            N_i = N // n_i
            x_i = get_inverse(N_i, n_i)
            x += b_i * x_i * N_i

        print(int(x % N))


    if __name__ == "__main__":
        main()

    #294354277694107