m = {}
def two_sum(k, target):
    for i in k:
        key = target-i
        if key in m:
            return m[key] * i
        else:
            m[i] = i

def three_sum(k):
    k.sort()
    for i in range(len(k)):
        for j in range(i+1, len(k)):
            val = two_sum(k, 2020-k[j])
            if val is not None:
                return val * k[j]

with open('inputs.txt', 'rb') as fh:
    all_lines = fh.readlines()
    k  = [int(i) for i in all_lines]
    print(three_sum(k))