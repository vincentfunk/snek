import time
from snek.snekgame import SnekGame
from tkinter import Tk, Label

game = SnekGame(10, 20)
# game.speed_solve(y=4, x=4, display=True, delay=0)
# game.only_closest(display=True, delay=0.1)


root = Tk()
board = Label(root, text=str(game.field), font="TkFixedFont", background='black', foreground='white')
board.grid(column=0, row=0)
board.focus_set()

# board.configure(text=str(game.field))

root.mainloop()