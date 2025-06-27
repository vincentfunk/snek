class Snek:
    def __init__(self, y, x):
        self.x = x
        self.y = y

    def up(self):
        self.y -= 1

    def dow(self):
        self.y += 1

    def rig(self):
        self.x += 1

    def lef(self):
        self.x -= 1
