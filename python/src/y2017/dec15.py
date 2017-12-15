from python.src.y2017.dec10 import KnotHash

class Generator(object):
    def __init__(self, factor, start_value, multiplier=1):
        self.factor = factor
        self.reminder = 2147483647
        self.value = start_value
        self.multiplier = multiplier

    def next_value(self):
        while True:
            self.value = (self.value * self.factor) % self.reminder
            if self.value % self.multiplier == 0:
                yield self.value & 0xFFFF

class Judge(object):

    def __init__(self, gen_A, gen_B):
        self.gen_A = gen_A
        self.gen_B = gen_B
        self.count = 0

    def run(self, steps):
        for x in range(steps):
            if next(self.gen_A.next_value()) == next(self.gen_B.next_value()):
                self.count += 1
        return self.count

def main():
    #a_start = 289
    #b_start = 629
    steps=40000000
    a_start = 65
    b_start = 8921
    # steps = 5000000


    A = Generator(16807, a_start, 1)
    B = Generator(48271, b_start, 1)

    j = Judge(A, B)
    j.debug = True
    j.run(steps)

    print(j.count)

if __name__ == '__main__':
    main()
