import copy
#this is a diagram of how the list for the state will be layed out. the numbers are the index into the list
#                                                                           PLAYER 2 SIDE
#                              ____________________________________________________________________________________________________________
#                             |       |            |             |              |               |                 |                |       |
#                             |       |     13     |      12     |      11      |      10       |         9       |       8        |       |
#                             |       |            |             |              |               |                 |                |       |          
#     HOME FOR PLAYER 2 ->    |   0   |------------|-------------|--------------|---------------|-----------------|----------------|  7    |      <- HOME FOR PLAYER 1 
#                             |       |            |             |              |               |                 |                |       |         
#                             |       |     1      |      2      |       3      |       4       |         5       |       6        |       |          
#                             |_______|____________|_____________|______________|_______________|_________________|________________|_______|
#                
#                                                                           PLAYER 1 SIDE 
class Model:
    def __init__(self):
        # Initalize the starting State/Environment
        self.mState = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]
        self.mDone = False
      
    # there are a total of 48 marbles so once there are only marbles in either home spot for the two players the game is over
    # goaltest() and isdone() do the same thing so to reduce code im just using goal test
    def GoalTest(self):
        game_done=False
        if self.mState[0] + self.mState[7] == 48:
            game_done=True
        return game_done

    # The only  thing that needs to get passed is the board itself so state is simply the board
    def updatePercepts(self, state):
        self.mState= copy.deepcopy(state)

    # apply actions is the same as results    
    # the action is a number (the index of the marble slot you want to pick up and distribute)
    def applyAction(self, action,player):
        #0 means the turn is over, 1 will mean that the person gets another turn
        returnValue = 0
        if action != None:
            
            marbles=self.mState[action]
            self.mState[action]=0
            index=action+1
            turnOver=False

            #if player equals 2 that means this is the second player making the actions and we wont want to put marbles in player 1's home. vise versa for player 1
            enemyHome=0
            if player == 2:
                enemyHome = 7
            
            while not turnOver:
                for marble in range(marbles):
                    if index == 14:
                        index=0
                    if index == enemyHome:
                        index += 1
                    self.mState[index] += 1
                    index+=1
                if index == 0:
                    if self.mState[13] > 1:
                        marbles=self.mState[13]
                        self.mState[13] = 0
                    else:
                        turnOver = True

                elif index == 1 and player == 2:
                    returnValue=1
                    turnOver = True

                elif index == 1 :
                    if self.mState[13] > 1:
                        marbles=self.mState[13]
                        self.mState[13] = 0
                    else:
                        turnOver = True
                elif index == 8 and player == 1:
                    returnValue=1
                    turnOver = True

                elif index == 8:
                    if self.mState[6] > 1:
                        marbles=self.mState[6]
                        self.mState[6] = 0
                    else:
                        turnOver = True
                
                elif self.mState[index-1] > 1:
                    marbles=self.mState[index-1]
                    self.mState[index-1] = 0
                else:
                    turnOver = True
        return returnValue
       
    def getObservable(self):
        return self.mState

    # the variable player will be simply a number, 1 or 2, depending on which player you are
    def getLegalActions(self,player):
        validActions=[]
        #you will return all indexes that have at least 1 marble
        if player == 1:
            if self.mState[1] > 0 :
                validActions.append(1)
            if self.mState[2] > 0 :
                validActions.append(2)
            if self.mState[3] > 0 :
                validActions.append(3)
            if self.mState[4] > 0 :
                validActions.append(4)
            if self.mState[5] > 0 :
                validActions.append(5)
            if self.mState[6] > 0 :
                validActions.append(6)
        else:
            if self.mState[8] > 0 :
                validActions.append(8)
            if self.mState[9] > 0 :
                validActions.append(9)
            if self.mState[10] > 0 :
                validActions.append(10)
            if self.mState[11] > 0 :
                validActions.append(11)
            if self.mState[12] > 0 :
                validActions.append(12)
            if self.mState[13] > 0 :
                validActions.append(13)

        return validActions

    def printBoard(self):
        print()
        print("    ", end="")
        print(self.mState[13], end=" ")
        print(self.mState[12], end=" ")
        print(self.mState[11], end=" ")
        print(self.mState[10], end=" ")
        print(self.mState[9], end=" ")
        print(self.mState[8])
        print(f"{self.mState[0]}               {self.mState[7]}")
        print("    ", end="")
        print(self.mState[1], end=" ")
        print(self.mState[2], end=" ")
        print(self.mState[3], end=" ")
        print(self.mState[4], end=" ")
        print(self.mState[5], end=" ")
        print(self.mState[6])
        
        print()
    def evaluate(self,player):
        score=0
        if player == 1 :
           score = self.mState[7] - self.mState[0]
        else:
            score = self.mState[0] - self.mState[7]
            
        return score