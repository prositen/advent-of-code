from collections import deque
from copy import deepcopy
from enum import IntEnum
from itertools import combinations, product


class Item:
    def __init__(self, name, item_type):
        self.name = name
        self.type = item_type

    def __repr__(self):
        return "<Item {0} {1}>".format(self.name, self.type)

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type


def filter_generators(items):
    return [item for item in items if item.type == 'generator']


def filter_microchips(items):
    return [item for item in items if item.type == 'microchip']


def pair(items):
    generator_names = {x.name for x in filter_generators(items)}
    microchip_names = {x.name for x in filter_microchips(items)}
    paired = generator_names.intersection(microchip_names)
    unpaired_microchips = microchip_names - paired
    unpaired_generators = generator_names - paired
    return paired, unpaired_microchips, unpaired_generators

def safe(items):
    paired, unpaired_microchips, unpaired_generators = pair(items)
    if len(paired) + len(unpaired_generators) == 0 or len(unpaired_microchips) == 0:
        return True

class Floor(IntEnum):
    ELEVATOR = 0
    FLOOR_1 = 1
    FLOOR_2 = 2
    FLOOR_3 = 3
    FLOOR_4 = 4


class Configuration:
    def __init__(self, items=None, elevator_floor=None, previous_step=None):
        if previous_step:
            self.items = deepcopy(previous_step.items)
            self.elevator_floor = previous_step.elevator
        else:
            if items:
                self.items = deepcopy(items)
            else:
                self.items = [None] * 5
        if elevator_floor:
            self.elevator_floor = elevator_floor

    def floor(self, num):
        return self.items[num]

    def elevator(self):
        return self.items[Floor.ELEVATOR]

    def configuration_key(self):
        """ Two configurations are congruent if they have the same
        * Elevator position
        and number of
        * paired microchips / elements
        * unpaired elements
        * unpaired microchips
        per floor
        """
        no_floors = len(self.items)
        paired = self.__pair()
        return self.elevator_floor, frozenset([(floor, len(paired[floor][0]), len(paired[floor][1]), len(paired[floor][2]))
                                     for floor in range(no_floors)])

    def is_safe(self):
        """" Paired microchips are safe. Unpaired microchips are killed if on the same floor / elevator
        as a generator, whether or not the generator is paired """

        return all(safe(x) for x in self.items)

    def is_done(self):
        lengths = [len(x) for x in self.items]
        return sum(lengths[:-1]) == 0

    def __pair(self):
        return [pair(self.items[x]) for x in range(len(self.items))]

    def move(self, items, from_floor, to_floor):
        if isinstance(items, Item):
            items = [items]
        for x in items:
            self.items[from_floor].remove(x)
            self.items[to_floor].append(x)

    def get_moves(self):
        moves = list()
        items = self.floor(self.elevator_floor)
        to_elevator = [x for x in items] + list(combinations(items, 2))
        next_floor = list()
        if self.elevator_floor > Floor.FLOOR_1:
            next_floor.append(self.elevator_floor - 1)
        if self.elevator_floor < Floor.FLOOR_4:
            next_floor.append(self.elevator_floor + 1)

        # print([x for x in product(next_floor, to_elevator)])
        for floor, items in product(next_floor, to_elevator):
            next_config = Configuration(previous_step=self, elevator_floor=floor)
            print("Move ", items, "from floor", self.elevator_floor, "to floor", floor)
            next_config.move(items, from_floor=self.elevator_floor, to_floor=floor)
            if next_config.is_safe():
                moves.append(next_config)
                print("safe")
            else:
                print(next_config.items)
                print("unsafe")

        return moves


class Factory:
    def __init__(self, instructions):
        self.visited = dict()
        self.steps = list()
        self.configurations = dict()
        self.start_configuration = None
        self.parse(instructions)

    def parse(self, instructions):
        """ A really ugly parser """
        floor_list = [None] * 5
        floor_list[0] = list()
        for floor, i in enumerate(instructions):
            floor += 1
            items = i.split(' a ')
            floor_list[floor] = list()
            for item in items[1:]:
                space_split = item.split(' ')
                item_name = space_split[0].split('-')[0]
                item_type = space_split[1]
                if item_type[-1] == '.':
                    item_type = item_type[:-1]
                floor_list[floor].append(Item(item_name, item_type))
                # print(floor, floor_list[floor])
        self.start_configuration = Configuration(items=floor_list, elevator_floor=1)

    def run(self):
        visit = deque()
        paths = list()
        visit.extend([(self.start_configuration, next_move, []) for next_move in self.start_configuration.get_moves()])
        while visit:
            prev_state, move, moves = visit.popleft()
            key = move.configuration_key()
            if key in self.configurations:
                print("skipped", move)
                continue
            print("run", prev_state, move, moves)
            current_state = move
            if current_state.is_done():
                paths.append(moves)
            else:
                visit.extend((current_state, next_move, moves + [prev_state]) for next_move in current_state.get_moves())
        print(paths)

    def minimum_steps(self):
        pass

    def steps(self):
        pass
