import game

class Player(game.TFT): 
  def __init__(self, name):
    self.gold = 5
    self.xp = 8
    self.name = name
    self.streak = 0
    self.level = self.getLevel()
    self.bench = []
    self.board = []
    self.shop = []
    self.health = 100
  
  def buyXP(self):
    if self.gold < 4 or self.level == 9:
      return
    self.gold -= 4
    self.xp += 4
    
  def getLevel(self):
    if self.xp == 0:
      return 1
    elif self.xp >= 2 and self.xp < 8:
      return 2
    elif self.xp >= 8 and self.xp < 18:
      return 3
    elif self.xp >= 18 and self.xp < 38:
      return 4
    elif self.xp >= 38 and self.xp < 74:
      return 5
    elif self.xp >= 74 and self.xp < 130:
      return 6
    elif self.xp >= 130 and self.xp < 210:
      return 7
    elif self.xp >= 210 and self.xp < 310:
      return 8 
    elif self.xp >= 310:
      return 9
    
  def rerollShop(self):
    if self.gold < 2:
      return
    self.gold -= 2
    self.shop = game.TFT.generateUserShop(self.level)

  def placeHero(self, hero):
    self.board.append(hero)
    self.bench.pop(self.bench.index(hero))
  
  def getCurrentBoard(self):
    return self.board
  
  def getCurrentBench(self):
    return self.bench
  
  def earnGold(self, gold):
    self.gold += gold