import multiprocessing
import re
from collections import Counter, deque, namedtuple
from enum import Enum
from heapq import heappush, heappop

from python.src.common import Day, timer, Timer

State = namedtuple('State',
                   ['ore', 'clay', 'geodes', 'obsidian'])


class Material(Enum):
    ORE = 0
    CLAY = 1
    OBSIDIAN = 2
    GEODE = 3

    def __str__(self):
        return self.name.lower()

    def __lt__(self, other):
        return self.value < other.value


class Blueprint(object):

    def __init__(self, instructions):
        self.recipes = {
            Material.ORE: State(ore=instructions[0], clay=0, obsidian=0, geodes=0),
            Material.CLAY: State(ore=instructions[1], clay=0, obsidian=0, geodes=0),
            Material.OBSIDIAN: State(ore=instructions[2], clay=instructions[3],
                                     obsidian=0, geodes=0),
            Material.GEODE: State(ore=instructions[4], clay=0,
                                  obsidian=instructions[5], geodes=0)
        }


class Factory(object):
    def __init__(self, blueprint: Blueprint):
        self.recipes = blueprint.recipes
        self.robots = Counter({Material.ORE: 1})
        self.materials = Counter()
        self.geodes = 0
        self.time = 0
        self.building = None
        self.max_ore = sum(x.ore for x in self.recipes.values())
        self.max_clay = sum(x.clay for x in self.recipes.values())
        self.max_obsidian = sum(x.obsidian for x in self.recipes.values())

    def should_build(self, robot, materials, robots):
        enough_obsidian = robots.obsidian >= self.max_obsidian
        enough_clay = robots.clay >= self.max_clay
        enough_ore = robots.ore >= self.max_ore
        match robot:
            case Material.GEODE:
                return (materials.ore >= self.recipes[Material.GEODE].ore
                        and materials.obsidian >= self.recipes[Material.GEODE].obsidian)
            case Material.OBSIDIAN:
                if enough_obsidian:
                    return False
                return (materials.ore >= self.recipes[Material.OBSIDIAN].ore
                        and materials.clay >= self.recipes[Material.OBSIDIAN].clay)
            case Material.CLAY:
                if enough_obsidian or enough_clay:
                    return False
                return materials.ore >= self.recipes[Material.CLAY].ore
            case Material.ORE:
                if enough_obsidian or enough_ore:
                    return False
                return materials.ore >= self.recipes[Material.ORE].ore

    def collect(self, materials: State, robots: State):
        return State(ore=min(materials.ore + robots.ore, 2 * self.max_ore),
                     clay=min(materials.clay + robots.clay, 2 * self.max_clay),
                     obsidian=min(materials.obsidian + robots.obsidian, 2 * self.max_obsidian),
                     geodes=materials.geodes + robots.geodes)
        # return State(ore=materials.ore + robots.ore,
        #             clay=materials.clay + robots.clay,
        #             obsidian=materials.obsidian + robots.obsidian,
        #             geodes=materials.geodes + robots.geodes)

    def build(self, robot, materials: State, robots: State):
        needed_materials = self.recipes[robot]
        match robot:
            case Material.ORE:
                return (materials._replace(ore=materials.ore - needed_materials.ore)), \
                       robots._replace(ore=robots.ore + 1),

            case Material.CLAY:
                return (materials._replace(ore=materials.ore - needed_materials.ore),
                        robots._replace(clay=robots.clay + 1),
                        )
            case Material.OBSIDIAN:
                return (materials._replace(ore=materials.ore - needed_materials.ore,
                                           clay=materials.clay - needed_materials.clay),
                        robots._replace(obsidian=robots.obsidian + 1),
                        )
            case Material.GEODE:
                return (materials._replace(ore=materials.ore - needed_materials.ore,
                                           obsidian=materials.obsidian - needed_materials.obsidian),
                        robots._replace(geodes=robots.geodes + 1),
                        )


class GeoCracker(object):

    def __init__(self, blueprint):
        self.factory = Factory(blueprint=blueprint)

    def run(self, max_time=24):
        to_visit = list()
        to_visit.append((0,
                         State(ore=0, clay=0, geodes=0, obsidian=0),  # materials
                         State(ore=1, clay=0, geodes=0, obsidian=0),  # robots
                         0))  # time
        visited = set()
        max_geodes = 0
        while to_visit:
            # materials, robots, time = to_visit.popleft()
            _, materials, robots, time = heappop(to_visit)
            state = (robots, materials)
            future_geodes = materials.geodes + (robots.geodes * (max_time - time))
            max_geodes = max(max_geodes, future_geodes)
            if time == max_time or state in visited:
                continue

            m_geodes = (future_geodes
                        + ((max_time - time) * (max_time - time + 1) // 2))  # we might pick up
            if m_geodes < max_geodes:
                continue

            visited.add(state)
            if time < max_time:
                for robot in sorted(Material, reverse=True):
                    if self.factory.should_build(robot=robot,
                                                 materials=materials,
                                                 robots=robots):
                        m, r = self.factory.build(robot, materials, robots)
                        m = self.factory.collect(m, robots)
                        # to_visit.append((m, r, time + 1))
                        heappush(to_visit, (-future_geodes, m, r, time + 1))

                m = self.factory.collect(materials, robots)
                # to_visit.append((m, robots, time + 1))
                heappush(to_visit, (-future_geodes, m, robots, time + 1))
        return max_geodes


def quality_crack(bp):
    gc = GeoCracker(bp[1]).run(max_time=24)
    print(bp[0] + 1, gc)
    return (bp[0] + 1) * gc


def geode_crack(bp):
    gc = GeoCracker(bp).run(max_time=32)
    print(gc)
    return gc


class Dec19(Day, year=2022, day=19):

    def __init__(self, instructions=None, filename=None):
        super().__init__(instructions=instructions, filename=filename)
        self.blueprints = [Blueprint(i) for i in self.instructions]

    @staticmethod
    def parse_instructions(instructions):
        pattern = re.compile(r'\d+')
        return [
            list(map(int, pattern.findall(line)[1:]))
            for line in instructions
        ]

    @timer(part=1)
    def part_1(self):
        with multiprocessing.Pool() as pool:
            results = 0
            for result in pool.map(quality_crack, enumerate(self.blueprints)):
                results += result
        return results

        # for index, blueprint in self.blueprints.items():
        #    g = GeoCracker(blueprint=blueprint)
        #    geodes = g.run()
        #    print(index + 1, geodes)
        #    total += (index + 1) * geodes
        # return total

    @timer(part=2)
    def part_2(self):
        with multiprocessing.Pool() as pool:
            results = 1
            for result in pool.map(geode_crack, self.blueprints[:3]):
                results *= result
        return results


if __name__ == '__main__':
    with Timer('Total'):
        Dec19().run_day()
