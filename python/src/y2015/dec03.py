__author__ = 'Anna'


def houses(puzzle_input, santas=1):
    visited = set()
    santa_pos = dict()
    start_pos = (0, 0)
    for i in range(santas):
        santa_pos[i] = start_pos

    visited.add(start_pos)

    for num, instruction in enumerate(puzzle_input):
        santa = num % santas
        pos = santa_pos[santa]
        if instruction == '>':
            pos = (pos[0] + 1, pos[1])
        elif instruction == '<':
            pos = (pos[0] - 1, pos[1])
        elif instruction == '^':
            pos = (pos[0], pos[1] + 1)
        elif instruction == 'v':
            pos = (pos[0], pos[1] - 1)
        visited.add(pos)
        santa_pos[santa] = pos

    return len(visited)


if __name__ == '__main__':
    with open('../../../data/2015/input.3.txt','r') as fh:
        for no, line in enumerate(fh.readlines()):
            print("Instruction {line}: {houses} houses got gifts with 1 santa.".format(line=no, houses=houses(line, 1)))
            print("Instruction {line}: {houses} houses got gifts with 2 santas.".format(line=no, houses=houses(line, 2)))

