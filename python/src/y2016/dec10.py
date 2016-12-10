import re
from collections import deque


class Recipient:
    def __init__(self, number):
        self.number = number
        self.value = None

    def get(self, value):
        pass

    def can_get(self):
        return False


class Bin(Recipient):
    def get(self, value):
        if self.can_get():
            self.value = value

    def can_get(self):
        return self.value is None

    def __repr__(self):
        return "<Bin id={0} value={1}>".format(self.number, self.value)


class Bot(Recipient):
    def __init__(self, number):
        super().__init__(number)
        self.value = []

    def get(self, value):
        if self.can_get():
            self.value.append(value)
            self.value.sort()

    def give(self, low, high):
        if len(self.value) == 2:
            if high.can_get() and low.can_get():
                high.get(self.value[1])
                low.get(self.value[0])
                return True
        return False

    def can_get(self):
        return len(self.value) < 2

    def __repr__(self):
        return "<Bot id={0} value={1}>".format(self.number, self.value)


class Instruction:
    def run(self, context):
        pass


class AssignToBot(Instruction):
    def __init__(self, bot, value):
        self.bot = bot
        self.value = value

    def run(self, context):
        bot = context.get_or_create_bot(self.bot)
        if bot.can_get():
            bot.get(self.value)
            return True
        return False

    def __repr__(self):
        return "<Assign {0} to bot {1}>".format(self.value, self.bot)


class Give(Instruction):
    def __init__(self, bot, low_type, low_id, high_type, high_id):
        self.bot = bot
        self.low_type = low_type
        self.low_id = low_id
        self.high_type = high_type
        self.high_id = high_id

    def run(self, context):
        bot = context.get_or_create_bot(self.bot)
        if self.low_type == 'output':
            to_low = context.get_or_create_output(self.low_id)
        else:
            to_low = context.get_or_create_bot(self.low_id)
        if self.high_type == 'output':
            to_high = context.get_or_create_output(self.high_id)
        else:
            to_high = context.get_or_create_bot(self.high_id)
        return bot.give(to_low, to_high)

    def __repr__(self):
        return "<Give low to {0} {1}, high to {2} {3} from bot {4}>".format(self.low_type, self.low_id, self.high_type,
                                                                            self.high_id, self.bot)


class Factory:
    re_VALUE_TO_BOT = re.compile(r"value (\d+) goes to bot (\d+)")
    re_BOT_GIVES = re.compile(r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)")

    def __init__(self, instructions):
        self.output = dict()
        self.bots = dict()
        self.instructions = deque()
        self.parse(instructions)

    def parse(self, instructions):
        for instruction in instructions:
            result = self.re_VALUE_TO_BOT.match(instruction)
            if result:
                self.instructions.append(AssignToBot(int(result.group(2)), int(result.group(1))))
                continue

            result = self.re_BOT_GIVES.match(instruction)
            if result:
                bot = int(result.group(1))
                low_type = result.group(2)
                low_id = int(result.group(3))
                high_type = result.group(4)
                high_id = int(result.group(5))
                self.instructions.append(Give(bot, low_type, low_id, high_type, high_id))
                continue

    def get_or_create_bot(self, bot):
        if bot not in self.bots:
            self.bots[bot] = Bot(bot)
        return self.bots[bot]

    def get_or_create_output(self, output) -> Bin:
        if output not in self.output:
            self.output[output] = Bin(output)
        return self.output[output]

    def run(self):
        while self.instructions:
            instruction = self.instructions.popleft()
            if not instruction.run(self):
                self.instructions.append(instruction)
            # self.dump()

    def get_output(self, bin_id):
        return self.get_or_create_output(bin_id).value

    def get_bot_responsibility(self, bot_id):
        bot = self.get_or_create_bot(bot_id)
        return bot.value

    def dump(self):
        print("---")
        print("Bots:", ", ".join(repr(x) for x in self.bots.values()))
        print("Bins:", ", ".join(repr(x) for x in self.output.values()))
        print("Instructions:", "," .join(repr(x) for x in self.instructions))
        print("---")


if __name__ == '__main__':
    with open('../../../data/2016/input.10.txt', 'r') as fh:
        instr = fh.readlines()
    factory = Factory(instr)
    factory.run()

    f = filter(lambda x: x.value == [17, 61], factory.bots.values())
    print("The bot responsible for comparing value-17 chips with value-61 chips is", "".join(repr(x) for x in f))
    bin_values = factory.get_output(0) * factory.get_output(1) * factory.get_output(2)
    print("The values in outputs 0, 1, 2 multiplied is", bin_values)