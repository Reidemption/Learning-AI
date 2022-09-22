import random 
import player
import heroes

class TFT:
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
  {'name': "Ezreal", 'traits': ['Tempest', 'Swiftshot'], 'cost': 1, 'total': 29, 'current': 0},
  {'name': "Karma", 'traits': ['Jade', 'Dragonmancer'], 'cost': 1, 'total': 29, 'current': 0},
  {'name': "Leona", 'traits': ['Mirage', 'Guardian'], 'cost': 1, 'total': 29, 'current': 0},
  {'name': "Malphite", 'traits': ['Lagoon', 'Bruiser'], 'cost': 1, 'total': 29, 'current': 0},
  {'name': "Nasus", 'traits': ['Shimmerscale', 'Guardian'], 'cost': 1, 'total': 29, 'current': 0},
  {'name': "Nidalee", 'traits': ['Astral', 'Shapeshifter'], 'cost': 1, 'total': 29, 'current': 0},
  {'name': "Sejuani", 'traits': ['Guild', 'Cavalier'], 'cost': 1, 'total': 29, 'current': 0},
  {'name': "Senna", 'traits': ['Ragewing', 'Cannoneer'], 'cost': 1, 'total': 29, 'current': 0},
  {'name': "Sett", 'traits': ['Ragewing', 'Dragonmancer'], 'cost': 1, 'total': 29, 'current': 0},
  {'name': "Scarner", 'traits': ['Astral', 'Bruiser'], 'cost': 1, 'total': 29, 'current': 0},
  {'name': "Taliyah", 'traits': ['Lagoon', 'Mage'], 'cost': 1, 'total': 29, 'current': 0},
  {'name': "Vladimir", 'traits': ['Astral', 'Mage'], 'cost': 1, 'total': 29, 'current': 0},
  {'name': "Wukong", 'traits': ['Jade', 'Warrior'], 'cost': 1, 'total': 29, 'current': 0}
]
    self.cost2 = [
        {'name': "Aphelios", 'traits': ['Darkflight', 'Cannoneer'], 'cost': 2, 'total': 22, 'current': 0},
        {'name': "Braum", 'traits': ['Scalescorn', 'Guardian'], 'cost': 2, 'total': 22, 'current': 0},
        {'name': "Gnar", 'traits': ['Jade', 'Shapeshifter'], 'cost': 2, 'total': 22, 'current': 0},
        {'name': "Jax", 'traits': ['Jade', 'Shimmerscale', 'Bruiser'], 'cost': 2, 'total': 22, 'current': 0},
        {'name': "Kai'Sa", 'traits': ['Lagoon', 'Dragonmancer'], 'cost': 2, 'total': 22, 'current': 0},
        {'name': "Lillia", 'traits': ['Scalescorn', 'Mage' 'Cavalier'], 'cost': 2, 'total': 22, 'current': 0},
        {'name': "Lux", 'traits': ['Astral', 'Mage'], 'cost': 2, 'total': 22, 'current': 0},
        {'name': "Qiyana", 'traits': ['Tempest', 'Assassin'], 'cost': 2, 'total': 22, 'current': 0},
        {'name': "Rell", 'traits': ['Darkflight', 'Cavalier'], 'cost': 2, 'total': 22, 'current': 0},
        {'name': "Twitch", 'traits': ['Guild', 'Swiftshot'], 'cost': 2, 'total': 22, 'current': 0},
        {'name': "Yone", 'traits': ['Mirage', 'Warrior'], 'cost': 2, 'total': 22, 'current': 0},
        {'name': "Zac", 'traits': ['Lagoon', 'Guardian'], 'cost': 2, 'total': 22, 'current': 0},
        {'name': "Zyra", 'traits': ['Whispers', 'Evoker'], 'cost': 2, 'total': 22, 'current': 0}]
    self.cost3 = [
        {'name': "Diana", 'traits': ['Scalescorn', 'Assassin'], 'cost': 3, 'total': 18, 'current': 0},
        {'name': "Heimerdinger", 'traits': ['Mage'], 'cost': 3, 'total': 18, 'current': 0},
        {'name': "Lee Sin", 'traits': ['Tempest', 'Dragonmancer'], 'cost': 3, 'total': 18, 'current': 0},
        {'name': "Lulu", 'traits': ['Evoker'], 'cost': 3, 'total': 18, 'current': 0},
        {'name': "Nunu", 'traits': ['Mirage', 'Cavalier'], 'cost': 3, 'total': 18, 'current': 0},
        {'name': "Olaf", 'traits': ['Scalescorn', 'Bruiser' 'Warrior'], 'cost': 3, 'total': 18, 'current': 0},
        {'name': "Rakan", 'traits': ['Ragewing', 'Guardian', 'Mystic'], 'cost': 3, 'total': 18, 'current': 0},
        {'name': "Rengar", 'traits': ['Darkflight', 'Assassin'], 'cost': 3, 'total': 18, 'current': 0},
        {'name': "Seraphine", 'traits': ['Lagoon', 'Evoker', 'Mystic'], 'cost': 3, 'total': 18, 'current': 0},
        {'name': "Sylas", 'traits': ['Whispers', 'Mage', 'Bruiser'], 'cost': 3, 'total': 18, 'current': 0},
        {'name': "Tristana", 'traits': ['Cannoneer'], 'cost': 3, 'total': 18, 'current': 0},
        {'name': "Varus", 'traits': ['Astral', 'Swiftshot'], 'cost': 3, 'total': 18, 'current': 0},
        {'name': "Volibear", 'traits': ['Shimmerscale', 'Dragonmancer'], 'cost': 3, 'total': 18, 'current': 0},
        {'name': "Zeri", 'traits': ['Lagoon', 'Cannoneer'], 'cost': 3, 'total': 18, 'current': 0},
        ]
    self.cost4 = [
        {'name': "Graves", 'traits': ['Tempest', 'Cannoneer'], 'cost': 4, 'total': 12, 'current': 0},
        {'name': "Hecarim", 'traits': ['Ragewing', 'Cavalier'], 'cost': 4, 'total': 12, 'current': 0},
        {'name': "Jayce", 'traits': ['Guild', 'Shapeshifter'], 'cost': 4, 'total': 12, 'current': 0},
        {'name': "Nilah", 'traits': ['Lagoon', 'Assassin'], 'cost': 4, 'total': 12, 'current': 0},
        {'name': "Pantheon", 'traits': ['Whispers', 'Warrior'], 'cost': 4, 'total': 12, 'current': 0},
        {'name': "Xayah", 'traits': ['Ragewing', 'Swiftshot'], 'cost': 4, 'total': 12, 'current': 0},
      ]
    self.cost5 = [
  {'name': "Bard", 'traits': ['Guild', 'Mystic', 'Bard'], 'cost': 5, 'total': 10, 'current': 0},
  {'name': "Soraka", 'traits': ['Jade', 'Starcaller'], 'cost': 5, 'total': 10, 'current': 0},
  {'name': "Yasuo", 'traits': ['Mirage', 'Dragonmancer', 'Warrior'], 'cost': 5, 'total': 10, 'current': 0},
  {'name': "Zoe", 'traits': ['Shimmerscale', 'Spellthief', 'Mage'], 'cost': 5, 'total': 10, 'current': 0},
]
    self.givePlayersShop()
    self.startGameForPlayers()
    
    
  # https://www.reddit.com/r/CompetitiveTFT/comments/g5slm2/sweaty_tft_scouting_tips_to_predict_opponent/
  # Very dumbed down version of the link above since there are only two players.
  def battle(self):
    for i in range(len(self.players)):
      combat(self.players[i], self.players[i+1])
      i+1
  
  def givePlayersShop(self):
    for player in self.players:
      heroes.generateUserShop(player)
  
  def startGameForPlayers(self):
    for player in self.players:
      player.board.append(heroes.generateHero(1))
      player.board.append(heroes.generateHero(1))
      player.board.append(heroes.generateHero(2))
  
  def generateHero(self,cost):
    if cost == 1:
      hero = random.choice(self.cost1)
    elif cost == 2:
      hero = random.choice(self.cost2)
    elif cost == 3:
      hero = random.choice(self.cost3)
    hero['current'] += 1
    return hero 
  
  def generateUserShop(self,player_index):
    player = self.players[player_index]
    shop = []
    reroll_percentages = heroes.getRerollPercentages(player.level)
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
    player.shop = shop

  def buyHero(self, player_index):
    player = self.players[player_index]
    available_heroes = set(player.bench).intersection(player.shop)
    for hero in available_heroes:
      if player.gold >= hero['cost'] and hero['current'] != hero['total']:
        player.gold -= hero['cost']
        self.updateCostList(hero)
        player.bench.append(hero)
      
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

def combat(player1, player2):
  attacking_board = player1.board
  defending_board = player2.board
  player1_hero_total = 0
  player2_hero_total = 0
  for hero in attacking_board:
    player1_hero_total += hero['cost']
  for hero in defending_board:
    player2_hero_total += hero['cost']
  
  if player1_hero_total > player2_hero_total:
    print(f'{player1.name} wins the round!')
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
  
def userInfo(player):
  print(f'Gold: {player.gold} \nLevel: {player.level}')
  print('Shop:', *player.shop, sep = "\n")
  print('Board:', *player.board, sep = "\n")
  print('Bench:', *player.bench, sep = "\n")

def userPrompts(player):
  print(f"Press 'r' to reroll the shop. \nPress 'b' to buy a hero. \nPress 'p' to place a hero on the board. \nPress 's' to see your current board. \nPress 'q' to quit the game.")
  user_input = input()
  if user_input == 'r':
    player.rerollShop()
  elif user_input == 'b':
    index = input('Index of hero to buy: ')
    heroes.buyHero(player, player.shop[int(index)])
  elif user_input == 'p':
    index = input('Index of hero to place: ')
    player.placeHero(player.bench[int(index)])
  elif user_input == 's':
    print(player.board, '\n', player.bench)
  elif user_input == 'q':
    return False
  
def intro():
  print('Welcome to Terminal Based Teamfight Tactics!')