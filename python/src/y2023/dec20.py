import math

from python.src.common import Day, timer, Timer


class Module(object):
    def __init__(self, name: str, targets: tuple[str]):
        self.name = name
        self.targets = targets
        self.signal = False
        self.senders = set()

    def add_sender(self, sender: str):
        self.senders.add(sender)

    def update(self, sender, signal):
        return False

    @staticmethod
    def from_rule(rule):
        name, targets = rule.split(' -> ')
        targets = tuple(t.strip() for t in targets.split(','))
        if name[0] == '%':
            return FlipFlop(name[1:], targets)
        elif name[0] == '&':
            return Conjunction(name[1:], targets)
        elif name == 'broadcaster':
            return Broadcast(name, targets)

    def __repr__(self):
        return f'<Module {self.name}>'


class FlipFlop(Module):

    def update(self, sender, signal):
        if not signal:
            self.signal = not self.signal
            return True
        return False

    def __repr__(self):
        return f'<FlipFlop {self.name} {",".join(self.targets)}>'


class Conjunction(Module):
    def __init__(self, name, targets):
        super().__init__(name=name, targets=targets)
        self.signals = dict()

    def add_sender(self, sender):
        self.signals[sender] = False
        super().add_sender(sender)

    def update(self, sender, signal):
        self.signals[sender] = signal
        self.signal = any([not s for s in self.signals.values()])
        return True

    def __repr__(self):
        return f'<Conjunction {self.name} {",".join(self.targets)}>'


class Broadcast(Module):

    def update(self, sender, signal):
        self.signal = signal
        return True

    def __repr__(self):
        return f'<Broadcaster {",".join(self.targets)}>'


class Machines(object):

    def __init__(self, module_rules):
        self.modules: dict[str, Module] = {
            m.name: m for m in [Module.from_rule(r) for r in module_rules]
        }
        for module in list(self.modules.values()):
            for target in module.targets:
                if target not in self.modules:
                    self.modules[target] = Module(target, [])
                self.modules[target].add_sender(module.name)

        self.pulses = {False: 0, True: 0}
        self.subscriptions = set()
        self.sub_values = dict()
        self.button_presses = 0

    def run(self):
        self.button_presses += 1
        queue = [('button', 'broadcaster', False)]
        while queue:
            next_queue = list()
            for from_name, to_name, signal in queue:
                if (from_name, signal) in self.subscriptions:
                    if from_name in self.sub_values:
                        self.sub_values[from_name] += self.button_presses
                        self.subscriptions.discard((from_name, signal))
                        if not self.subscriptions:
                            return False
                    else:
                        self.sub_values[from_name] = -self.button_presses

                self.pulses[signal] += 1
                module = self.modules[to_name]
                if module.update(sender=from_name, signal=signal):
                    next_queue.extend(
                        [(to_name, t, module.signal) for t in module.targets]
                    )
            queue = next_queue
        return True

    def count(self):
        return self.pulses[False] * self.pulses[True]

    def find_closest_multi_source_conjunction(self, module_name):
        module = self.modules[module_name]
        while not isinstance(module, Conjunction) and len(module.senders) == 1:
            module = self.modules[module.senders.pop()]
        return module

    def solve_for_rx(self):
        """
        The machine grid ends with a Conjunction module with several inputs,
        sending it to the final module.

        In order to get a low pulse sent to 'rx', we need all inputs to this
        predecessor to be high.

        Let's keep track of when any of inputs are sent high, and do a LVM
        to find their common cycle.

        """
        module = self.find_closest_multi_source_conjunction('rx')
        for sender in module.senders:
            self.subscriptions.add((sender, True))
        while self.run():
            pass

        return math.lcm(*self.sub_values.values())


class Dec20(Day, year=2023, day=20):

    @timer(part=1, title='Low pulses * high pulses')
    def part_1(self):
        m = Machines(self.instructions)
        for i in range(1000):
            m.run()

        return m.count()

    @timer(part=2, title='Fewest number of button presses')
    def part_2(self):
        return Machines(self.instructions).solve_for_rx()


if __name__ == '__main__':
    with Timer('Total'):
        Dec20().run_day()
