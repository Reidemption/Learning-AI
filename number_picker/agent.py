import number
import random
import copy 
  
LIMIT = 10
class Agent:
  def __init__(self, seed, size):
    self.model = number.Environment(seed, size)
    
  # random action
  def decideAction(self, percepts):
    self.model.updatePercepts(percepts)
    actions = self.model.getLegalActions()
    action = random.choice(actions)
    return action
  
  def Top_Max(self, state):
    self.model.updatePercepts(state)
    limit=0
    if self.model.GoalTest():
      return None
    v = -99999999
    best_action = None
    for a in self.model.getLegalActions():
      model_copy=copy.deepcopy(self.model)
      model_copy.Result(state, a)
      new_v = self.Min(model_copy, v, limit)
      if new_v > v:
        v = new_v
        best_action = a
    return best_action
  
  def Max(self, state, greek, limit):
    if self.model.GoalTest() or limit == LIMIT:
      return self.model.Utility() #Am going to want this to return the score for stated player.
    alpha = -99999999
    limit += 1
    for action in self.model.getLegalActions():
      model_copy=copy.deepcopy(self.model)
      
      model_copy.Result(state, action)
      new_alpha = self.Min(model_copy, alpha, limit)
      if new_alpha > alpha:
        alpha = new_alpha
      if alpha > greek:
        return alpha
      
    return alpha
          
  def Min(self, state, greek, limit):
    if self.model.GoalTest() or limit == LIMIT:
      return self.model.Utility() #Am going to want this to return the score for stated player.
    beta = 99999999
    limit += 1    
    for action in self.model.getLegalActions():
      model_copy = copy.deepcopy(state)
      model_copy.Result(state, action)
      new_beta = self.Max(model_copy, beta, limit)
      if new_beta < beta:
        beta = new_beta
      if beta < greek:
        return beta
    return beta
  
def main():
  seed = 1234567890
  env = number.Environment(seed, 100) # assumes environment is randomly populated among possible environments.
  agent = Agent(seed, 100) # assumes random agent class exists.
  agent2 = Agent(seed, 100) # multi agent environment
  while not env.done():
      # env.showState()
      players = [agent, agent2] # multi agent environment
      
      for i,player in enumerate(players):
        percepts = env.getPercepts()
        print('percepts:', percepts)
        if i == 0: #player1
          action = player.Top_Max(percepts)
          # action = player.decideAction(percepts)
        else: #player2  
          action = player.decideAction(percepts)
        print('action:', action)
        print('\n')
        env.applyAction(action, i+1)
        if env.GoalTest():
          # env.done = True
          break
      
  return


main()