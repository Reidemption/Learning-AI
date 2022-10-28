import model
import random
import game

  
class Agent:
  def __init__(self):
    self.model = model.Model()
    
  def decideAction(self, percepts):
    actions = self.model.Actions(percepts)
    action = random.choice(actions)
    return action
   
def main():
  env = game.Environment() # assumes environment is randomly populated among possible environments.
  agent = Agent() # assumes random agent class exists.
  agent2 = Agent() # multi agent environment
  while not env.done:
      # env.showState()
      percepts = env.getPercepts(0)
      action = agent.decideAction(percepts)
      print(action)
      #print(action)
      env.applyAction(0,action)
      env.battle()
      for player in env.players:
        env.generateUserShop(player)
      if env.GoalTest():
        env.done = True
      
      
      #percepts = env.getObservablePercepts()
      #action2 = agent2.agentFunction(percepts)
      #env.applyAction(action2)
      
  # displayPerformanceMeasure(env, agent)
  #displayPerformanceMeasure(env, agent2)

  return


main()