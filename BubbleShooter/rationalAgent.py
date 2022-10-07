from BubbleModel import BubbleModel
import random

class RationalAgent:

    def __init__(self,seed,numPBubbles,numSBubbles,numCols):
        self.model = BubbleModel(seed,numPBubbles,numSBubbles,numCols)
    
    def agentFunction(self,percepts):
        self.model.updateFromPercepts(percepts)
        actions = self.model.actions()
        print('ACTIONS',actions)
        action = self.bestMoveFromActions(actions)
        print('ACTION: ',action)
        self.model.printState()
        print('')
        return action
      
    def bestMoveFromActions(self, actions):
      best_move = None
      possible_moves = []
      next_move = self.model.sBubbles[0]
      for i in range(self.model.numRows):
        for j in range(self.model.numCols):
          if self.model.pBubbles[i][j] == 0: #starting this will be the bottom row. I will want to check the row above it to find if any are the same color, and if so, shoot that one.
            for k in range(i):
              if self.model.pBubbles[k][j] == next_move: #if the k is the same as the next bubble, shoot it
                if self.nearMatches(k,j, next_move):
                  best_move = ('shoot', (i,j))
                  if best_move not in possible_moves:
                    possible_moves.append(best_move)
          # best_move = ('shoot', (i,j))
      if best_move and best_move in actions:
        print(possible_moves)
        print('best move was calculated to be:', best_move)
        return random.choice(possible_moves) #return what could potentially be the best move
      next_best = random.choice(actions)
      print('best move not found. choosing random action:', next_best)
      return next_best
    
    def nearMatches(self, x, y, current_color):
      #check left of current location, if same color return true
      if self.model.pBubbles[x-1][y] == current_color:
        return True
      if self.model.pBubbles[x+1][y] == current_color:
        return True
      if self.model.pBubbles[x][y-1] == current_color:
        return True     
      return False 