import functools

from python.src.common import Day, timer, Timer, stringify


class Combat(object):
    def __init__(self, my_cards, their_cards, recursive=False,
                 game_no=1):
        self.my_cards = [c for c in my_cards]
        self.their_cards = [c for c in their_cards]
        self.recursive = recursive
        self.memory = set()
        self.game_no = game_no

    def play(self, debug=False):
        game_round = 1
        while self.my_cards and self.their_cards:
            state = (tuple(self.my_cards), tuple(self.their_cards))
            if state in self.memory:
                if debug:
                    print('Game state has been seen before. Player 1 wins!')
                return True
            self.memory.add(state)
            if debug:
                print(f'-- Round {game_round} (Game {self.game_no}) --')
                print(f'Player 1\'s deck: {stringify(self.my_cards)}')
                print(f'Player 2\'s deck: {stringify(self.their_cards)}')
            my = self.my_cards.pop(0)
            their = self.their_cards.pop(0)

            if debug:
                print(f'Player 1 plays: {my}')
                print(f'Player 2 plays: {their}')
            if self.recursive and my <= len(self.my_cards) and their <= len(self.their_cards):
                if debug:
                    print('Playing a sub-game to determine the winner...\n')
                winner = Combat(self.my_cards[:my], self.their_cards[:their], recursive=True,
                                game_no=self.game_no + 1).play(debug)
            else:
                winner = my > their
            if debug:
                print(f'Player {1 if winner else 2} wins round {game_round} '
                      f'of game {self.game_no}!\n')
            if winner:
                self.my_cards.extend([my, their])
            else:
                self.their_cards.extend([their, my])
            game_round += 1
        if debug:
            print('== Post-game results == ')
            print(f'Player 1\'s deck: {stringify(self.my_cards)}')
            print(f'Player 2\'s deck: {stringify(self.their_cards)}')

        return bool(self.my_cards)

    def score(self, winner):
        deck = self.my_cards if winner else self.their_cards
        return functools.reduce(lambda a, b: a + ((1 + b[0]) * b[1]),
                                enumerate(reversed(deck)),
                                0)


class Dec22(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 22, instructions, filename)
        self.my_cards, self.their_cards = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        g1, g2 = Day.parse_groups(instructions=instructions)
        return list(map(int, g1[1:])), list(map(int, g2[1:]))

    @timer(part=1)
    def part_1(self):
        c = Combat(self.my_cards, self.their_cards)
        winner = c.play()
        return c.score(winner)

    @timer(part=2)
    def part_2(self, debug=False):
        c = Combat(self.my_cards, self.their_cards, recursive=True)
        winner = c.play()
        return c.score(winner)


if __name__ == '__main__':
    with Timer():
        Dec22().run_day()
