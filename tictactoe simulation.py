import tictactoe
import random
import numpy as np
import main
p1w = 0
p2w = 0
draw = 0
sims = 1
gameInstance = tictactoe.Game()
done = gameInstance.checkOver()[0]
#    gameInstance.makeMove(random.choice(gameInstance.getMoves()))
for i in range(0, sims):
    while not done:
        move = (input())
        move = (int(move[0]), int(move[1]))
        gameInstance.makeMove(move)
        print(gameInstance.board)
        # gameInstance.makeMove(aiBestMove(gameInstance))
        done = gameInstance.checkOver()[0]
        if done:
            break
        print(done)
        gameInstance.makeMove(main.aiBestMove(gameInstance))
        done = gameInstance.checkOver()[0]
        print(gameInstance.board)
    if gameInstance.checkOver()[2] == 1:
        p1w += 1
    elif gameInstance.checkOver()[2] == 2:
        p2w += 1
    else:
        draw += 1
    print(p1w, p2w, draw)
# X_train = np.array(X_train)
# Y_train = np.array(Y_train)
# model = model.MyModel()
# model.compile(optimizer="adam", loss="mse")
# model.fit(X_train, Y_train, batch_size=1, epochs=1)
# model.save_weights("weights")
