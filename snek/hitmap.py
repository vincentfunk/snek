import time
import math
from snek.grid import Grid
from snek.loadingbar import LoadingBar
from snek.snekgame import SnekGame


class HitMap:
    def __init__(self, y=10, x=20):
        self.field = Grid(y, x)

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
        quad_amount = math.ceil(len(self.field) / 2) * math.ceil(len(self.field[0]) / 2)
        long = []
        bar = LoadingBar(quad_amount)
        bar.start()
        # Only run 1/4 of the games then mirror the results
        for j, line in enumerate(self.field[:math.ceil(len(self.field) / 2)]):
            for k, pos in enumerate(line[:math.ceil(len(line) / 2)]):
                finish_by = time.time() + timeout
                game = SnekGame(len(self.field), len(self.field[0]))
                result = game.speed_solve(j, k, finish_by)
                if time.time() > finish_by - (timeout / 4):
                    long.append((j, k))
                if result:
                    self.field[j][k] = 'X'
                bar.progress()
        self.field.quad_mirror()
        # check number of success and fails
        success, fail = 0, 0
        total = len(self.field) * len(self.field[0])
        for line in self.field:
            for char in line:
                if char == '.':
                    fail += 1
        success = total - fail
        # display results and stats
        self.field.display()
        print("Success:", success, "Fail:", fail)
        print("Success Ratio:", f"{success * 100 / total}%")
        print("Long Cords:", long)

