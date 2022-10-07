from BubbleModel import BubbleModel
import random
from collections import deque
import copy


class RationalAgent:

    def __init__(self,seed,numPBubbles,numSBubbles,numCols):
        self.model = BubbleModel(seed,numPBubbles,numSBubbles,numCols)
    
    def agentFunction(self,percepts):
        self.model.updateFromPercepts(percepts)
        # create a stack
        frontier = deque()
        frontier.append((copy.deepcopy(self.model), None))
        while len(list(frontier)) > 0:
          state = frontier.pop()
          if state[0].goalTest():
            child_node = parent_node[0]
            parent_node = parent_node[1]
            while parent_node != None:
              child_node = parent_node[0]
              parent_node = parent_node[1]
            return self.bestMoveFromActions(state[1])
        
          # actions = self.model.actions()
          # print('ACTIONS',actions)
          for action in state[0].actions():
            print(state[0].actions())
            new_state = state[0].result(action)
            print('NS',new_state)
            frontier.append((new_state, state))
        # action = self.bestMoveFromActions(actions)
        # print('ACTION: ',action)
        # self.model.printState()
        # print('')
        # return action
      
    def bestMoveFromActions(self, actions):
      move = ''
      # actions will have my 'possible_moves' list
      # I need to check each action to see which will be the best.
      best_move_rating = 0
      for action in actions:
        if action[0] == 'shoot':
          score = self.nearMatches(action[1][0], action[1][1], self.model.sBubbles[0])
          if score > best_move_rating:
            best_move_rating = score
            move = action
      
      if best_move_rating == 0 or move == '':
        
        next_best = random.choice(actions)
        print('best move not found. choosing random action:', next_best)
        return next_best
      else:
        print('best move found:', move)
        return move
    
    def nearMatches(self, x, y, current_color):
      goodness = 0
      #check left of current location, if same color return true
      if x < 5 and x > 0 and y < 5:
        if self.model.pBubbles[x-1][y] == current_color:
          goodness += 1
        if self.model.pBubbles[x-1][y+1] == current_color:
          goodness += 1
        if y > 0:
          if self.model.pBubbles[x-1][y-1] == current_color:
            goodness += 1     
      return goodness 