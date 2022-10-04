
# MAZE AI -- Model Implementation
import copy
# model class takes in a state (the maze simulator/agent?) and sets the current state to it 
class Model:
    def __init__(self, state):
        # Initialize the starting State/Environment
        self.mState = state
        self.mGoal = False
      
    
    def GoalTest(self):
        # is the agent in the correct position
        
        coords = (self.mState.mX_Location, self.mState.mY_Location)
      
        if coords ==  (self.mState.mWidth-1, self.mState.mHeight-1):  # can change how big the maze is, the goal will be in the bottom-right corner
            return True
        
        return False

    def Result(self, action):
        state_copy = copy.copy(self)
        
        if action == "L":
            state_copy.mState.left()
        elif action == "R":
            state_copy.mState.right()
        elif action == "U":
            state_copy.mState.up() 
        else:
            state_copy.mState.down()
        
        return state_copy
    
    
    
    
    def updatePercepts(self, coords_wall_steps_map):
        
        self.mState.mX_Location, self.mState.mY_Location, self.mState.mWallHits, self.mState.mSteps, self.mMaze = coords_wall_steps_map
        

    def applyAction(self, action):
        
        # applies the desired action 
        
        # the maze simulation implements actions [L,R,U,D]
        
        if action == "L":
            self.mState.left()
        elif action == "R":
            self.mState.right()
        elif action == "U":
            self.mState.up() 
        else:
            self.mState.down()
    
    def getObservable(self):
        # returns the current position of the agent in the maze, maze map, wall hits and steps
        return self.mState.mX_Location, self.mState.mY_Location, self.mState.mWallHits, self.mState.mSteps, self.mState.mMaze
    
    def getLocation(self):
        return (self.mState.mX_Location, self.mState.mY_Location)
    
    def getLegalActions(self):
        return self.mState.validMoves()
    
    def done(self):
        if self.GoalTest() == True:
            self.mGoal = True
           
            return True
        elif self.mState.mSteps == (10 * (self.mState.mWidth * self.mState.mHeight)):   # depending on maze size the step count is scaled to match 
            return True
        else:
            return False
        
    


        
            

