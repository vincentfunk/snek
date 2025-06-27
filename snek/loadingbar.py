class LoadingBar:
    def __init__(self, total):
        self.total = total
        self.finished = 0
        self.fin_ratio = 0

    def start(self):
        """display empty loading bar"""
        print('|', '-' * 100, '|', sep="", end="")

    def progress(self):
        """move loading bar forward"""
        self.finished += 1
        if self.finished > self.total:
            raise ValueError("Too much progress")
        self.fin_ratio = int((self.finished / self.total) * 100)
        print("\b" * 101, "#" * self.fin_ratio, "-" * (100 - self.fin_ratio), "|", sep="", end="")
        if self.finished == self.total:
            print()
