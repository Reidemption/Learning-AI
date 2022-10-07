from BubbleModel import BubbleModel

class Environment:
    def __init__(self,seed,numPBubbles,numSBubbles,numCols):
        self.model = BubbleModel(seed,numPBubbles,numSBubbles,numCols)