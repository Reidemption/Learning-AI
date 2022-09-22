import model
import random

class Environment: 
  def __init__(self) -> None:
    self.moves = 0
    self.max_moves = 5 #picked an arbitrary number here.
  
  def done(self):
    if self.moves > self.max_moves:
      self.moves = 0
      return True
    return False
  
  
class Agent:
  def __init__(self):
    self.model = model.Model()
    
  def agentFunction(self, percepts):
    self.model.updateFromPercepts(percepts)
    actions = self.model.getActions()
    action = random.choice(actions)
    return action
  
def main():
  env = Environment() # assumes environment is randomly populated among possible environments.
  agent = Agent() # assumes random agent class exists.
  agent2 = Agent() # multi agent environment
  while not env.done():
      #env.showState()
      percepts = env.getObservablePercepts()
      action = agent.agentFunction(percepts)
      #print(action)
      env.applyAction(action)
      
      #percepts = env.getObservablePercepts()
      #action2 = agent2.agentFunction(percepts)
      #env.applyAction(action2)
      
      env.timeStepUpdate()
  displayPerformanceMeasure(env, agent)
  #displayPerformanceMeasure(env, agent2)

  return


main()