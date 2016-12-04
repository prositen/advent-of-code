from collections import defaultdict
import copy

__author__ = 'Anna'

class Cell(object):

    def __init__(self, char):
        self.value = (char == '#')

    def __str__(self):
        return '#' if self.value else '.'

    def off(self):
        self.value = False

    def on(self):
        self.value = True

    def lit(self):
        return self.value

    def update(self, neighbours):
        if self.value and neighbours not in (2,3):
            self.off()
        elif not self.value and neighbours == 3:
            self.on()


class Grid(object):

    def __init__(self, from_char=None, from_cells=None):
        if from_char is not None:
            self.cells = dict()
            for y,line in enumerate(from_char):
                self.cells[y] = dict()
                for x, cell in enumerate(line):
                    self.cells[y][x] = Cell(cell)
        elif from_cells is not None:
            self.cells = from_cells
        else:
            raise ValueError("Missing argument from_char or from_cells to constructor")
        self.max_x = max(self.cells.keys())
        self.max_y = self.max_x

    def __str__(self):
        lines = list()
        for y in self.cells:
            line = list()
            for x in self.cells[y]:
                line.append(str(self.cells[y][x]))
            lines.append(''.join(line))
        return '\n'.join(lines)

    def neighbours(self, y, x):
        lit = 0
        for y_skip in -1, 0, 1:
            y_check = y + y_skip
            if y_check in self.cells:
                for x_skip in -1, 0, 1:
                    x_check = x + x_skip
                    if x_check in self.cells and not (x_skip == 0 and y_skip == 0):
                        lit += self.cells[y_check][x_check].lit()
        return lit

    def next(self):
        new_cells = copy.deepcopy(self.cells)
        for row in range(self.max_y + 1):
            for col in range(self.max_x + 1):
                lit = self.neighbours(row, col)
                new_cells[row][col].update(lit)

        return Grid(from_cells=new_cells)

    def count(self):
        count = 0
        for row in self.cells.values():
            for col in row.values():
                count += col.lit()
        return count


class CornerLitGrid(Grid):

    def __init__(self, from_char=None, from_cells=None):
        super(CornerLitGrid, self).__init__(from_char, from_cells)
        self.cells[0][0].on()
        self.cells[0][self.max_x].on()
        self.cells[self.max_y][0].on()
        self.cells[self.max_y][self.max_x].on()

    def next(self):
        grid = super(CornerLitGrid, self).next()
        return CornerLitGrid(from_cells=grid.cells)


def step(grid, steps):
    for step in range(steps):
        # print("Running step", step)
        grid = grid.next()
    #print(grid)
    return(grid)


def main():
    with open('../../../data/2015/input.18.txt', 'r') as fh:
        from_chars = fh.readlines()
        grid = Grid(from_char=from_chars)
        grid_100 = step(grid, 100)
        print("After 100 steps, the grid has", grid_100.count(), "lit lamps")
        corner_grid = CornerLitGrid(from_char=from_chars)
        corner_grid_100 = step(corner_grid, 100)
        print("After 100 steps, the broken grid has", corner_grid_100.count(), "lit lamps")
if __name__ == '__main__':
    main()