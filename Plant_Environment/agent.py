import env
import random
import copy 
  
LIMIT = 10
class Agent:
  def __init__(self, seed):
    self.model = env.Plant(seed)
    
  # random action
  def decideAction(self, percepts):
    self.model.updatePercepts(percepts)
    actions = self.model.getLegalActions()
    action = random.choice(actions)
    return action
  
  #A* search algorithm
  
  
def main():
  seed = 1234567890
  environment = env.Plant(seed)
  agent = Agent(seed)
  
  while not environment.done():
    percepts = environment.getPercepts()
    print('percepts:', percepts)
    action = agent.decideAction(percepts)
    print('action:', action)
    print('\n')
    environment.applyAction(action)
  return


main()