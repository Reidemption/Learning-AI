import model
import random
import copy

LIMIT = 5   
#the parameter player will be either 1 or 2 , which player they are on the board
class randomAgent:
    def __init__(self,player):
        self.model = model.Model()
        self.mPlayer=player
        
    def agentFunction(self, state):
        self.model.updatePercepts(state)
        action = None
        actions=self.model.getLegalActions(self.mPlayer)
        if actions != []:
            action = random.choice(actions)
        return action
    
    def Top_Max(self, percepts):
        self.model.updatePercepts(percepts)
        limit=0
        if self.model.GoalTest():
            return None
        v = -99999999
        best_action = None
        for a in self.model.getLegalActions(self.mPlayer):
            model_copy = copy.deepcopy(self.model)
            model_copy.applyAction(a, 1)
            new_v = self.Min(model_copy, v,limit)
            if new_v > v:
                v = new_v
                best_action = a
        return best_action

    def Max(self, state, greek, limit):
        if self.model.GoalTest() or limit == LIMIT:
            return self.model.evaluate(2)
        limit+=1
        alpha = -99999999
        for action in self.model.getLegalActions(self.mPlayer):
            model_copy = copy.deepcopy(state)
            model_copy.applyAction(action, 1)
            new_alpha = self.Min(model_copy, alpha, limit)
            if new_alpha > alpha:
                alpha = new_alpha
            if alpha > greek:
                return alpha
        
        return alpha
            
    def Min(self, state, greek, limit):
        if self.model.GoalTest() or limit == LIMIT:
            return self.model.evaluate(1)
        limit+=1
        beta = 99999999
        for action in self.model.getLegalActions(self.mPlayer):
            model_copy = copy.deepcopy(state)
            # print(state)
            model_copy.applyAction(action, 2)
            new_beta = self.Max(model_copy, beta, limit)
            if new_beta < beta:
                beta = new_beta
            if beta < greek:
                return beta
        return beta