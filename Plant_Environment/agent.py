import env
import random
import copy 
from collections import deque
import queue
  
class Agent:
  def __init__(self, seed):
    self.model = env.Plant(seed)
    
  # random action
  def decideRandomAction(self, percepts):
    self.model.updatePercepts(percepts)
    actions = self.model.getLegalActions()
    action = random.choice(actions)
    return action
  
  def decideComputedAction(self, percepts):
    self.model.updatePercepts(percepts)
    visited = [] # want to use this to keep track of visited nodes
    frontier = deque()
    frontier.append((copy.deepcopy(self.model), None, None)) #add child, parent, and action to frontier
    i = 0
    while len(list(frontier)) > 0:
      i+= 1
      state = frontier.pop()
      print('state', i ,state)
      if state[0].GoalTest():
        child_node = state[0]
        parent_node = state[1]
        while parent_node != None:
          # grandchild_node = child_node
          child_node = parent_node[0]
          parent_node = parent_node[1]
        action = parent_node[2]
        return action
      for action in state[0].getLegalActions():
        print('og state', state[0])
        new_state = state[0].updatePercepts(action)
        print('new_state',new_state)
        frontier.append((new_state, state[0], action))
  
  def uniformCostSearch(self, percepts):
    self.model.updatePercepts(percepts)
    if self.model.GoalTest():
      return None
    frontier = queue.PriorityQueue(720)
    model_copy = copy.deepcopy(self.model)
    # print('model copy',model_copy)
    frontier.put((0,model_copy))
    while not frontier.empty():
      state = frontier.get()
      # print('state 1',state[1])
      if state[1].GoalTest():
        print('goal test passed.')
        print(state[0])
        return state[0] #TODO: should return the action required to get to the state
      for action in state[1].getLegalActions():
        new_state = copy.deepcopy(state[1])
        new_state.applyAction(action)
        new_cost = state[0] + state[1].cost(action)
        if new_state.isPlantAlive():
          print('put in frontier')
          frontier.put((new_cost, new_state))
        # print((new_cost, new_state))
        

  
def main():
  seed = 1234567890
  environment = env.Plant(seed)
  agent = Agent(seed)
  while not environment.done():
    percepts = environment.getPercepts()
    # print('percepts:', percepts)
    action = agent.uniformCostSearch(percepts)
    # action = agent.decideRandomAction(percepts)
    # print('action:', action)
    # print('\n')
    environment.applyAction(action)
  return


main()