# snek
snake pathing simulator


### Usage
"python full_board.py [height] [width] [timeout]"

defaults to: height-10 width-30 timeout-5  
options must be integers  
both or neither "height" and "width" must be included


### Detailed Description
Board simulates a snake attempting to completely fill each tile and reports if it was successful in the given timeout on a per start location basis

Snake follows simple rules to move

-always go to the closest wall or filled in tile  
-unless it would split the open space into two separate areas which would make the route a fail  
-when the snake is finished if the board is not complete it will recursively rewind and try the next best direction for the last movement
