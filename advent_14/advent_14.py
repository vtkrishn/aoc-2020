# def part_2():
#     pass
#
# def part_1():
#     pass
#
#
# def parse(data):
#     pass

# with open('inputs.txt', 'r') as fh:
#     data = fh.read().splitlines()
#
#     masks = {}
#     line = 0
#     index = 0
#     for i in data:
#         masks[index] = [data[line].split(" = "),  data[line + 1].split(" = "), data[line + 2].split(" = "), data[line + 3].split(" = ")]
#         line = line + 4
#         index += 1
#
#     for k, v in masks.items():
#         mask = ''
#         for i in v:
#             value = []
#             if i[0] != 'mask':
#                 memory = int(i[0].replace('mem[','').replace(']',''))
#                 pr = bin(int(i[1])).replace('0b','')
#                 for i in pr:
#                     value.append(i)
#                 for i in range(36-len(value)):
#                     value.insert(0,'0')
#                 #print(memory, value)
#             else:
#                 mask = i[1]
#
#             # if len(value) != 0:
#             #     print(len(mask), len(value))
#             for i in range(len(value)):
#                 if mask[i] == '1':
#                     value[i] = '1'
#                 if mask[i] == '0':
#                     value[i] = '0'
#             if len(value) != 0:
#                 print(int(''.join(value),2))
#
#
#
#
#     processed_data = parse(data)


import re

with open('inputs.txt', 'r') as fh:
	data = fh.read().splitlines()
	memory = {}
	for instr in data:
		if 'mask' in instr:
			mask = instr.split(' = ')[-1].strip()
		else:
			address, value = map(int, re.findall(r'\d+', instr))
			value_bits = '{0:b}'.format(value).zfill(len(mask))
			value_list = []
			for index, bit in enumerate(mask):
				if bit != 'X':
					value_list.append(bit)
				else:
					value_list.append(value_bits[index])
			memory[address] = int(''.join(value_list), 2)
	print(sum(memory.values()))


import itertools
import re

memory, mask = {}, None

for line in open('inputs.txt'):
	if 'mask' in line:
		mask = line.split('=')[-1].strip()
	else:
		address, value = map(int, re.findall(r'\d+', line))
		address_bitstr = '{0:b}'.format(address).zfill(len(mask))
		masked_bitlist = [address_bitstr[i] if mask_bit == '0' else mask[i] for i, mask_bit in enumerate(mask)]

		for bits in itertools.product('01', repeat=masked_bitlist.count('X')):
			bit_iter = iter(bits)
			address_bitlist = (next(bit_iter) if char == 'X' else char for char in masked_bitlist)
			memory[int(''.join(address_bitlist), 2)] = value

print(sum(memory.values()))
# https://github.com/daniel-dara/advent-of-code/blob/master/2020/day14/part2.py

