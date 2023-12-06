import itertools
from functools import lru_cache

from python.src.common import Day, timer, Timer


class SeedAlmanac(object):

    def __init__(self, seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water,
                 water_to_light, light_to_temperature, temperature_to_humidity,
                 humidity_to_location):
        self.seeds = seeds
        self.seed_ranges = [(seeds[x], seeds[x] + seeds[x + 1])
                            for x in range(0, len(seeds), 2)]
        self.seed_to_soil = self.parse_mapping(seed_to_soil)
        self.soil_to_fertilizer = self.parse_mapping(soil_to_fertilizer)
        self.fertilizer_to_water = self.parse_mapping(fertilizer_to_water)
        self.water_to_light = self.parse_mapping(water_to_light)
        self.light_to_temperature = self.parse_mapping(light_to_temperature)
        self.temperature_to_humidity = self.parse_mapping(temperature_to_humidity)
        self.humidity_to_location = self.parse_mapping(humidity_to_location)

    @staticmethod
    def parse_mapping(mapping):
        f_mapping = list()
        for line in mapping[1:]:
            line = list(map(int, line.split()))
            f_mapping.append((line[1], line[1] + line[2], line[0] - line[1]))
        return [(r[0], r[1], r[2]) for r in sorted(f_mapping)]

    @staticmethod
    def lookup_in(lookup, mapping):
        for start, end, value in mapping:
            if lookup in range(start, end):
                return value + lookup
        return lookup

    def find_location_for_seed(self, seed):
        """
        Brute attempt just doing the plain lookups
        :param seed: Do lookup chain for this seed
        :return: location
        """
        soil = self.lookup_in(seed, self.seed_to_soil)
        fertilizer = self.lookup_in(soil, self.soil_to_fertilizer)
        water = self.lookup_in(fertilizer, self.fertilizer_to_water)
        light = self.lookup_in(water, self.water_to_light)
        temp = self.lookup_in(light, self.light_to_temperature)
        hum = self.lookup_in(temp, self.temperature_to_humidity)
        return self.lookup_in(hum, self.humidity_to_location)

    def find_lowest_location(self, part):
        if part == 1:
            seed_lookup = set((r, r + 1, 0) for r in self.seeds)
        else:
            seed_lookup = set((r[0], r[1], 0) for r in self.seed_ranges)
        seed_mapping = self.split_ranges(seed_lookup=seed_lookup)
        return min((r[0] + r[2]) for r in seed_mapping)

    def split_ranges(self, seed_lookup):
        """
        This monster of a function makes a unified lookup function from the given
        seed ranges to possible locations by chaining the lookup ranges, splitting
        them whenever necessary.
        """
        mappings = (self.seed_to_soil,
                    self.soil_to_fertilizer,
                    self.fertilizer_to_water,
                    self.water_to_light,
                    self.light_to_temperature,
                    self.temperature_to_humidity,
                    self.humidity_to_location)

        for next_step in mappings:
            next_seed = set()
            while seed_lookup:
                seed_start, seed_stop, seed_delta = seed_lookup.pop()
                range_start = seed_start + seed_delta
                range_stop = seed_stop + seed_delta
                for start, stop, delta in next_step:
                    new_seed_delta = seed_delta + delta
                    if start <= range_start < stop:
                        if range_stop <= stop:
                            next_seed.add((seed_start, seed_stop, new_seed_delta))
                        else:
                            next_seed.add((seed_start, stop - seed_delta,
                                           new_seed_delta))
                            seed_lookup.add((stop - seed_delta, seed_stop,
                                             seed_delta))
                        break

                    elif start < range_stop <= stop:
                        next_seed.add((start - seed_delta, seed_stop,
                                       new_seed_delta))
                        seed_lookup.add((seed_start, start - seed_delta, seed_delta))
                        break
                else:
                    next_seed.add((seed_start, seed_stop, seed_delta))
            seed_lookup = next_seed
        return seed_lookup


class Dec05(Day, year=2023, day=5):

    @staticmethod
    def parse_instructions(instructions):
        seeds = list(map(int, instructions[0][6:].split()))
        return SeedAlmanac(seeds, *Day.parse_groups(instructions[2:]))

    @timer(part=1)
    def part_1(self):
        almanac = self.instructions
        return min(almanac.find_location_for_seed(s)
                   for s in almanac.seeds)
        # Can also use
        # return almanac.find_lowest_location(part=1)

    @timer(part=2)
    def part_2(self):
        almanac = self.instructions
        return almanac.find_lowest_location(part=2)


if __name__ == '__main__':
    with Timer('Total'):
        Dec05().run_day()
