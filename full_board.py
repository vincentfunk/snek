from snek.snekgame import SnekGame
import sys

if len(sys.argv) == 3 or len(sys.argv) > 4:
    print("Usage: python full_board.py [height] [width] [timeout]")
    sys.exit()

if len(sys.argv) == 4:
    game = SnekGame(int(sys.argv[2]), int(sys.argv[3]))
else:
    game = SnekGame(10, 20)

if len(sys.argv) == 2:
    game.hit_map(int(sys.argv[1]))
else:
    game.hit_map(5)
