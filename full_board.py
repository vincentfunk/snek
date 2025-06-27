from snek.snekgame import SnekGame
import sys

if len(sys.argv) == 2 or len(sys.argv) > 4:
    print("Usage: python full_board.py [height] [width] [timeout]")
    sys.exit()

if len(sys.argv) > 2:
    game = SnekGame(int(sys.argv[1]), int(sys.argv[2]))
else:
    game = SnekGame(10, 30)

if len(sys.argv) > 3:
    game.hit_map(int(sys.argv[3]))
else:
    game.hit_map()

