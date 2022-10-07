import random
from copy import deepcopy

class BubbleModel:
    
    def __init__(self, seed, numSBubbles, numPBubbles, numCols):
        if seed != None:
            random.seed(seed)
        self.sBubbles = []
        self.pBubbles = []
        if numCols != None:
            self.numCols = numCols
        if numSBubbles != None and numPBubbles != None:
            for i in range (numSBubbles):
                color = random.randint(1,3)
                self.sBubbles.append(color)
            self.numRows = (numPBubbles // self.numCols) + 1
            rows = numPBubbles // self.numCols
            row = []
            for i in range (rows):
                for j in range (self.numCols):
                    row.append(random.randint(1,3))
                self.pBubbles.append(row)
                row = []
            bottomRow = []
            for i in range(self.numCols):
                bottomRow.append(0)
            self.pBubbles.append(bottomRow)
    
    def printBoard(self):
        i=0
        for row in self.pBubbles:
            print(f"{i}",row)
            i += 1
    
    def printBubbles(self):
        print(self.sBubbles)

    def printState(self):
        self.printBoard()
        self.printBubbles()
        print("")
        
    def getPBubble(self, pos):
        return self.pBubbles[pos[0]][pos[1]]

    def checkThenPop(self, pos, color):
        checks = [True, True, True]
        if (pos[0] - 1 >= 0): 
            if self.pBubbles[pos[0]-1][pos[1]] == color:
                checks[0] = False
        if (pos[1] - 1 >= 0):
            if self.pBubbles[pos[0]][pos[1]-1] == color:
                checks[1] = False
        if (pos[1] + 1 < self.numCols):
            if self.pBubbles[pos[0]][pos[1]+1] == color:
                checks[2] = False
        if checks == [True, True, True]:
            self.pBubbles[pos[0]][pos[1]] = color
        else:
            self.popBubbles(pos, color)
    
    def popBubbles(self, pos, color): 
        if (pos[0] - 1 >= 0) and self.pBubbles[pos[0]-1][pos[1]] == color: #check bubble right above
            self.pBubbles[pos[0]-1][pos[1]] = 0
            self.popBubbles((pos[0]-1,pos[1]),color)
        if (pos[1] - 1 >= 0) and self.pBubbles[pos[0]][pos[1]-1] == color: #check bubble to the left
            self.pBubbles[pos[0]][pos[1]-1] = 0
            self.popBubbles((pos[0],pos[1]-1),color)
        if (pos[1] + 1 < self.numCols) and self.pBubbles[pos[0]][pos[1]+1] == color: #check bubble to the right
            self.pBubbles[pos[0]][pos[1]+1] = 0
            self.popBubbles((pos[0],pos[1]+1),color)

    def swapBubbles(self):
        fBubble = self.sBubbles[0]
        if len(self.sBubbles) > 1:
            self.sBubbles[0] = self.sBubbles[1]
            self.sBubbles[1] = fBubble

    def dumpBubble(self):
        self.sBubbles = self.sBubbles[1:]

    def shootBubble(self, pos):
        if len(self.sBubbles) == 0:
            return
        self.checkThenPop(pos,self.sBubbles[0])
        self.dumpBubble()

    def getShootPositions(self): 
        positions = []
        for i in range(self.numRows):
            for j in range(self.numCols):
                checks = [False, False, False, False, False]
                #check current position
                if self.pBubbles[i][j] == 0:
                    checks[0] = True
                #check above position
                if (i - 1 >= 0) and self.pBubbles[i-1][j] != 0: 
                    checks[1] = True
                #check left position
                if (j - 1 >= 0) and self.pBubbles[i][j-1] != 0:
                    checks[2] = True
                #check right position
                if (j + 1 < self.numCols) and self.pBubbles[i][j+1] != 0:
                    checks[3] = True
                #check bottom position
                if (i + 1 < self.numRows) and self.pBubbles[i+1][j] == 0:
                    checks[4] = True
                if i == self.numRows-1:
                    checks[4] = True

                if checks[0] and checks[4] and (checks[1] or checks[2] or checks[3]):
                        positions.append((i,j))
        return positions

    def getObservablePercepts(self):
        return [self.sBubbles,self.pBubbles]

    def updateFromPercepts(self,percepts):
        self.sBubbles = percepts[0]
        self.pBubbles = percepts[1]
        self.numCols = len(self.pBubbles[0])
        numPBubbles = len(self.pBubbles[0]) * len(self.pBubbles)
        self.numRows = numPBubbles // self.numCols

    def actions(self):
        pActions = []
        if len(self.sBubbles) != 0:
            pShots = self.getShootPositions()
            for shot in pShots:
                pActions.append(("shoot",shot))
        # if len(self.sBubbles) >= 2:
        #     pActions.append(("swap",None))
        # if len(self.sBubbles) > 0:
        #     pActions.append(("dump",None))
        return pActions

    def goalTest(self, score=-900):
        if score <= self.performanceMeasure():
            return True
        if len(self.sBubbles) == 0:
            return True
        for row in self.pBubbles:
            for bubble in row:
                if bubble == 0:
                    continue
                else:
                    return False
        return True

    def done(self):
        if self.goalTest() or self.sBubbles == []:
            return True
        else:
            return False

    def result(self, action):
        bubbleModelCopy = deepcopy(self)
        if action[0] == "swap":
            bubbleModelCopy.swapBubbles()
        elif action[0] == "dump":
            bubbleModelCopy.dumpBubble()
        elif action[0] == "shoot":
            bubbleModelCopy.shootBubble(action[1])
        return bubbleModelCopy

    def applyAction(self, action):
        if action[0] == "swap":
            self.swapBubbles()
        elif action[0] == "dump":
            self.dumpBubble()
        elif action[0] == "shoot":
            self.shootBubble(action[1])
            
    def performanceMeasure(self):
        shotsLeft = len(self.sBubbles)
        bubblesLeft = 0
        for i in range(self.numRows):
            for j in range(self.numCols):
                if self.pBubbles[i][j] != 0:
                    bubblesLeft += 1
        return shotsLeft * 20 + bubblesLeft * -50

# Things to Add
    # Floating bubbles are dropped from board
