import sys
from collections import deque

from python.src.common import Day, timer, Timer


class Defragger(object):
    def __init__(self, disk_map):
        self.blocks = [0 for _ in range(sum(disk_map))]
        self.files = deque()
        self.free_space = deque()
        self.file_size = 0
        pos = 0
        for n, size in enumerate(disk_map):
            index, is_space = divmod(n, 2)
            end_pos = pos + size
            if is_space:
                self.blocks[pos:end_pos] = (-1,) * size
                if size > 0:
                    self.free_space.append((pos, size))
            else:
                self.blocks[pos:end_pos] = (index,) * size
                self.file_size += size
                self.files.append((index, pos, size))
            pos = end_pos

    def deallocate(self, pos, size):
        self.blocks[pos:pos + size] = (-1,) * size
        if len(self.free_space) and self.free_space[-1][0] > pos:
            _, right_size = self.free_space.pop()
            size += right_size

        while pos > 0 and self.blocks[pos - 1] == -1:
            pos -= 1
            size += 1
        if len(self.free_space):
            space_pos, space_size = self.free_space.pop()
            while self.free_space and space_pos > pos:
                space_pos, space_size = self.free_space.pop()
            if space_pos != pos:
                self.free_space.append((space_pos, space_size))
        self.free_space.append((pos, size))

    def defrag_by_block(self):
        while len(self.free_space) > 1:
            file_index, file_pos, file_size = self.files.pop()
            self.deallocate(file_pos, file_size)

            left_to_place = file_size
            while left_to_place > 0:
                space_pos, space_size = self.free_space.popleft()
                if left_to_place > space_size:
                    place_size = space_size
                else:  # left_to_place <= space_size:
                    place_size = left_to_place
                    if (space_size := (space_size - left_to_place)) > 0:
                        self.free_space.appendleft((space_pos + place_size, space_size))

                self.blocks[space_pos:space_pos + place_size] = (file_index,) * place_size
                left_to_place -= place_size

    def defrag_by_file(self):
        while self.files:
            file_index, file_pos, file_size = self.files.pop()
            replace = list()
            while self.free_space:
                space_pos, space_size = self.free_space.popleft()
                if space_pos > file_pos:
                    break
                if space_size < file_size:
                    replace.append((space_pos, space_size))
                else:
                    self.deallocate(file_pos, file_size)
                    if space_size > file_size:
                        self.free_space.appendleft((space_pos + file_size, space_size - file_size))

                    self.blocks[space_pos:space_pos + file_size] = (file_index,) * file_size
                    break
            self.free_space.extendleft(replace[::-1])

    def checksum(self):
        return sum(
            index * max(file_id, 0) for index, file_id in enumerate(self.blocks)
        )

    def print(self, file=sys.stdout):
        print(''.join('#' if c >= 0 else '.' for c in self.blocks),
              file=file)


class Dec09(Day, year=2024, day=9):

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_digits(instructions)

    @timer(part=1)
    def part_1(self):
        df = Defragger(self.instructions)
        df.defrag_by_block()
        return df.checksum()

    @timer(part=2)
    def part_2(self):
        df = Defragger(self.instructions)
        df.defrag_by_file()
        return df.checksum()


if __name__ == '__main__':
    with Timer('Total'):
        Dec09().run_day()
