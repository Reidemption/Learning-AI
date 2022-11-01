# equivalent of game.py; maze.py; or BubbleModel.py
import random
import hashlib 

class Environment:
  def __init__(self, seed, size):
    self.state = []
    self.populateState(seed, size)
    self.players = {'score1': 0, 'score2': 0}
    
  def populateState(self, seed, size):
    hash = repr(seed).encode()
    i = 0
    print(size)
    while i < size:
        hash = hashlib.md5(hash).digest()
        for c in hash:
          if i < size:
            self.state.append(c)
            i += 1
          else:
            break
    print(self.state)
    
  def applyAction(self, action, player):
    value = 0
    if action == 1: #first item in state
      value = self.state.pop(0)
    elif action == -1: #last item in state array
      value = self.state.pop()
    else:
      print("Invalid action:", action)
    if player == 1:
      self.players['score1'] += value
    elif player == 2:
      self.players['score2'] += value
    return value
    
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
  
  def done(self):
    if self.GoalTest():
      print('Game Over.')
      print('player1: ', self.players['score1'], '\nplayer2: ', self.players['score2'])
      return True
    return False