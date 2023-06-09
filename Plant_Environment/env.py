import random
import copy

class Plant:
  def __init__(self, seed1, seed2, seed3):
    self.plant = {
      'time': 0,
      'days': 0,
      'water_levels': self.initializePlant(seed1),
      'alive': True,
      'soil_quality':self.initializePlant(seed2),
      'light_levels': self.initializePlant(seed3),
      'inLight': self.initializeInLight(),
    }
  
  def cost(self,action):
    if action == 'water':
      return .98
    elif action == 'wait':
      return .1
    elif action == 'change soil':
      return .99
    elif action == 'light':
      return .63
    elif action == 'remove light':
      return .36
    
  def initializePlant(self, seed):
    random.seed(seed)
    water_or_soil = random.random()
    while water_or_soil < 0.3 or water_or_soil > 0.8:
      water_or_soil = random.random()
    return water_or_soil
  
  def initializeInLight(self):
    return random.choice([True, False])
  
  def updatePercepts(self, state):
    self.plant = state
    
  def getPercepts(self):
    return self.plant
  
  def getLegalActions(self):
    if self.plant['days'] >= 30 or not self.plant['alive']:
      return []
    if self.plant['inLight']:
      return ['water', 'wait', 'change soil', 'remove light']
    return ['water', 'wait', 'change soil', 'light']
      
  
  def changeSoil(self):
    self.plant['soil_quality'] += .8
    
  def moveIntoLight(self):
    self.plant['inLight'] = True
    
  def removeFromLight(self):
    self.plant['inLight'] = False
    
  def waterPlant(self):
    self.plant['water_levels'] += 0.5
  
  def applyAction(self, action):
    if action == 'water':
      self.waterPlant()
    elif action == 'wait':
      pass
    elif action == 'change soil':
      self.changeSoil()
    elif action == 'light':
      self.moveIntoLight()
    elif action == 'remove light':
      self.removeFromLight()
    else:
      print("Invalid action:", action)
    self.agePlant()
    
  
  def GoalTest(self):
    if (self.plant['days'] >= 29 and self.plant['time'] >= 23) and self.plant['alive'] : #if the simulation has run for less than 30 days and the plant is still alive
      return True
    return False
    
  def done(self):
    if self.GoalTest():
      print("Plant simulation has ended with the plant alive") if self.plant['alive'] else print("Plant simulation has ended with the plant dead")
      return True
    return False
  
  def isPlantAlive(self):
    return self.plant['alive']
  
  def plantAlive(self):
    if self.plant['water_levels'] <= 0.2 or self.plant['water_levels'] >= 1.0:
      # print('Watered the plant too often or not enough.')
      self.plant['alive'] = False
    
    if self.plant['soil_quality'] <= .1 or self.plant['soil_quality'] >= 2.5:
      self.plant['alive'] = False
      # print('Changed soil too often or not enough.')
      
    if self.plant['light_levels'] <= 0.0 or self.plant['light_levels'] >= 3.0:
      self.plant['alive'] = False
      # print('Exposed the plant to too much light or not enough.')
  
  def agePlant(self):
    if self.plant['time'] <= 17 and self.plant['time'] >= 7 and self.plant['inLight']:
      self.plant['light_levels'] += 0.727272
    elif self.plant['time'] <= 17 and self.plant['time'] >= 7 and not self.plant['inLight']:
      self.plant['light_levels'] -= 0.363636
    if self.plant['time'] >= 23:
      self.plant['time'] = 0
      self.plant['days'] += 1
    else:
      self.plant['time'] += 1
    self.plant['water_levels'] -= 0.00555
    self.plant['soil_quality'] -= 0.0012987
    self.plantAlive()
    
  def printState(self):
    print("Water Levels:", self.plant['water_levels'])
    print("Soil Quality:", self.plant['soil_quality'])
    print("Light Levels:", self.plant['light_levels'])
    print("In Light:", self.plant['inLight'])