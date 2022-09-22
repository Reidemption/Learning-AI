import game, heroes
import time

class Model:
  def __init__(self):
    pass
  
  def Actions(self, state, player):
    possible_actions = []
    if state.players[player].gold >= 4 and state.players[player].level < 9:
      possible_actions.append("buyXP")
    if state.players[player].gold >= 2:
      possible_actions.append("rerollShop")
    if len(state.players[player].bench) < 10 and state.players[player].gold > 0:
      possible_actions.append("buyHero")
    if len(state.players[player].board) < state.players[player].level:
      possible_actions.append("placeHero")
    if len(state.players[player].bench) > 0 and len(state.players[player].board) > 0:
      possible_actions.append("swapHero")
    possible_actions.append("endTurn")
    return possible_actions
  
  def Result(self, state, action, player):
    # ends up being called on each action from the Action method
    # Copies the state and returns the new state with the action applied (deep copy)
    # applies an action to the state and produces a new state
    new_state = state.deepcopy()  
    
    if action == "buyXP":
      new_state.players[player].buyXP()
    elif action == "rerollShop":
      new_state.players[player].rerollShop()
    elif action == "buyHero":
      new_state.players[player].buyHero()
    elif action == "placeHero":
      new_state.players[player].placeHero()
    
    return new_state
  
  def GoalTest(self, state, player):
    # if state is a goal state, return True
    desired_total = 12
    current_total = 0
    if player.gold > 20: 
      current_total += 5
    elif player.gold > 50:
      current_total += 10
    if len(player.board) == player.level:
      current_total += 3
    if len(player.bench) > 0:
      current_total += 1
    if desired_total >= current_total:
      return True
    return False
  
  def getPercepts(self):
    # return all info about current state of environment for the agent to be able to configure current copy of model 
    pass
  
  
def main():
  agent = game.TFT()
  game.intro()
  # agent.givePlayersShop()
  # agent.startGameForPlayers()
  # print(agent.players)
  for player in agent.players:
    if player.name == 0:
      start_round_time = time.time()
      game.roundStart(agent.round)
      game.userInfo(player)
      while game.userPrompts(agent.round, player) != False:
        game.userPrompts(agent.round, player)
      
      if start_round_time - time.time() > 30:
        print("Battle!")
    
    agent.battle()
    agent.round+=1
      
    heroes.buyHero(player, player.shop[0])
if __name__ == "__main__":
  main()