class Recipient:
    def get(self, value):
        pass


class Bin(Recipient):
    def __init__(self, number):
        self.number = number
        self.value = 0

    def give(self, recipient):
        pass


class Bot(Recipient):
    def __init__(self, number):
        self.number = number
        self.high = 0
        self.low = 0

    def give(self, high, low):
        pass


class Factory:
    def __init__(self, instructions):
        self.output = dict()
        self.input = dict()
        self.parse(instructions)

    def parse(self, instructions):
        pass
