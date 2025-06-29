import random
import time
import math
from snek.snek import Snek
from snek.grid import Grid
from snek.loadingbar import LoadingBar


class SnekGame:
    def __init__(self, y, x, snek_y=None, snek_x=None):
        self.field = Grid(y, x)
        self.snek = None
        if snek_x is None or snek_y is None:
            self.random_snek()
        else:
            self.custom_snek(snek_y, snek_x)

    def random_snek(self):
        self.snek = Snek(random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1))
        self.field[self.snek.y][self.snek.x] = '@'

    def custom_snek(self, y, x):
        self.snek = Snek(y, x)
        self.field[self.snek.y][self.snek.x] = '@'

    def move_snek(self, direct):
        """move snek in direction"""
        self.field[self.snek.y][self.snek.x] = '0'
        if direct == "up":
            self.snek.up()
        elif direct == "down":
            self.snek.dow()
        elif direct == "left":
            self.snek.lef()
        elif direct == "right":
            self.snek.rig()
        self.field[self.snek.y][self.snek.x] = '@'

    def reverse_snek(self, direct):
        """move snek in opposite of direction"""
        self.field[self.snek.y][self.snek.x] = '.'
        if direct == "up":
            self.snek.dow()
        elif direct == "down":
            self.snek.up()
        elif direct == "left":
            self.snek.rig()
        elif direct == "right":
            self.snek.lef()
        self.field[self.snek.y][self.snek.x] = '@'

    def is_finished(self):
        """check if map is completed successfully"""
        for line in self.field:
            if '.' in line:
                return False
        return True

    @staticmethod
    def timer(func):
        """wrapper to print execution time"""
        def wrap(*args, **kwargs):
            begin = time.time()
            thefunc = func(*args, **kwargs)
            print("Execution Time:", time.time() - begin)
            return thefunc
        return wrap

    @timer
    def hit_map(self, timeout=5):
        """generate and display map of successful completions on the current grid"""
        hit_map = Grid(len(self.field), len(self.field[0]))
        quad_amount = math.ceil(len(self.field) / 2) * math.ceil(len(self.field[0]) / 2)
        long = []
        bar = LoadingBar(quad_amount)
        bar.start()
        for j, line in enumerate(hit_map[:math.ceil(len(self.field) / 2)]):
            for k, pos in enumerate(line[:math.ceil(len(line) / 2)]):
                finishby = time.time() + timeout
                result = self.speed_solve(j, k, finishby)
                if time.time() > finishby - (timeout / 4):
                    long.append((j, k))
                if result:
                    hit_map[j][k] = 'X'
                bar.progress()
        hit_map.quad_mirror()
        # check number of success and fails
        success, fail = 0, 0
        total = len(hit_map) * len(hit_map[0])
        for line in hit_map:
            for char in line:
                if char == '.':
                    fail += 1
        success = total - fail
        # display results and stats
        hit_map.display()
        print("Success:", success, "Fail:", fail)
        print("Success Ratio:", f"{success * 100 / total}%")
        print("Long Cords:", long)

    def open_space(self, line):
        """return amount of open space to the left of snek in a line, snek = @, open = ."""
        line = "".join(line)
        before = line.split('@')[0]
        for distance, char in enumerate(before[::-1] + '|'):
            if char != '.':
                return distance

    def closest_list(self):
        """return sorted list of directions based on closest open space"""
        row = self.field[self.snek.y]
        col = [row[self.snek.x] for row in self.field]
        directs = [
            (self.open_space(row), "left"),
            (self.open_space(row[::-1]), "right"),
            (self.open_space(col), "up"),
            (self.open_space(col[::-1]), "down")
        ]
        return sorted([data for data in directs if data[0] != 0], key=lambda x: x[0])

    def only_closest(self, display=False, delay=0):
        """attempt to solve by only moving to closest"""
        if display:
            self.field.display()
        time.sleep(delay)
        # calculate movement
        close = self.closest_list()
        # if no move check if complete
        if not close:
            return self.is_finished()
        # move in the closest direction
        self.move_snek(close[0][1])
        return self.only_closest(display, delay)

    def can_solve(self, timeout, display=False, delay=0):
        """attempt to solve trying all combinations that don't violate all adjacency"""
        # display, timeout, and adjacent checks
        if display:
            self.field.display()
        time.sleep(delay)
        if time.time() > timeout:
            return False
        if not self.field.all_adjacent('.'):
            return False
        # calculate movement
        close = self.closest_list()
        # if no move check if complete
        if not close:
            return self.is_finished()
        # attempt movement in each direction starting from closest
        for value, direction in close:
            self.move_snek(direction)
            works = self.can_solve(timeout, display, delay)
            if works:
                return True
            self.reverse_snek(direction)

        return False

    def speed_solve(self, y, x, timeout=None, display=False, delay=0):
        """combine both solving methods to only use recursive mode if basic closest fails
        also resets board to a new snek location"""
        if timeout is None:
            timeout = time.time() + 600
        self.__init__(len(self.field), len(self.field[0]), y, x)
        if self.only_closest(display, delay):
            return True
        else:
            self.__init__(len(self.field), len(self.field[0]), y, x)
            return self.can_solve(timeout, display, delay)
