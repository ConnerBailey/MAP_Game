import random
import time

class Map:
    def __init__(self, size, num_obstacles):
        self.size = size
        self.map = [['.' for _ in range(size)] for _ in range(size)]
        self.map[0][0] = 'R'  # Start point at (0, 0)
        self.map[size-1][size-1] = 'E'  # End point at the bottom right corner
        self.index = [0, 0]

        # Place obstacles randomly
        for _ in range(num_obstacles):
            x, y = random.randint(1, size-2), random.randint(1, size-2)
            self.map[x][y] = 'X'

    def check_on_object(self):
        if self.map[self.index[0]][self.index[1]] == 'X':
            raise Exception("You hit a rock!")
    
    def check_in_bounds(self):
        if self.index[0] < 0 or self.index[1] < 0:
            raise Exception("You hit a wall!")
        if self.index[0] == self.size or self.index[1] == self.size:
            raise Exception("You hit a wall!")

    def move_up(self):
        self.map[self.index[0]][self.index[1]] = '.'
        self.index[0] -= 1
        self.check_in_bounds()
        self.check_on_object()
        self.map[self.index[0]][self.index[1]] = 'R'

    def move_down(self):
        self.map[self.index[0]][self.index[1]] = '.'
        self.index[0] += 1
        self.check_in_bounds()
        self.check_on_object()
        self.map[self.index[0]][self.index[1]] = 'R'

    def move_left(self):
        self.map[self.index[0]][self.index[1]] = '.'
        self.index[1] -= 1
        self.check_in_bounds()
        self.check_on_object()
        self.map[self.index[0]][self.index[1]] = 'R'

    def move_right(self):
        self.map[self.index[0]][self.index[1]] = '.'
        self.index[1] += 1
        self.check_in_bounds()
        self.check_on_object()
        self.map[self.index[0]][self.index[1]] = 'R'

    def print_map(self):
        for row in self.map:
            print(' '.join(str(cell) for cell in row))

if __name__ == '__main__':
    board = Map(10,20)
    board.print_map()
    board.move_right()

    print("\n\n")

    board.print_map()

