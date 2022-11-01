import model
import random
import number

  
class Agent:
  def __init__(self):
    self.model = model.NumberPickerModel()
    
  # random action
  def decideAction(self, percepts):
    actions = self.model.getLegalActions(percepts)
    action = random.choice(actions)
    return action
  
  def alphaBetaSearch(self, depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    MIN, MAX = -10000000, 10000000
    # Terminating condition. i.e
    # leaf node is reached
    if depth == 3:
        return values[nodeIndex]
    if maximizingPlayer:
        best = MIN
        # Recur for left and right children
        for i in range(0, 2):
             
            val = self.alphaBetaSearch(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
 
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        # Recur for left and
        # right children
        for i in range(0, 2):
          
            val = self.alphaBetaSearch(depth + 1, nodeIndex * 2 + i,
                            True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best
  
def main():
  seed = 1234567890
  env = number.Environment(seed, 100) # assumes environment is randomly populated among possible environments.
  agent = Agent() # assumes random agent class exists.
  agent2 = Agent() # multi agent environment
  while not env.done():
      # env.showState()
      players = [agent, agent2] # multi agent environment
      print('while loopage')
      
      for i,player in enumerate(players):
        percepts = env.getPercepts()
        print('percepts:', percepts)
        action = player.decideAction(percepts)
        print('action:', action)
        env.applyAction(action, i+1)
        if env.GoalTest():
          # env.done = True
          break
      
  return


main()