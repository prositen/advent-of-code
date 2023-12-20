import math

from python.src.common import Day, timer, Timer


class Module(object):
    def __init__(self, machines, name, targets):
        self.machines: Machines = machines
        self.name = name
        self.targets = targets
        self.signal = False
        self.senders = set()

    def add_sender(self, sender):
        self.senders.add(sender)

    def update(self, sender, signal):
        pass

    def enqueue(self):
        self.machines.enqueue(sender=self.name,
                              signal=self.signal,
                              targets=self.targets)

    @staticmethod
    def from_rule(machines, rule):
        name, targets = rule.split(' -> ')
        targets = [t.strip() for t in targets.split(',')]
        if name[0] == '%':
            return FlipFlop(machines, name[1:], targets)
        elif name[0] == '&':
            return Conjunction(machines, name[1:], targets)
        elif name == 'broadcaster':
            return Broadcast(machines, name, targets)

    def __repr__(self):
        return f'<Module {self.name}>'


class FlipFlop(Module):

    def update(self, sender, signal):
        if not signal:
            self.signal = not self.signal
            self.enqueue()

    def __repr__(self):
        return f'<FlipFlop {self.name} {",".join(self.targets)}>'


class Conjunction(Module):
    def __init__(self, name, targets, machines):
        super().__init__(name, targets, machines)
        self.signals = dict()

    def add_sender(self, sender):
        self.signals[sender] = False
        super().add_sender(sender)

    def update(self, sender, signal):
        self.signals[sender] = signal
        self.signal = any([not s for s in self.signals.values()])
        self.enqueue()

    def __repr__(self):
        return f'<Conjunction {self.name} {",".join(self.targets)}>'


class Broadcast(Module):

    def update(self, sender, signal):
        self.signal = signal
        self.enqueue()

    def __repr__(self):
        return f'<Broadcaster {",".join(self.targets)}>'


class Machines(object):

    def __init__(self, module_rules):
        self.modules: dict[str, Module] = {
            m.name: m for m in [Module.from_rule(self, r) for r in module_rules]
        }
        for module in list(self.modules.values()):
            for target in module.targets:
                if target not in self.modules:
                    self.modules[target] = Module(self, target, [])
                self.modules[target].add_sender(module.name)

        self.pulses = {False: 0, True: 0}
        self.queue = list()
        self.subscriptions = dict()
        self.button_presses = 0

    def enqueue(self, sender: str, signal: bool, targets: list[str]):
        self.queue.extend(
            [
                (sender, self.modules[t], signal) for t in targets
            ]
        )

    def run(self):
        self.button_presses += 1
        next_up = [('button', self.modules['broadcaster'], False)]
        while next_up:
            self.queue.clear()
            for sender, module, signal in next_up:
                if self.subscriptions.get((module.name, signal)) == -1:
                    self.subscriptions[(module.name, signal)] = self.button_presses
                    if not any(s == -1 for s in self.subscriptions.values()):
                        return False
                self.pulses[signal] += 1
                module.update(sender=sender, signal=signal)
            next_up = [c for c in self.queue]
        return True

    def count(self):
        return self.pulses[False] * self.pulses[True]

    def find_closest_multi_source_conjunction(self, module_name):
        module = self.modules[module_name]
        while not isinstance(module, Conjunction) and len(module.senders) == 1:
            module = self.modules[module.senders.pop()]
        return module

    def add_subscription(self, sender, signal):
        self.subscriptions[(sender, signal)] = -1

    def solve_for_rx(self):
        for sender in self.find_closest_multi_source_conjunction('rx').senders:
            self.add_subscription(sender, False)
        while self.run():
            pass

        return math.lcm(*self.subscriptions.values())


class Dec20(Day, year=2023, day=20):

    @timer(part=1)
    def part_1(self):
        m = Machines(self.instructions)
        for i in range(1000):
            m.run()

        return m.count()

    @timer(part=2)
    def part_2(self):
        return Machines(self.instructions).solve_for_rx()


if __name__ == '__main__':
    with Timer('Total'):
        Dec20().run_day()
