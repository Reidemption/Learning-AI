# equivalent of game.py; maze.py; or BubbleModel.py
import random
import hashlib 

class Environment:
  def __init__(self, seed, size):
    self.state = self.populateState(seed)
    
  def populateState(self, seed, size):
    hash = seed
    i = 0
    while i < size:
        hash = hashlib.md5(hash).digest()
        for c in hash:
            self.state.append(c)
    print(self.state)
    
  def applyAction(self, action):
    if action == 1: #first item in state
      return self.state.pop(0)
    elif action == -1: #last item in state array
      return self.state.pop()
    else:
      print("Invalid action:", action)
    
  def Result(self, player, action):
    new_state = player.deepcopy()
    if action == 1:
      new_state.applyAction(1)
    elif action == -1:
      new_state.applyAction(-1)
    else: 
      print("Invalid action:", action)
    return new_state
      
  def getPercepts(self):
    return self.state
  
  def GoalTest(self):
    if len(self.state) == 0:
      return True
    return False