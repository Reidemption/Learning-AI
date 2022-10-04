from model import *
from maze import *
from collections import deque
import random
import copy
class RandomAgent:
  def __init__(self, maze):
    self.model = Model(maze)
    
  def agentFunction(self, coords):
    self.model.updatePercepts(coords)
    actions = self.model.getLegalActions()
    action = random.choice(actions)
    
    return action
  
  def dfsSearch(self, coords):
    self.model.updatePercepts(coords)
    frontier = deque() #this should be a stack from python's collections library
    frontier.append((copy.deepcopy(self.model), None)) #frontier pushes a copy of the model and the parent 'None' for initial state 
    while len(list(frontier)) > 0:
      state = frontier.pop()
      if state[0].GoalTest():
        child_node = state[0]
        parent_node = state[1]
        while parent_node != None:
          grandchild_node = child_node
          child_node = parent_node[0]
          parent_node = parent_node[1]
        
        action = ''
        if child_node.mState.mX_Location > grandchild_node.mState.mX_Location:
          action = 'R'
        elif child_node.mState.mX_Location < grandchild_node.mState.mX_Location:
          action = 'L'
        elif child_node.mState.mY_Location > grandchild_node.mState.mY_Location:
          action = 'D'
        else:
          action = 'U'
        return action
          # return state[1] #return the parent of the goal state
      for action in state[0].getLegalActions():
        print(state[0].getLegalActions())
        new_state = state[0].Result(action)
        frontier.append((new_state, state))
    
    
    
def main():
    maze = Maze(10,10)
    
    env = Model(maze)
    agent = RandomAgent(maze)
    
    # shows what the maze looks like
    env.mState.printMaze()
    
    while not env.done():
      # goaltest = env.GoalTest()
      percepts = env.getObservable()
      # action = agent.agentFunction(percepts) # uncomment this line to use the random agent
      action = agent.dfsSearch(percepts) # uncomment this line to use dfs search
      print(action)
      env.applyAction(action)
      
    env.mState.displayPerformanceMeasure(agent.model.mState, env.mGoal)
    
    return

if '__main__':
    main()