def change(line, instructions):
    if instructions[line][0] == "jmp": instructions[line][0] = "nop"
    elif instructions[line][0] == "nop": instructions[line][0] = "jmp"
    return instructions


def part_2(instructions):
    pc,halt = 0,0
    while not halt:
        change(pc, instructions)
        acc, fin = part_1(instructions)
        if not fin:
            change(pc, instructions)
            pc += 1
        else:
            break
    return acc


def part_1(instruction_set):
    pc, acc, fin = 0,0,0
    executed = set()
    while pc not in executed:
        if pc == len(instruction_set):
            fin = 1
            break
        opcode, value = instruction_set[pc][0], instruction_set[pc][1]
        executed.add(pc)
        if opcode == "acc":
            acc += value
            pc += 1
        elif opcode == "jmp":
            pc += value
        else:
            pc += 1
    return acc, fin

with open('inputs.txt', 'r') as fh:
    data = fh.read().splitlines()
    instruction_set = [i.split() for i in data]
    for line in range(len(instruction_set)):
        instruction_set[line][1] = int(instruction_set[line][1])

part1 = part_1(instruction_set)[0]
part2 = part_2(instruction_set)
print(part1)
print(part2)