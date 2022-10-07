from randomAgent import RandomAgent
from environment import Environment
from rationalAgent import RationalAgent

def performanceMeasure(model):
    shotsLeft = len(model.sBubbles)
    bubblesLeft = 0
    for i in range(model.numRows):
        for j in range(model.numCols):
            if model.pBubbles[i][j] != 0:
                bubblesLeft += 1
    return shotsLeft * 20 + bubblesLeft * -50

def main():
    env = Environment(12,10,30,6)
    # agent = RandomAgent()
    agent = RationalAgent(12,10,30,6)
    env.model.printState()
    while not env.model.done():
        percepts = env.model.getObservablePercepts()
        action = agent.agentFunction(percepts)
        print(action)
        env.model.applyAction(action)
    env.model.printState()
    # print(performanceMeasure(env.model))
    print(env.model.performanceMeasure())


main()