class Keypad(object):
    def __init__(self, num):
        self.num = num
        self.code = ""

    def up(self):
        pass

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def select(self):
        self.code += str(self.num)
        return self.num

    def enter(self):
        return self.code


class Standard(Keypad):
    def up(self):
        if self.num > 3:
            self.num -= 3

    def down(self):
        if self.num < 7:
            self.num += 3

    def left(self):
        if (self.num % 3) != 1:
            self.num -= 1

    def right(self):
        if (self.num % 3) != 0:
            self.num += 1


class Designed(Keypad):
    KEY_A, KEY_B, KEY_C, KEY_D = (10, 11, 12, 13)

    def __init__(self, num):
        self.CODE = [str(x) for x in range(10)]
        self.CODE.extend(['A', 'B', 'C', 'D'])
        super(Designed, self).__init__(num)

    def up(self):
        if self.num == 3 or self.num == self.KEY_D:
            self.num -= 2
        elif self.num in [6, 7, 8, self.KEY_A, self.KEY_B, self.KEY_C]:
            self.num -= 4

    def down(self):
        if self.num == 1 or self.num == self.KEY_B:
            self.num += 2
        elif (1 < self.num < 5) or (5 < self.num < 9):
            self.num += 4

    def left(self):
        if self.num not in [1, 2, 5, self.KEY_A, self.KEY_D]:
            self.num -= 1

    def right(self):
        if self.num not in [1, 4, 9, self.KEY_C, self.KEY_D]:
            self.num += 1

    def select(self):
        print(self.num)
        self.code += self.CODE[self.num]
        return self.num


def bathroom_code(instructions, keypad):
    for instruction in instructions:
        for direction in instruction.strip():
            if direction == 'U':
                keypad.up()
            elif direction == 'D':
                keypad.down()
            elif direction == 'L':
                keypad.left()
            elif direction == 'R':
                keypad.right()
                # print(direction, current_num)
        keypad.select()
        # print(code)
    return keypad.enter()


if __name__ == '__main__':
    with open('../../../data/2016/input.2.txt', 'r') as fh:
        instructions = fh.readlines()
        print(bathroom_code(instructions, Standard(5)))
        print(bathroom_code(instructions, Designed(5)))
