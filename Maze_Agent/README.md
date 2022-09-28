# Maze AI

This enviorment creates a maze for an AI to navaigate through. The starting coordinates of the agent is (0,0)
There are walls inside of the maze that the agent can bump into. This enviorment uses a (X,Y) coordinate system. 

### Actions
- Left: This moves the agent on square to the left (X-1, Y)
- Right: This moves the agent to the right one square. (X+1,Y)
- Up: This moves the agent up one square. (X,Y+1)
- Down: This moves the agent down one square. (X,Y-1)

### 8x8 Repersentation
          X-Axis
     0 1 2 3 4 5 6 7    
   0 X O O W O O O O  
Y  1 O O O W O O O O  
   2 O W W W O O W W  
A  3 O O O W W O O O  
X  4 O O O O O O O O  
I  5 O W O W W O O O  
S  6 W W O O O O W W  
   7 O O O O O O O G

- W: Wall (these are calculated using the randomMaze function)
- X: Starting Location
- G: Goal 
- O: Open Space

### Datamembers (maze.py)
- mWidth: the desired width of the enviorment
- mHeight: the desired height of the enviorment
- mX_Location: the x location of the agent
- mY_Location: the y location of the agent
- mWalls: a list containing all of the coordinates of where the walls exist. 
- mMaze = a list containing locations for the start of the agent, goal and walls



### Maze Enviorment Methods (maze.py)
- __init__: initalizes the maze enviorment (height and width are parameters). Sets the AI in the top-left corner and initalizes the wall locations.  
- __boundary_check__: checks that the new x and y will not go off of the maze. If they do, then it returns false.
- __check_walls__: checks that the AI doesn't bump into any walls, if it does returns false.
- __left__: returns the value of the current position one square to the left. 
- __right__: returns the value of the current position one sqaure to the right.
- __up__: returns the value of the current position one square up.
- __down__: returns the value of the current position one square down.
- __createRandomMaze__: returns a randomly created maze (spots can either be open or wall, each has a 50% chance, or if a path exists, it leaves it open)
- __generatePath__: returns a randomly generated path, this guarantees an exit to the maze. 
- __displayPerformanceMeasure__: returns the performance measure for the agent. 
- __printMaze__: prints out what the maze looks like

### Model Class Methods (model.py)
- __GoalTest__: returns true/false based on the location of the agent. the goal is the right-bottom corner. (mWorldWidth -1, mWorldHeight -1)
- __Results__: this copys the current state and applies the action and then returns that state object.
- __Actions__: returns a list of possible actions.

### Agent Class Methods (agent.py)
- __init__: initalizes a model object by passing in a maze object.
- __agenetFunction__: takes in a set of coords, map, and bookeeping elements (steps and wall hits) to update the position of the agent, then returns the next action to take

### Main (agent.py)
creates enviorment and the agent, displays the perfomance measure, currently runs the random agent implementation 
