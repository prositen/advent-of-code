import re

__author__ = 'anna'


class Reindeer(object):
    RE_REINDEER = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')

    def __init__(self, rule):
        result = re.match(self.RE_REINDEER, rule)
        if result:
            self.name = result.group(1)
            self.speed = int(result.group(2))
            self.speed_duration = int(result.group(3))
            self.rest_duration = int(result.group(4))
            self.score = 0
            self.time = 0
            self.location = 0
        else:
            raise ValueError("Rule on wrong format ({0})".format(rule))

    def __repr__(self):
        return "{0} can fly {1} km/s for {2} seconds, but then must rest for {3} seconds.".format(self.name, self.speed, self.speed_duration, self.rest_duration)

    def reset(self):
        self.score = 0
        self.time = 0

    def set_time(self, time):
        cycle = self.speed_duration + self.rest_duration

        cycles_done = time // cycle
        seconds_in_cycle = time % cycle
        self.location = self.speed * (cycles_done * self.speed_duration + min(seconds_in_cycle, self.speed_duration))
        self.time = time

    def increase_score(self):
        self.score += 1

    def tick(self):
        self.time += 1
        self.set_time(self.time)


def parse_reindeer(reindeer_rules):
    reindeer = dict()
    for rule in reindeer_rules:
        r = Reindeer(rule)
        reindeer[r.name] = r
    return reindeer


def leader(reindeer, key):
    return max(reindeer.values(), key=key)


def winner(reindeer_rules, seconds):
    reindeer = parse_reindeer(reindeer_rules)
    for r in reindeer.values():
        r.set_time(seconds)

    return leader(reindeer, lambda k: k.location)


def winner_ticks(reindeer_rules, seconds):
    reindeer = parse_reindeer(reindeer_rules)
    for x in range(seconds):
        for r in reindeer.values():
            r.tick()
        # Find the location of the leader, and give a point to every reindeer
        # with the same location
        l = leader(reindeer, lambda k: k.location)
        for r in reindeer.values():
            if r.location == l.location:
                reindeer[r.name].increase_score()

    return leader(reindeer, key=lambda k: k.score)


def main():
    with open('../../data/input.14.txt', 'r') as fh:
        r = winner(fh.readlines(), 2503)
        print("The winning reindeer is {name} with {location} km traveled.".format(name=r.name, location=r.location))
        fh.seek(0)
        r = winner_ticks(fh.readlines(), 2503)
        print("The winning reindeer with tick rules is {name} with a score of {score}.".format(name=r.name, score=r.score))


if __name__ == '__main__':
    main()