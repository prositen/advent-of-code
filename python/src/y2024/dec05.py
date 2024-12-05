from collections import defaultdict

from python.src.common import Day, timer, Timer


class Dec05(Day, year=2024, day=5, title='Print queue'):

    @staticmethod
    def parse_instructions(instructions):
        groups = Day.parse_groups(instructions)

        rules = defaultdict(set)
        for rule in Day.parse_multiple_ints_per_line(groups[0], separator=r'\|'):
            rules[rule[1]].add(rule[0])
        pages = Day.parse_multiple_ints_per_line(groups[1], separator=',')
        return rules, pages

    def page_order_is_valid(self, pages):
        return not any([
            set(pages[i + 1:]).intersection(self.instructions[0][page])
            for i, page in enumerate(pages)
        ])

    def reorder_pages(self, pages):
        # Sort pages by number of prerequisites
        page_requirements = sorted(
            {
                page: set(self.instructions[0][page]).intersection(pages)
                for page in pages
            }.items(),
            key=lambda c: len(c[1])
        )
        return list(p[0] for p in page_requirements)

    @timer(part=1)
    def part_1(self):
        return sum(
            pages[len(pages) // 2]
            if self.page_order_is_valid(pages) else 0
            for pages in self.instructions[1]
        )

    @timer(part=2)
    def part_2(self):
        page_sum = 0
        for pages in self.instructions[1]:
            if not self.page_order_is_valid(pages):
                pages = self.reorder_pages(pages)
                page_sum += pages[len(pages) // 2]
        return page_sum


if __name__ == '__main__':
    with Timer('Total'):
        Dec05().run_day()
