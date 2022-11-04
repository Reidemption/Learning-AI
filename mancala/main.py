import model
import agents

def main():
    env=model.Model()
    player1=agents.randomAgent(1)
    player2=agents.randomAgent(2)
    while not env.GoalTest():
        player1turn=1
        while player1turn == 1:
            percepts = env.getObservable()
            action = player1.Top_Max(percepts)
            player1turn = env.applyAction(action,1)
         
        player2turn=1
        while player2turn == 1:
            percepts = env.getObservable()
            action = player2.agentFunction(percepts)
            player2turn = env.applyAction(action,2)
          
        env.printBoard()
    
    return

if '__main__':
    main()