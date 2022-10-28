# referencing model.py from TFT_Agent 

import random

class NumberPickerModel:
  def __init__(self):
    return
  
  def printState(self, state):
    return state
  
  def getLegalActions(self, state):
    actions = []
    if len(state) > 0:
      actions.append(1)
      actions.append(-1)
    else:
      actions.append(-1)
    return actions
    
  def done(self):
    if len(self.numbers) == 0:
      return True
    return False
  
  def Result(self, state, action):
    new_state = state.deepcopy()
    if action == 1:
      new_state.applyAction(1)
    elif action == -1:
      new_state.applyAction(-1)
    else:
      print('error')
    return new_state
  
  def GoalTest(self, state):
    if len(state.state) == 0:
      return True
    return False
  