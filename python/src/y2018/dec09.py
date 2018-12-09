from python.src.common import Day


class Dec09(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 9, instructions, filename)
        self.players = 0
        self.last_marble = 0
        self.players, self.last_marble = self.instructions[0], self.instructions[1]

    @staticmethod
    def parse_instructions(instructions):
        w = instructions[0].split()
        return int(w[0]), int(w[6])

    def part_1(self):
        return Game(players=self.players, last_marble=self.last_marble).run()

    def part_2(self):
        return Game(players=self.players, last_marble=self.last_marble * 100).run()


class Marble(object):

    def __init__(self, value):
        self.value = value
        self.next = self
        self.prev = self

    def insert_and_next(self, m):
        m.next = self.next
        m.next.prev = m

        m.prev = self
        self.next = m
        return m

    def remove_and_next(self):
        n = self.next
        n.prev = self.prev
        self.prev.next = n
        return n


class Game(object):
    def __init__(self, players, last_marble):
        self.players = players
        self.last_marble = last_marble
        self.current_marble = Marble(0)
        self.scores = [0] * players

    def place(self, player, value):
        if value % 23 == 0:
            for _ in range(7):
                self.current_marble = self.current_marble.prev
            self.scores[player] += value + self.current_marble.value
            self.current_marble = self.current_marble.remove_and_next()
        else:
            self.current_marble = self.current_marble.next.insert_and_next(Marble(value))

    def run(self):
        player = 1
        for marble in range(1, self.last_marble + 1):
            self.place(player, marble)
            player = (player + 1) % self.players
        return max(self.scores)


if __name__ == '__main__':
    d = Dec09()
    print("Winning score with", d.last_marble, "marbles: ", d.part_1())
    print("Winning score with", d.last_marble * 100, "marbles:", d.part_2())
