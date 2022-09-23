import game, random
class Player(): 
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
    
  def buyHero(self):
    if len(self.shop) == 0:
      print('empty shop')
    for hero in self.shop:
      if hero not in self.board and hero not in self.bench and self.gold >= hero['cost'] and len(self.bench) <= self.level+1:
        print(hero['name'], 'costs', hero['cost'], 'gold and player has now:', self.gold)
        self.gold -= hero['cost']
        self.bench.append(hero)
        print(self.bench)
        print(self.board)
      else:
        print('no one purchased')
    if len(self.board) < self.level:
      self.placeHero()
    
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
    
  def endTurn(self):
    return

  def placeHero(self):
    hero = random.choice(self.bench)
    self.board.append(hero)
    self.bench.pop(self.bench.index(hero))
  
  def swapHero(self):
    print(self.board)
    print(self.bench)
    hero1 = random.choice(self.board)
    hero2 = random.choice(self.bench)
    self.board.pop(self.board.index(hero1))
    self.bench.pop(self.bench.index(hero2))
    self.board.append(hero2)
    self.bench.append(hero1)
    print('now swapped')
    print(self.board)
    print(self.bench)
  
  def getCurrentBoard(self):
    return self.board
  
  def getCurrentBench(self):
    return self.bench
  
  def earnGold(self, gold):
    self.gold += gold