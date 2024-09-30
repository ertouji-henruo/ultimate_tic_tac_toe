# Ultimate Tic Tac Toe CNN

Using CNN and monte-carlo search tree to write a program that can play tic-tac-toe and ultimate tic tac toe (as per the rules on https://bejofo.net/ttt)

## Overview

The **Ultimate Tic Tac Toe CNN** is a convolutional neural network (CNN) designed to play the game of **Ultimate Tic Tac Toe**. This project aims to implement a smart AI that can learn optimal strategies through reinforcement learning, enabling it to compete against human players or itself. This README provides an overview of the project, its functionality, installation instructions, and usage guidelines.

## Table of Contents

- [Project Description](#project-description)
- [Model Architecture](#model-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributors](#contributors)
- [License](#license)

## Project Description

- **Goal**: The primary objective of this project is to create a CNN that can effectively learn and play Ultimate Tic Tac Toe, a more complex version of the classic game.
- **Game Rules**: Ultimate Tic Tac Toe consists of a 3x3 grid of Tic Tac Toe boards. Players take turns placing their marks in one of the smaller boards, and the location of the last move determines which small board the next player must play in.

## Model Architecture

The Ultimate Tic Tac Toe CNN utilizes a convolutional neural network architecture to process the game state and make decisions.

- **Input Layer**: Takes a 3D representation of the game board (3x3x3).
- **Convolutional Layers**: Multiple convolutional layers extract features from the game board.
- **Activation Function**: ReLU (Rectified Linear Unit) is used to introduce non-linearity.
- **Pooling Layers**: Max pooling layers reduce dimensionality and retain important features.
- **Fully Connected Layers**: Connect the features learned by convolutional layers to the output layer.
- **Output Layer**: Produces predictions for the best move based on the current game state.

## Installation

To install the necessary dependencies and set up the environment for running the Ultimate Tic Tac Toe CNN, follow these steps:

1. **Clone the Repository**:
   - Navigate to your preferred directory and clone the repository.

2. **Create a Virtual Environment** (optional but recommended):
   - Create a virtual environment for the project.

3. **Install Dependencies**:
   - Use the requirements.txt file to install the necessary libraries.

## Usage

1. **Train the Model**: To train the model on the Ultimate Tic Tac Toe game, run the training script. The model will learn from self-play and improve over time.

2. **Play Against the AI**: Once the model is trained, you can play against it or let it play against itself. Use the provided scripts to initiate a game and specify the players.

3. **Evaluate Performance**: To evaluate the model's performance, run the evaluation script against a set of predetermined opponents or strategies.

## Examples

Here are a few example game scenarios:

1. **Game Scenario 1**: 
   - **Player X** starts the game by placing an X in the center of the top-left small board.
   - The AI responds with an O in the center of the middle board.

2. **Game Scenario 2**: 
   - **Player O** places an O in the bottom right corner of the bottom-left small board.
   - The AI then places an X in the top right corner of the corresponding small board.

## Contributors

- **ertouji-henruo**: Project Creator and Maintainer
- **Collaborators**: Cobra of Bronze

---

Feel free to explore the strategic world of Ultimate Tic Tac Toe with the power of convolutional neural networks! For any questions or contributions, please reach out to the contributors listed above.
