from model import *
from maze import *
from collections import deque
import random

class RandomAgent:
  def __init__(self, maze):
    self.model = Model(maze)
    
  def agentFunction(self, coords):
    self.model.updatePercepts(coords)
    actions = self.model.getLegalActions()
    action = random.choice(actions)
    
    return action
  
  def dfsSearch(self, initial_state, actions, results, goaltest):
    frontier = deque() #this should be a stack from python's collections library
    frontier.append(initial_state)
    while len(frontier) > 0:
      state = frontier.pop()
      if goaltest(state):
        return True
      for action in actions(state):
        new_state = results(state, action)
        frontier.append(new_state)
    
    
    
def main():
    maze = Maze(10,10)
    
    env = Model(maze)
    agent = RandomAgent(maze)
    
    # shows what the maze looks like
    env.mState.printMaze()
    
    while not env.done():
      # goaltest = env.GoalTest()
      percepts = env.getObservable()
      action = agent.agentFunction(percepts) # uncomment this line to use the random agent
      # action = agent.dfsSearch(initial_state, percepts) # uncomment this line to use dfs search
      env.applyAction(action)
        
    env.mState.displayPerformanceMeasure(agent.model.mState, env.mGoal)
    
    return

if '__main__':
    main()