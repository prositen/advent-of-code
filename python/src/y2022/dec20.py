from collections import deque

from python.src.common import Day, timer, Timer


def mix(numbers, mixes=1):
    """ Using the deque as a circular list.
    `data` contains the numbers
    `indexes` contains the original order of the numbers

    By always rotating both lists we keep a record of the original order
    connected to the actual numbers.

    Using tuples or a custom class could work too, but then it wouldn't be as
    easy to look up where we are.
    """

    length = len(numbers)
    data = deque(numbers)
    indexes = deque(range(0, len(numbers)))

    def rotate(steps=1):
        data.rotate(-steps)
        indexes.rotate(-steps)

    for _ in range(mixes):
        for index in range(length):
            # Rotate so that the current working number is first in the queue
            current_index = indexes.index(index)
            rotate(current_index)

            data_value = data.popleft()
            index_value = indexes.popleft()

            rotate(data_value)
            data.appendleft(data_value)
            indexes.appendleft(index_value)

    zero = data.index(0)
    return sum(data[(zero + x) % length] for x in (1000, 2000, 3000))


class Dec20(Day, year=2022, day=20):

    @staticmethod
    def parse_instructions(instructions):
        return Dec20.parse_int_lines(instructions=instructions)

    @timer(part=1)
    def part_1(self):
        return mix(self.instructions)

    @timer(part=2)
    def part_2(self):
        numbers = [811589153 * n for n in self.instructions]
        return mix(numbers, mixes=10)


if __name__ == '__main__':
    with Timer('Total'):
        Dec20().run_day()
