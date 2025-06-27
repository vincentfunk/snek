import math


class Grid(list):
    def __init__(self, y=None, x=None, grid=None):
        super().__init__()
        self.adjacent = []
        if grid is None:
            for line in range(y):
                # self.append(['.' for pos in range(x)])
                self.append(['.'] * x)
        else:
            for line in grid:
                self.append([pos for pos in line])

    def display(self):
        """print self with borders"""
        print('+' + '-' * len(self[0]) + '+')
        for line in self:
            print('|', end="")
            for pos in line:
                print(pos, end="")
            print('|')
        print('+' + '-' * len(self[0]) + '+')

    def draw_line(self, direct, pos):
        """create line of 0s on grid"""
        if direct == 'up' or direct == 'down':
            for row in self:
                row[pos] = '0'
        elif direct == 'left' or direct == 'right':
            self[pos] = ['0'] * len(self[pos])  # for char in self[pos]]
        else:
            raise ValueError('incorrect direction')

    def first_instance(self, symbol):
        """get first location of symbol"""
        for y, line in enumerate(self):
            for x, pos in enumerate(line):
                if pos == symbol:
                    return y, x
        return None

    def all_adjacent(self, symbol):
        """check if all of a character are adjacent to each other"""
        first = self.first_instance(symbol)
        # if no instances of symbol found return True
        if first is None:
            return True
        # create adjacent list
        adj = self.auto_adjacent(first)
        # make sure all instances of symbol are in adjacent list
        for i, line in enumerate(self):
            for j, pos in enumerate(line):
                if pos == symbol and (i, j) not in adj:
                    return False
        return True

    # def add_adj(self, cords, adj_list=None):
    #     """returns list of all adjacent instances of same symbol to cords
    #     might be more resonable than add_adjecent but actually is slower soo"""
    #     if adj_list is None:
    #         adj_list = []
    #     if cords not in adj_list:
    #         adj_list.append(cords)
    #     new = [adj for adj in self.same_adjacent(cords) if adj not in adj_list]
    #     adj_list.extend(new)
    #     loc_list = [cords]
    #     for cords in new:
    #         loc_list += self.add_adj(cords, adj_list)
    #     return loc_list

    def auto_adjacent(self, tup):
        """handles the starting point for adjacents and
        returns the list separate from the instance variable"""
        self.adjacent = []
        self.adjacent.append(tup)
        self.add_adjacent(tup)
        return self.adjacent

    def add_adjacent(self, tup):
        """add all adjacent instances from cords tup to list
        uses instance variable that must be cleared externally"""
        new = [adj for adj in self.same_adjacent(tup) if adj not in self.adjacent]
        self.adjacent.extend(new)
        for cords in new:
            self.add_adjacent(cords)

    def same_adjacent(self, tup):
        """return all adjacents of the same character to tup"""
        y, x = tup
        above, below, left, right = None, None, None, None
        if y != 0:
            if self[y][x] == self[y - 1][x]:
                above = y - 1, x
        if y != len(self) - 1:
            if self[y][x] == self[y + 1][x]:
                below = y + 1, x
        if x != 0:
            if self[y][x] == self[y][x - 1]:
                left = y, x - 1
        if x != len(self[0]) - 1:
            if self[y][x] == self[y][x + 1]:
                right = y, x + 1
        return [direct for direct in [above, below, left, right] if direct is not None]

    def quad_mirror(self):
        """mirror top left quadrant to all 4 quadrants"""
        # left right mirror
        # only first half of rows
        for row in self[:math.ceil(len(self) / 2)]:
            # odd len rows
            if len(row) % 2:
                row[len(row) // 2:] = row[len(row) // 2::-1]
            # even len rows
            else:
                row[len(row) // 2:] = row[len(row) // 2 - 1::-1]
        # up down mirror
        for i, row in enumerate(self[:math.ceil(len(self) / 2)]):
            self[len(self) - 1 - i] = row
