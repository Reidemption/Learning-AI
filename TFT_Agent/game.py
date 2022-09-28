import random 
import player

class Environment:
  """ 
  https://app.mobalytics.gg/tft/champions?cost=1
  https://tftactics.gg/db/rolling
  https://lolchess.gg/guide/exp?hl=en-US -> gold
  TODO:
  populate the "shop" with heroes per player
  add in each percentages per rerolls
  allow the user to reroll
  give users gold per round
  battle of enemies
  pick which enemy to battle -> https://www.reddit.com/r/CompetitiveTFT/comments/g5slm2/sweaty_tft_scouting_tips_to_predict_opponent/
  create array of dictionaries with heroes with their traits ✅
  current round
  minion rounds?
  augment rounds?
  """
  def __init__(self):
    self.players = [player.Player(i) for i in range(2)]
    self.round = 0
    self.cost1 = [
  {'name': "Ezreal", 'traits': ['Tempest', 'Swiftshot'], 'cost': 1},
  {'name': "Karma", 'traits': ['Jade', 'Dragonmancer'], 'cost': 1},
  {'name': "Leona", 'traits': ['Mirage', 'Guardian'], 'cost': 1},
  {'name': "Malphite", 'traits': ['Lagoon', 'Bruiser'], 'cost': 1},
  {'name': "Nasus", 'traits': ['Shimmerscale', 'Guardian'], 'cost': 1},
  {'name': "Nidalee", 'traits': ['Astral', 'Shapeshifter'], 'cost': 1},
  {'name': "Sejuani", 'traits': ['Guild', 'Cavalier'], 'cost': 1},
  {'name': "Senna", 'traits': ['Ragewing', 'Cannoneer'], 'cost': 1},
  {'name': "Sett", 'traits': ['Ragewing', 'Dragonmancer'], 'cost': 1},
  {'name': "Scarner", 'traits': ['Astral', 'Bruiser'], 'cost': 1},
  {'name': "Taliyah", 'traits': ['Lagoon', 'Mage'], 'cost': 1},
  {'name': "Vladimir", 'traits': ['Astral', 'Mage'], 'cost': 1},
  {'name': "Wukong", 'traits': ['Jade', 'Warrior'], 'cost': 1}
]
    self.cost2 = [
        {'name': "Aphelios", 'traits': ['Darkflight', 'Cannoneer'], 'cost': 2},
        {'name': "Braum", 'traits': ['Scalescorn', 'Guardian'], 'cost': 2},
        {'name': "Gnar", 'traits': ['Jade', 'Shapeshifter'], 'cost': 2},
        {'name': "Jax", 'traits': ['Jade', 'Shimmerscale', 'Bruiser'], 'cost': 2},
        {'name': "Kai'Sa", 'traits': ['Lagoon', 'Dragonmancer'], 'cost': 2},
        {'name': "Lillia", 'traits': ['Scalescorn', 'Mage' 'Cavalier'], 'cost': 2},
        {'name': "Lux", 'traits': ['Astral', 'Mage'], 'cost': 2},
        {'name': "Qiyana", 'traits': ['Tempest', 'Assassin'], 'cost': 2},
        {'name': "Rell", 'traits': ['Darkflight', 'Cavalier'], 'cost': 2},
        {'name': "Twitch", 'traits': ['Guild', 'Swiftshot'], 'cost': 2},
        {'name': "Yone", 'traits': ['Mirage', 'Warrior'], 'cost': 2},
        {'name': "Zac", 'traits': ['Lagoon', 'Guardian'], 'cost': 2},
        {'name': "Zyra", 'traits': ['Whispers', 'Evoker'], 'cost': 2}]
    self.cost3 = [
        {'name': "Diana", 'traits': ['Scalescorn', 'Assassin'], 'cost': 3},
        {'name': "Heimerdinger", 'traits': ['Mage'], 'cost': 3},
        {'name': "Lee Sin", 'traits': ['Tempest', 'Dragonmancer'], 'cost': 3},
        {'name': "Lulu", 'traits': ['Evoker'], 'cost': 3},
        {'name': "Nunu", 'traits': ['Mirage', 'Cavalier'], 'cost': 3},
        {'name': "Olaf", 'traits': ['Scalescorn', 'Bruiser' 'Warrior'], 'cost': 3},
        {'name': "Rakan", 'traits': ['Ragewing', 'Guardian', 'Mystic'], 'cost': 3},
        {'name': "Rengar", 'traits': ['Darkflight', 'Assassin'], 'cost': 3},
        {'name': "Seraphine", 'traits': ['Lagoon', 'Evoker', 'Mystic'], 'cost': 3},
        {'name': "Sylas", 'traits': ['Whispers', 'Mage', 'Bruiser'], 'cost': 3},
        {'name': "Tristana", 'traits': ['Cannoneer'], 'cost': 3},
        {'name': "Varus", 'traits': ['Astral', 'Swiftshot'], 'cost': 3},
        {'name': "Volibear", 'traits': ['Shimmerscale', 'Dragonmancer'], 'cost': 3},
        {'name': "Zeri", 'traits': ['Lagoon', 'Cannoneer'], 'cost': 3},
        ]
    self.cost4 = [
        {'name': "Graves", 'traits': ['Tempest', 'Cannoneer'], 'cost': 4},
        {'name': "Hecarim", 'traits': ['Ragewing', 'Cavalier'], 'cost': 4},
        {'name': "Jayce", 'traits': ['Guild', 'Shapeshifter'], 'cost': 4},
        {'name': "Nilah", 'traits': ['Lagoon', 'Assassin'], 'cost': 4},
        {'name': "Pantheon", 'traits': ['Whispers', 'Warrior'], 'cost': 4},
        {'name': "Xayah", 'traits': ['Ragewing', 'Swiftshot'], 'cost': 4},
      ]
    self.cost5 = [
  {'name': "Bard", 'traits': ['Guild', 'Mystic', 'Bard'], 'cost': 5},
  {'name': "Soraka", 'traits': ['Jade', 'Starcaller'], 'cost': 5},
  {'name': "Yasuo", 'traits': ['Mirage', 'Dragonmancer', 'Warrior'], 'cost': 5},
  {'name': "Zoe", 'traits': ['Shimmerscale', 'Spellthief', 'Mage'], 'cost': 5},
]
    self.givePlayersShop()
    self.startGameForPlayers()
    self.max_moves = 1
    self.done = False
    
  def showState(self):
    print(self.players)
    return
    
  # https://www.reddit.com/r/CompetitiveTFT/comments/g5slm2/sweaty_tft_scouting_tips_to_predict_opponent/
  # Very dumbed down version of the link above since there are only two players.
  def battle(self):
    i = 0
    combat(self.players[i], self.players[i+1])
  
  def givePlayersShop(self):
    for player in self.players:
      self.generateUserShop(player)
  
  def startGameForPlayers(self):
    for player in self.players:
      player.board.append(self.generateHero(1))
      player.board.append(self.generateHero(1))
      player.board.append(self.generateHero(2))
  
  def generateHero(self,cost):
    if cost == 1:
      hero = random.choice(self.cost1)
    elif cost == 2:
      hero = random.choice(self.cost2)
    elif cost == 3:
      hero = random.choice(self.cost3)
    return hero 
  
  def generateUserShop(self, player, fee=False):
    shop = []
    if fee:
      player.rerollShop()
    reroll_percentages = getRerollPercentages(player.level)
    for i in range(0, 5):
      cost_value = random.random() #random number [0-1)
      if cost_value < reroll_percentages[0]:
        shop.append(random.choice(self.cost1))
      elif cost_value < reroll_percentages[1] + reroll_percentages[0]:
        shop.append(random.choice(self.cost2))
      elif cost_value < reroll_percentages[2] + reroll_percentages[1] + reroll_percentages[0]:
        shop.append(random.choice(self.cost3))
      elif cost_value < reroll_percentages[3] + reroll_percentages[2] + reroll_percentages[1] + reroll_percentages[0]:
        shop.append(random.choice(self.cost4))
      elif cost_value < reroll_percentages[4] + reroll_percentages[3] + reroll_percentages[2] + reroll_percentages[1] + reroll_percentages[0]:
        shop.append(random.choice(self.cost5))        
    return shop
      
  def updateCostList(self, hero):
    if hero['cost'] == 1:
      index = self.cost1.index(hero)
      self.cost1[index]['current'] += 1
    elif hero['cost'] == 2:
      index = self.cost2.index(hero)
      self.cost2[index]['current'] += 1
    elif hero['cost'] == 3:
      index = self.cost3.index(hero)
      self.cost3[index]['current'] += 1
    elif hero['cost'] == 4:
      index = self.cost4.index(hero)
      self.cost4[index]['current'] += 1
    elif hero['cost'] == 5:
      index = self.cost5.index(hero)
      self.cost5[index]['current'] += 1
  
  def applyAction(self, player_index, action):
    if action == 'rerollShop':
      self.players[player_index].shop = self.generateUserShop(self.players[player_index], True )
    else:
      callableAction = getattr(self.players[player_index], action)
      callableAction()
  
  def Result(self, player, action):
    # TODO: mess with later when we have a better idea of how Curtis wants this used.
    # ends up being called on each action from the Action method
    # Copies the state and returns the new state with the action applied (deep copy)
    # applies an action to the state and produces a new state
    new_state = player.deepcopy()  
    
    if action == "buyXP":
      new_state.buyXP()
    elif action == "rerollShop":
      new_state.rerollShop()
    elif action == "buyHero":
      new_state.buyHero()
    elif action == "placeHero":
      new_state.placeHero()
    
    return new_state
  
  def GoalTest(self):
    
    if (self.players[0].health == 0 or self.players[1].health == 0):
      print("Player 1 has", self.players[0].health, "health left.")
      print("Player 2 has", self.players[1].health, "health left.")
      return True
    return False
  
  def getPercepts(self, player_index):
    # return all info about current state of environment for the agent to be able to configure current copy of model 
    return self.players[player_index]

def combat(player1, player2):
  attacking_board = player1.board
  defending_board = player2.board
  player1_hero_total = 0
  player2_hero_total = 0
  for hero in attacking_board:
    player1_hero_total += hero['cost']
  for hero in defending_board:
    player2_hero_total += hero['cost']
  
  # random number between 0 and 1
  winner = random.random()
  
  if winner < .5:
    print(f'{player1.name} wins the round!')
    print(f'{player1.name} has {player1.health} and {player2.name} has {player2.health}')
    earned_gold = earnedGold(player1, True)
    player1.earnGold(earned_gold)
    player2_gold = earnedGold(player2, False)
    player2.earnGold(player2_gold)
    player2.health -= 5
    return
  else:
    print(f'{player2.name} wins the round!')
    earned_gold = earnedGold(player2, True)
    player2.earnGold(earned_gold)
    player1_gold = earnedGold(player1, False)
    player1.earnGold(player1_gold)
    player1.health -= 5
    return
  
def earnedGold(player, battle_victory):
  earned_gold = 4
  interest = int(player.gold * 0.1)
  battle_result = 1 if battle_victory else 0
  return earned_gold + interest + battle_result

def getRerollPercentages(level):
  if level == 3:
    return [.75,.25,0,0,0]
  elif level == 4:
    return [.55,.3,.15,0,0]
  elif level == 5:
    return [.45,.33,.20,.2,0]
  elif level == 6:
    return [.25,.40,.30,.05,0]
  elif level == 7:
    return [.19,.30,.35,.15,.01]
  elif level == 8:
    return [.16,.20,.35,.25,.04]
  elif level == 9:
    return [.09,.15,.30,.30,.16]
  return [1,0,0,0,0]