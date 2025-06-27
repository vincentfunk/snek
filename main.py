from snek.snekgame import SnekGame

game = SnekGame(10, 30)
game.hit_map(timeout=1)


# grid = Grid(5, 5)
# grid.draw_line("left", 1)
# grid.display()
# print(grid.all_adjacent('.'))

# start = time.time()

# # print(game.open_space(['0', '.', '.', '@', '.']))
# # print(game.only_closest(display=True))
# # print(game.can_solve(time.time() + 20, display=True))

# # print(game.can_comp())
# # print(game.can_solve(timeout=time.time() + 100, display=True))
# # game.display()
# end = time.time()
# print("Time:", end - start)
