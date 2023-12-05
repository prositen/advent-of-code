import itertools
from functools import lru_cache

from python.src.common import Day, timer, Timer


class SeedAlmanac(object):

    def __init__(self, seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water,
                 water_to_light, light_to_temperature, temperature_to_humidity,
                 humidity_to_location):
        self.seeds = seeds
        self.seed_to_soil = self.parse_mapping(seed_to_soil)
        self.soil_to_fertilizer = self.parse_mapping(soil_to_fertilizer)
        self.fertilizer_to_water = self.parse_mapping(fertilizer_to_water)
        self.water_to_light = self.parse_mapping(water_to_light)
        self.light_to_temperature = self.parse_mapping(light_to_temperature)
        self.temperature_to_humidity = self.parse_mapping(temperature_to_humidity)
        self.humidity_to_location = self.parse_mapping(humidity_to_location)

    @staticmethod
    def parse_mapping(mapping):
        result = list()
        for line in mapping[1:]:
            line = list(map(int, line.split()))
            result.append((line[1], line[1] + line[2], line[0] - line[1]))

        return tuple((range(r[0], r[1]), r[2]) for r in sorted(result))

    @staticmethod
    def lookup_in(lookup, mapping):
        for key, value in mapping:
            if lookup in key:
                return value + lookup
        return lookup

    def find_location_for_seed(self, seed):
        soil = self.lookup_in(seed, self.seed_to_soil)
        fertilizer = self.lookup_in(soil, self.soil_to_fertilizer)
        water = self.lookup_in(fertilizer, self.fertilizer_to_water)
        light = self.lookup_in(water, self.water_to_light)
        temp = self.lookup_in(light, self.light_to_temperature)
        hum = self.lookup_in(temp, self.temperature_to_humidity)
        return self.lookup_in(hum, self.humidity_to_location)


class Dec05(Day, year=2023, day=5):

    @staticmethod
    def parse_instructions(instructions):
        seeds = list(map(int, instructions[0][6:].split()))
        return seeds, *Day.parse_groups(instructions[2:])

    @timer(part=1)
    def part_1(self):
        almanac = SeedAlmanac(*self.instructions)
        return min(almanac.find_location_for_seed(s)
                   for s in almanac.seeds)

    @timer(part=2)
    def part_2(self):
        almanac = SeedAlmanac(*self.instructions)
        seeds = itertools.chain(range(almanac.seeds[x], almanac.seeds[x] + almanac.seeds[x + 1])
                                for x in range(0, len(almanac.seeds), 2))
        return min(almanac.find_location_for_seed(s)
                   for r in seeds for s in r)


if __name__ == '__main__':
    with Timer('Total'):
        Dec05().run_day()
