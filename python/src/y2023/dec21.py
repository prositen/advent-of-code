from python.src.common import Day, timer, Timer


class Farm(object):
    def __init__(self, farm_map):
        self.max_dim = len(farm_map)
        assert(self.max_dim == len(farm_map[0]))
        self.start = (0, 0)
        for y, row in enumerate(farm_map):
            if 'S' in row:
                self.start = (y, row.index('S'))

        self.tiles = {(y, x) for y, row in enumerate(farm_map)
                      for x, c in enumerate(row) if c in '.S'}
        self.count = {0: 1, -1: 0}
        self.visited = {self.start}
        self.next_step = {self.start}

    def move(self, max_steps):
        delta = (-1, 0), (1, 0), (0, -1), (0, 1)
        for step in range(max(self.count), max_steps):
            self.visited, self.next_step = self.next_step, {
                (ny, nx)
                for (y, x) in self.next_step
                for (dy, dx) in delta
                for (ny, nx) in ((y + dy, x + dx),)
                if
                (ny, nx) not in self.visited and (ny % self.max_dim, nx % self.max_dim) in self.tiles
            }
            self.count[step + 1] = len(self.next_step) + self.count[step - 1]

        return self.count[max_steps]

    def calculate(self, max_steps):
        d, m = divmod(max_steps, self.max_dim)

        x0 = m
        y0 = self.move(max_steps=x0)

        x1 = m + self.max_dim
        y1 = self.move(max_steps=x1)

        x2 = m + 2 * self.max_dim
        y2 = self.move(max_steps=x2)

        """
        Lagrange Interpolation formula for  ax^2 + bx + c:     
        
        
(x−x1)(x−x2)(x0−x1)(x0−x2)f0+(x−x0)(x−x2)(x1−x0)(x1−x2)f1+(x−x0)(x−x1)(x2−x0)(x2−x1)f2        
        
                     (x-x1)(x-x2)           
        f(x) =  y0 * -------------  + y1 * 
                    (x0-x1)(x0-x2)                                      2
               
       a = 
         
          ax^2 + bx + c with x=[0,1,2] and y=[y0,y1,y2] we have
 *   f(x) = (x^2-3x+2) * y0/2 - (x^2-2x)*y1 + (x^2-x) * y2/2
 * so the coefficients are:
 * a = y0/2 - y1 + y2/2
 * b = -3*y0/2 + 2*y1 - y2/2
 * c = y0
 */
const simplifiedLagrange = (values) => {
  return {
    a: values[0] / 2 - values[1] + values[2] / 2,
    b: -3 * (values[0] / 2) + 2 * values[1] - values[2] / 2,
    c: values[0],
  };
};
        
        """
        # print(a, b, c)


class Dec21(Day, year=2023, day=21):

    @timer(part=1)
    def part_1(self):
        return Farm(self.instructions).move(max_steps=64)

    @timer(part=2)
    def part_2(self):
        """
        628206330073385

        :return:
        """

        return Farm(self.instructions).calculate(max_steps=26501365)


if __name__ == '__main__':
    with Timer('Total'):
        Dec21().run_day()
