import math
import random
class Maze:
    
    def __init__(self, world_width, world_height):
        
        self.mWidth = world_width
        self.mHeight = world_height
        
        self.mX_Location = 0
        self.mY_Location = 0
        
        
        self.mMaze, self.mPath, self.mWalls = self.createRandomMaze(self.mWidth, self.mHeight)
        
        self.mWallHits = 0
        self.mSteps = 0
        
        
    def createRandomMaze(self,width, height):
        # Creates a random maze around the random generated path
        randomMap = ["O"] * (width * height)
        
        pathLength = (width*height)
        while pathLength > ((width*height)//3):
            path = self.generatePath(width, height)
            pathLength = len(path)
        
        walls = []
        choice = ["O", "W"]
        for x in range(width):
            for y in range(height):
               
                randomChoice = random.choice(choice)
                
                if (x,y) in path:
                    randomMap[y * width + x] = "O"
                
                elif randomChoice == "W":
                    walls.append((x,y))
                    randomMap[y * width + x] = "W"
                         
                else:
                    randomMap[y * width + x] = "O"
                                        
        randomMap[-1] = "G"
        randomMap[0] = "X"   
        
        
        return randomMap, path, walls
        
    def generatePath(self,width, height):
        # creates a guaranteed exit to the maze
        
        x_location = 0
        y_location = 0
        
        
        Goal = ((width -1) , (height -1))
        
        x_step_limit = width // 2
        y_step_limit = height // 2
            
        prev_choice = ""
        directions = ["L", "R", "D", "U"]
        up_and_down = ["U", "D"]
        right_and_left = ["L", "R"]
        path = []
        
        while (x_location,y_location) != Goal:
            
            if prev_choice == "":
                choice = random.choice(directions)
            elif prev_choice == "L":
                choice = random.choice(up_and_down)
            elif prev_choice == "R":
                choice = random.choice(up_and_down)
            elif prev_choice == "D":
                choice = random.choice(right_and_left)
            else:
                choice = random.choice(right_and_left)
        
                
                
            if choice == "U":
                prev_choice = "U"
                steps = random.randint(1,y_step_limit)
                for i in range(1,steps+1):
                    y_location = y_location + 1
                    
                    
                    if y_location >= height:
                        y_location  = height - 1
                        
                    path.append((x_location, y_location))
                
            elif choice == "D":
                prev_choice = "D"
                steps = random.randint(1,y_step_limit)
                for i in range(1, steps+1):
                    y_location = y_location - 1
                    
                    if y_location < 0:
                        y_location = 0
                        
                    path.append((x_location, y_location))
                
            elif choice == "R":
                prev_choice = "R"
                steps = random.randint(1,x_step_limit)
                for i in range(1, steps+1):
                    x_location = x_location + 1
                    
                    
                    if x_location >= width:
                        x_location = width - 1
                        
                    path.append((x_location, y_location))
                
            else:
                prev_choice = "L"
                steps = random.randint(1,x_step_limit)
                for i in range(1, steps+1):
                    x_location = x_location - 1
                    
                    
                    if x_location < 0:
                        x_location = 0
                        
                    path.append((x_location, y_location))
                    
        path = list(dict.fromkeys(path))
        
            
            
        return path
    
    def printMaze(self):
        for x in range(self.mWidth):
            print("\n")
            for y in range(self.mHeight):
                print(self.mMaze[y * self.mWidth + x], end=" ")
                # print(self.mMaze[y * self.mWidth + x], end=" ")
                
        print("\n")
        

        
    def boundary_check(self, new_x, new_y):
        if new_x < 0 or new_x >= self.mWidth:
            
            return False
        
        if new_y < 0 or new_y >= self.mHeight:
            return False
        
        return True
    
        
    def check_walls(self, new_x, new_y):
        coords = (new_x, new_y)
        
        
        for i in range(0, len(self.mWalls)):
            if coords == self.mWalls[i]:
                self.mWallHits = self.mWallHits + 1
                return False
            
        return True
    
    def left(self):
        # Each movement needs to check if its a valid move
        
        self.mSteps = self.mSteps + 1
        
        
        new_x = self.mX_Location - 1
        
        if self.boundary_check(new_x, self.mY_Location) == False:
            new_x = self.mX_Location
        if self.check_walls(new_x, self.mY_Location) == False:
            new_x = self.mX_Location
        
        self.mX_Location = new_x
        
        
    
    def right(self):
        # Each movement needs to check if its a valid move
        self.mSteps = self.mSteps + 1
        
        new_x = self.mX_Location + 1
        
        if self.boundary_check(new_x, self.mY_Location) == False:
            new_x = self.mX_Location
        
        if self.check_walls(new_x, self.mY_Location) == False:
            new_x = self.mX_Location
        
        self.mX_Location = new_x

    def up(self):
        # Each movement needs to check if its a valid move
        self.mSteps = self.mSteps + 1
        
        new_y = self.mY_Location - 1
        
        if self.boundary_check(self.mX_Location, new_y) == False:
            new_y = self.mY_Location
        
        if self.check_walls(self.mX_Location, new_y) == False:
            new_y = self.mY_Location
        
        self.mY_Location = new_y
           
        
    def down(self):
        # Each movement needs to check if its a valid move
        
        self.mSteps = self.mSteps + 1
        
        new_y = self.mY_Location + 1
        
        if self.boundary_check(self.mX_Location, new_y) == False:
            new_y = self.mY_Location
        
        if self.check_walls(self.mX_Location, new_y) == False:
            new_y = self.mY_Location
         
        self.mY_Location = new_y
        
    def validMoves(self):
        actions = []
        if self.up():
            actions.append("U")
        if self.down():
            actions.append("D")
        if self.left():
            actions.append("L")
        if self.right():
            actions.append("R")
        return actions
        
    def displayPerformanceMeasure(self, agent, goal):
     
        wall_hits = agent.mWallHits
        x_location = agent.mX_Location
        y_location = agent.mY_Location
        
        final_x = self.mWidth - 1
        final_y = self.mHeight - 1
        
        
            
        steps = agent.mSteps
        distance = math.sqrt(((agent.mX_Location - final_x) ** 2) + ((agent.mY_Location - final_y)**2))
        
        final_score = (steps * -1) + (wall_hits * -2) + (distance * - 1.5) // (self.mWidth * self.mHeight)  # divided by the size in order to compare maze size 
        if goal == True:
            final_score += (10 * self.mWidth) # depending on maze size, the bonus scales.
            print("The Agent made it to the goal")
        print("The Agent hit %2d walls" % (wall_hits))
        print(final_score)
   
        
        
            
  
    
    

        
    
