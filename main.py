import tictactoe
import random
import numpy as np
import model
import os
n = 0
visits = {}
differential = {}
model = model.MyModel()
model.compile(optimizer="adam", loss="mse", metrics=["accuracy"])
# X_train = np.load("X_train.npy")
# Y_train = np.load("Y_train.npy")
# model.fit(X_train, Y_train, batch_size=1, epochs=10)
# model.save_weights("weights.hdf5")
while os.path.isfile(str(n)+".hdf5"):
    n += 1
n -= 1


def heuristicValue(game):
    #    N = visits.get("total", 1)
    #    Ni = visits.get(hash(game.board), 1e-5)
    #    V = score.get(hash(game.board), 0)*1.0/Ni
    #    return V + C*(np.log(N)/Ni)
    V = model.predict(np.array([[game.board.reshape(9, 9)]]))
    return V


def record(game, score):
    global n
    try:
        model.load_weights(str(n)+".hdf5")
    except:
        pass
    X_train = []
    Y_train = []
    X_train.append([game.board.reshape(9, 9)])
    Y_train.append([score])
    model.fit(np.array(X_train), np.array(Y_train), batch_size=1,)
    n += 1
    if n%5000 == 0:
        model.save_weights(str(n)+".hdf5")


def playoutValue(game):
    if game.checkOver()[0]:
        record(game, -game.checkOver()[1])
        return -game.checkOver()[1]
    actionHeuristicDict = {}
    for move in game.getMoves():
        game.makeMove(move)
        actionHeuristicDict[move] = -heuristicValue(game)
        game.undoMove(move)
    move = max(actionHeuristicDict, key=actionHeuristicDict.get)
    # move = random.choice(game.getMoves())
    game.makeMove(move)
    value = -playoutValue(game)
    game.undoMove(move)
    record(game, value)
    return value


def monteCarloValue(game, N=5):
    scores = [playoutValue(game) for i in range(0, N)]
    return np.mean(scores)


def aiBestMove(game):
    actionDict = {}
    for move in game.getMoves():
        game.makeMove(move)
        print(game.board)
        actionDict[move] = -monteCarloValue(game)
        game.undoMove(move)
    print(max(actionDict, key=actionDict.get))
    return max(actionDict, key=actionDict.get)



