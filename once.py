import sys
import threading
import time
from snek.snekgame import SnekGame
from tkinter import Tk, Label

if len(sys.argv) in [0, 1, 3, 5] or len(sys.argv) > 6:
    print("Usage: python once.py [step_time:float] [height:int] [width:int] [snek_start_y:int] [snek_start_x:int]")
    sys.exit()

try:
    if len(sys.argv) == 6:
        game = SnekGame(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
    elif len(sys.argv) == 4:
        game = SnekGame(int(sys.argv[2]), int(sys.argv[3]))
    else:
        game = SnekGame(10, 20)
except ValueError:
    print("Usage: python once.py [step_time:float] [height:int] [width:int] [snek_start_y:int] [snek_start_x:int]")
    sys.exit()

root = Tk()
board = Label(root, text=str(game.field), font="TkFixedFont", background='black', foreground='white')
board.grid(column=0, row=0)
board.focus_set()


# Generate timer events from a separate thread
def timer():
    while True:
        time.sleep(float(sys.argv[1]))
        board.event_generate('<<Timer>>')


timer_thread = threading.Thread(target=timer)


# Run the actual snekgame in a separate thread and start right after tkinter board is displayed
def act_game():
    game.speed_solve(game.snek.y, game.snek.x, display=False, delay=float(sys.argv[1]))


def start():
    game_thread.start()


root.after(1, start)
game_thread = threading.Thread(target=act_game)


def update(event):
    board.configure(text=str(game.field))


# Start timer and tkinter display
board.bind('<<Timer>>', update)
timer_thread.start()
root.mainloop()

