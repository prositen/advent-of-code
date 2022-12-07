from python.src.common import Day, timer, Timer


class Dec07(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2022, 7, instructions, filename)
        self.location = []
        self.fs = {
            '': {
                'files': list(),
                'size': 0
            }
        }
        self.build_file_system()

    @staticmethod
    def parse_instructions(instructions):
        return instructions

    def add_dir(self, sub_dir):
        self.fs['/'.join(self.location + [sub_dir])] = {
            'files': list(),
            'size': 0
        }

    def add_file(self, file_name, size):
        self.fs['/'.join(self.location)]['files'].append((file_name, size))
        self.fs['/'.join(self.location)]['size'] += size
        for i in range(len(self.location)):
            self.fs['/'.join(self.location[:i])]['size'] += size

    def build_file_system(self):
        for line in self.instructions:
            match line.split():
                case ['$', 'cd', '/']:
                    self.location = []
                case ['$', 'cd', '..']:
                    self.location.pop()
                case ['$', 'cd', sub_dir]:
                    self.location.append(sub_dir)
                case ['$', 'ls']:
                    pass
                case ['dir', sub_dir]:
                    self.add_dir(sub_dir)
                case [size, file_name]:
                    self.add_file(file_name, int(size))

    @timer(part=1)
    def part_1(self):
        return sum(subdir['size'] for subdir in self.fs.values() if subdir['size'] <= 100000)

    @timer(part=2)
    def part_2(self):
        needed_space = 30_000_000
        total_space = 70_000_000
        to_delete = needed_space - (total_space - self.fs['']['size'])
        return min(subdir['size'] for subdir in self.fs.values()
                   if subdir['size'] >= to_delete)


if __name__ == '__main__':
    with Timer('Total'):
        Dec07().run_day()
