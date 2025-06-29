# snek
snake pathing simulator

## Usage
### Full Board
Run a simulation of every starting point on a board to produce a map of points that could be completed successfully in the given time per point  
`python full_board.py [timeout:int:default-5] [height:int:default-10] [width:int:default-20]`

-`height` and `width` must be included together  

### One Game
Watch one round play in slow steps to visually watch the snek attempt to fill the board  
`python once.py [step_time:float:default-0.1] [height:int:default-10] [width:int:default-20] [snek_start_y:int:default-random] [snek_start_x:int:default-random]`

-requires tkinter  
-`height` and `width` must be included together  
-`snek_start_y` and `snek_start_x` must be included together

## Detailed Description
Board simulates a snake attempting to completely fill each tile and reports if it was successful in the given timeout on a per start location basis

Snake follows simple rules to move

-always go to the closest wall or filled in tile  
-unless it would split the open space into two separate areas which would make the route a fail  
-when the snake is finished if the board is not complete it will recursively rewind and try the next best direction for the last movement
