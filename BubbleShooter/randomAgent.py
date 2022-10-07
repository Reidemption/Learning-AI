from BubbleModel import BubbleModel
import random

class RandomAgent:

    def __init__(self):
        self.model = BubbleModel(None,None,None,None)
    
    def agentFunction(self,percepts):
        self.model.updateFromPercepts(percepts)
        actions = self.model.actions()
        random.seed(None)
        action = random.choice(actions)
        print(action)
        self.model.printState()
        print("")
        return action