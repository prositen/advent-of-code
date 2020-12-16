from python.src.common import Day, timer, Timer
from src.y2019.intcode import IntCode


class Dec25(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 25, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    @staticmethod
    def parse_room(output):
        desc = [row for row in (row.strip() for row in output.splitlines()) if row]
        room = desc.pop(0)[3:-3]
        door_start, door_end = 0,0
        items_start, items_end = 0,0
        command = 0
        description = []
        for index, line in enumerate(desc):
            if line.startswith('Doors here'):
                description = desc[0:index-1]
                door_start = index+1
            elif line.startswith('Items here'):
                items_start = index+1
                if door_start and not door_end:
                    door_end = index
            elif line == 'Command?':
                if not door_end:
                    door_end = index
                elif not items_end:
                    items_end = index
                command = index

        if not command:
            raise BaseException('Game over')

        items = []
        if items_start and items_end:
            items = [item[2:] for item in desc[items_start:items_end]]
        doors = []
        if door_start and door_end:
            doors = [door[2:] for door in desc[door_start:door_end]]
        return room, description, doors, items

    @timer(part=1)
    def play(self):
        ic = IntCode(instructions=self.instructions)
        while True:
            if ic.run_and_wait():
                break
            output = ic.get_ascii_string()
            room, description, doors, items = self.parse_room(output)
            print(output)
            command = input()
            if command == 'quit':
                break
            ic.input_ascii_string(command)


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec25()
        d.play()
        # d.part_1()
