import copy
import itertools
from collections import deque

from python.src.common import Day, timer, Timer
from src.y2019.intcode import IntCode


class GameOverException(BaseException):
    pass


class Ship(object):

    def __init__(self, instructions):
        self.doors = dict()
        self.items = {
            'all': set()
        }
        self.shit_list = {'infinite loop'}
        self.ic = IntCode(instructions)

    @staticmethod
    def take_and_walk(ic, item: 'str', doors: 'list[str]'):
        ic = copy.deepcopy(ic)
        output = ic.run_command(f'take {item}')
        if 'Command?' in output:
            output = ic.run_command(doors[0])
            if 'Doors' in output:
                return True
        return False

    def parse_room(self, output):
        desc = [row for row in (row.strip() for row in output.splitlines()) if row]
        room = desc.pop(0)[3:-3]
        if room in self.doors:
            return room
        self.items[room] = set()
        self.doors[room] = list()
        door_start, door_end = 0, 0
        items_start, items_end = 0, 0
        command = False
        for index, line in enumerate(desc):
            if line.startswith('Doors here'):
                door_start = index + 1
            elif line.startswith('Items here'):
                items_start = index + 1
                if door_start and not door_end:
                    door_end = index
            elif line == 'Command?':
                if not door_end:
                    door_end = index
                elif not items_end:
                    items_end = index

        if items_start and items_end:
            self.items[room] = set(item[2:] for item in desc[items_start:items_end])
            self.items[room].difference_update(self.shit_list)

        if door_start and door_end:
            self.doors[room] = {
                door[2:]: None
                for door in desc[door_start:door_end]
            }
        return room

    def map_ship(self):
        output = self.ic.run_command(command=None)
        room = self.parse_room(output)
        to_visit = deque([(copy.deepcopy(self.ic), room)])
        visited = set()

        while to_visit:
            ic, room = to_visit.popleft()
            if room in visited:
                continue
            visited.add(room)

            doors = list(self.doors[room])
            for item in list(self.items[room]):
                if self.take_and_walk(ic, item, doors):
                    self.items['all'].add(item)
                else:
                    self.items[room].remove(item)
            for door in doors:
                next_ic = copy.deepcopy(ic)
                next_room = self.parse_room(next_ic.run_command(door))
                if next_room != 'Pressure-Sensitive Floor':
                    self.doors[room][door] = next_room
                    to_visit.append((next_ic, next_room))

    def find_path(self):
        goal = ('Security Checkpoint', tuple(self.items['all']))
        to_visit = deque([('Hull Breach', (), [])])
        visited = dict()
        while to_visit:
            room, inventory, path = to_visit.popleft()
            best = visited.get((room, inventory), [])
            if 0 < len(best) < len(path):
                continue
            visited[(room, inventory)] = path
            if (room, inventory) == goal:
                continue
            for item in self.items.get(room, []):
                if item not in inventory:
                    path.append(f'take {item}')
                    inventory = tuple(set(inventory + (item,)))
            for door, destination in self.doors.get(room, dict()).items():
                to_visit.append((destination, inventory, path + [door]))
            to_visit = deque(sorted(to_visit, key=lambda c: (-len(c[1]), len(c[2]))))
        return visited[goal]

    def run_commands(self, commands, ic):
        output = list()
        for command in commands:
            output.append(ic.run_command(command))
        return output

    def pass_checkpoint(self):
        all_items = self.items['all']
        more, less = list(), list()
        drop_all = [
            f'drop {item}' for item in all_items
        ]
        self.run_commands(drop_all, self.ic)

        for r in range(1, 7):
            combos = list(itertools.combinations(all_items, r=r))
            for items in combos:
                if any(heavy_items.intersection(items) == heavy_items for heavy_items in less):
                    continue
                commands = [
                    f'take {item}' for item in items
                ]
                commands += ['west']
                output = self.run_commands(commands, ic=copy.deepcopy(self.ic))
                if 'lighter' in output[-1]:
                    less.append(set(items))
                elif 'keypad' in output[-1]:
                    print(output[-1].splitlines()[-1])
                    return


class Dec25(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 25, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    def play(self):
        ic = IntCode(instructions=self.instructions)
        while True:
            if ic.run_and_wait():
                break
            output = ic.get_ascii_string()
            print(output)
            command = input()
            if command == 'quit':
                break
            ic.input_ascii_string(command)

    @timer(part=1)
    def part_1(self, debug=False):
        ship = Ship(instructions=self.instructions)
        with Timer('Map ship'):
            ship.map_ship()
        with Timer('Get items and move to checkpoint'):
            ship.run_commands(commands=ship.find_path(),
                              ic=ship.ic)
        with Timer('Pass checkpoint'):
            ship.pass_checkpoint()


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec25()
        # d.play()
        d.part_1()
