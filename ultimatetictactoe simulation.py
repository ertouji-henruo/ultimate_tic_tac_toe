import main
import random
import numpy as np
import ultimatetictactoe
import model

for i in range(0, 20):
    gameInstance = ultimatetictactoe.Game()
    done = gameInstance.checkOver()[0]
    move = random.choice(gameInstance.getMoves())
    gameInstance.makeMove(move)
    # print(move)
    # print(gameInstance.board)
    while not done:
        # move = random.choice(gameInstance.getMoves())
        move = main.aiBestMove(gameInstance)
        # move = input()
        # move = (int(move[0]), int(move[1]), int(move[2]), int(move[3]))
        gameInstance.makeMove(move)
        print("move made", move)
        print(gameInstance.board)
        # print(gameInstance.board)
        done = gameInstance.checkOver()[0]
        if done:
            break
        # move = random.choice(gameInstance.getMoves())
        move = main.aiBestMove(gameInstance)
        gameInstance.makeMove(move)
        print("move made", move)
        print(gameInstance.board)
        done = gameInstance.checkOver()[0]
    print("done sim " + str(i))



# X_train = np.array(main.X_train)
# np.save("X_train.npy", X_train)
# Y_train = np.array(main.Y_train)
# np.save("Y_train.npy", Y_train)

# model = model.MyModel()
# model.compile(optimizer="adam", loss="mse", metrics=["accuracy"])
# model.load_weights("weights.hdf5")
# X_train = np.load("X_train.npy")
# Y_train = np.load("Y_train.npy")
# model.fit(X_train, Y_train, batch_size=1, epochs=10)
# model.save_weights("weights.hdf5")
