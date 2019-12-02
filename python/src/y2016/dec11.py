from collections import deque
from copy import deepcopy
from itertools import combinations


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
    """
    :param items: Items on floor
    :return (set of microchip/generator pairs, set of lone microchips, set of lone generators)
    """
    generator_names = {x.name for x in filter_generators(items)}
    microchip_names = {x.name for x in filter_microchips(items)}
    paired = generator_names.intersection(microchip_names)
    unpaired_microchips = microchip_names - paired
    unpaired_generators = generator_names - paired
    return paired, unpaired_microchips, unpaired_generators


def safe(items):
    """"
    Paired microchips are safe.
    Unpaired microchips are killed if on the same floor / elevator
    as a generator, whether or not the generator is paired
    :param items: Items on floor
    """
    paired, unpaired_microchips, unpaired_generators = pair(items)
    if len(paired) + len(unpaired_generators) == 0 or len(unpaired_microchips) == 0:
        return True


class Configuration:
    def __init__(self, items=None, elevator_floor=None, previous_step=None):
        if previous_step:
            self.items = deepcopy(previous_step.items)
            self.elevator_floor = previous_step.elevator_floor
        else:
            if items:
                self.items = deepcopy(items)
            else:
                self.items = [None] * 5
        if elevator_floor is not None:
            self.elevator_floor = elevator_floor

    def floor(self, num):
        return self.items[num]

    def elevator(self):
        return self.items[0]

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
        return "{0}:{1}".format(self.elevator_floor,
                                ",".join("{0}.{1}.{2}.{3}.".format(floor,
                                                                   len(paired[floor][0]),
                                                                   len(paired[floor][1]),
                                                                   len(paired[floor][2]))
                                         for floor in range(no_floors)))

    def is_safe(self):
        """" Paired microchips are safe. Unpaired microchips are killed if on the
        same floor / elevator as a generator, whether or not the generator is paired """
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
        items = self.items[self.elevator_floor]
        possible_moves = list()
        if self.elevator_floor < 3:
            # Prioritize moving 2 items up, then moving 1 item up
            floor = self.elevator_floor + 1
            possible_moves.extend((floor, item_pair) for item_pair in combinations(items, 2))
            possible_moves.extend((floor, [item]) for item in items)

        if self.elevator_floor > 0:
            # Don't move items back down if all lower floors are empty
            items_on_lower_floor = sum(len(x) for x in self.items[:self.elevator_floor])
            if items_on_lower_floor > 0:
                # Prioritize moving one item down, then moving 2 items down
                floor = self.elevator_floor - 1
                possible_moves.extend((floor, [item]) for item in items)
                possible_moves.extend((floor, item_pair) for item_pair in combinations(items, 2))

        for floor, items in possible_moves:
            next_config = Configuration(previous_step=self, elevator_floor=floor)
            # print("Move ", items, "from floor", self.elevator_floor, "to floor", floor)
            next_config.move(items, from_floor=self.elevator_floor, to_floor=floor)
            if next_config.is_safe():
                moves.append(next_config)

        return moves

    def __repr__(self):
        r = []
        for floor, items in enumerate(self.items[::-1]):
            floor = 4 - floor
            r.append("F{0} {1} {2}".format(floor, 'E' if self.elevator_floor == floor else ' ',
                                           ', '.join(str(item) for item in items)))
        return "\n".join(r)


class Factory:
    def __init__(self, instructions, extra_items=None):
        self.steps = list()
        self.configurations = set()
        self.start_configuration = None
        self.parse(instructions, extra_items)

    def parse(self, instructions, extra_items):
        """ This ugly parser caused me hours of extra work. Time well spent.
        :param instructions:
        :param extra_items: Extra items not included in the directions
        """
        if not extra_items:
            extra_items = dict()
        floor_list = [None] * 4
        for floor, i in enumerate(instructions):
            items = i.split(' a ')
            floor_list[floor] = list()
            for item in items[1:]:
                space_split = item.split(' ')
                item_name = space_split[0].split('-')[0]
                item_type = space_split[1].rstrip().rstrip('.,')
                floor_list[floor].append(Item(item_name, item_type))
            if floor in extra_items:
                floor_list[floor].extend(extra_items[floor])

        self.start_configuration = Configuration(items=floor_list, elevator_floor=0)
        self.configurations.add(self.start_configuration.configuration_key())

    def run(self):
        """
        A lovely BFS of the configuration space.
        Don't revisit nodes, or nodes congruent to the ones already visited.
        """
        visit = deque()
        root = (self.start_configuration, [])
        visit.append(root)
        while visit:
            current_state, moves = visit.popleft()
            if current_state.is_done():
                # Break at the first match; since we're using DFS we don't
                # need to continue further.
                self.steps = moves + [current_state]
                return
            else:
                not_seen_children = list()
                for state in current_state.get_moves():
                    if state.configuration_key() not in self.configurations:
                        not_seen_children.append((state, moves + [current_state]))
                        self.configurations.add(state.configuration_key())
                visit.extend(not_seen_children)

    @staticmethod
    def dump_path(path):
        print('-' * 50)
        for step, config in enumerate(path):
            print("Step ", step + 1)
            print(config)

    def minimum_steps(self):
        return len(self.steps[1:])

    def get_steps(self):
        return self.steps


if __name__ == '__main__':
    with open('../../../data/2016/input.11.txt', 'r') as fh:
        start_setup = fh.readlines()

    factory = Factory(start_setup)
    factory.run()
    print("Part 1: Minimum number of steps", factory.minimum_steps())

    factory_b = Factory(start_setup, extra_items={0: [Item('elerium', 'generator'),
                                                      Item('elerium', 'microchip'),
                                                      Item('dilithium', 'generator'),
                                                      Item('dilithium', 'microchip')]})
    factory_b.run()
    print("Part 2: Minimum number of steps", factory_b.minimum_steps())
