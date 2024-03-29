# Chess-Game with AI

Chess-Game is a chess game project with an artificial intelligence (AI) component in development.
The goal of this project is to create a functional chess game with the ability to play against human players or an AI.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Contribute](#contribute)

## Project Overview

The Chess-Game project aims to create a complete chess game and integrate an AI that can play against human opponents or other AIs.
Currently, the AI is not yet functional but is under development.
This project is ideal for chess enthusiasts and programming enthusiasts who want to explore chess and artificial intelligence concepts.

## Features

- Interactive chess game board.
- Legal move generation for human players.
- User-friendly user interface.
- **Sound Effects**: Enjoy immersive gameplay with sound effects for different moves.
- **Sound Control**: Toggle sound on/off in the top-left corner.
- **Theme Customization**: Change the board theme to your liking using the button in the top-right corner.
- **Image Swap**: Change the board and piece images by pressing the mouse wheel (middle mouse button).
- Integration of AI based on the Minimax algorithm. [To be completed]
- Ability to play against the AI or another human player. [To be completed for the IA]

## Screenshots

Below are some screenshots showcasing Chess-Game's features:

1. **Board Themes**:
   - The main chessboard with three different color themes:

<table>
  <tr>
    <td align="center">Theme 1</td>
    <td align="center">Theme 2</td>
    <td align="center">Theme 3</td>
  </tr>
  <tr>
    <td align="center"><img src="images/screenshots/theme_brown.png" alt="Theme 1 Screenshot"></td>
    <td align="center"><img src="images/screenshots/theme_green.png" alt="Theme 2 Screenshot"></td>
    <td align="center"><img src="images/screenshots/theme_blue.png" alt="Theme 3 Screenshot"></td>
  </tr>
</table>


2. **Gameplay**:
   - During a game:

<table>
  <tr>
    <td align="center">Board and Pieces</td>
    <td align="center">Highlighted Legal Moves</td>
  </tr>
  <tr>
    <td align="center"><img src="images/screenshots/board_and_pieces.png" alt="Board and Pieces Screenshot"></td>
    <td align="center"><img src="images/screenshots/highlighted_legal_moves.png" alt="Highlighted Legal Moves Screenshot"></td>
  </tr>
</table>

## Installation

To get started with Chess-Game, follow these steps:

1. **Clone the repository**: 
```bash
git clone https://github.com/Mathis003/Chess-Game.git
```
2. **Navigate to the project directory**:
```bash
cd Chess-Game
```
3. **Install dependencies**:
```bash
pip install -r requirements.txt
```
4. **Run the game**:
```bash
python main.py
```

This will launch the chess game, and you can start playing.

## Usage

Chess-Game is a user-friendly chess game with an AI component under development. Here's how to use it:

1. **Start the Game**:
- Launch the game by running `python main.py`.
- You will see the chessboard displayed on your screen and two buttons.
- Choose to play against another human player or against the IA. [The IA is not developped yet]

2. **Make a Move**:
- To make a move as a human player, click on the piece you want to move, and then release the click on the destination tile.
- The game will validate your move based on the rules of chess.
- When you clicks on a piece, the available moves is shown.

3. **Game Completion**:
- The game will indicate when the game is over, whether it's a win, loss, or draw.
- You can then choose to start a new game or exit.

4. **Playing Against AI (Coming Soon)**:
- The AI component is currently in development and will be added in future updates.
- You'll be able to play against the AI once it's functional.

That's it! Enjoy playing Chess-Game and improving your chess skills.

## Contribute

We welcome contributions to Chess-Game!
If you'd like to contribute to AI development, fix bugs, improve the user interface, or add features, here's how you can contribute:

1. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the Chess-Game project from GitHub.
2. Clone your fork locally: `git clone https://github.com/Mathis003/Chess-Game.git`
3. Create a branch for your contribution: `git checkout -b my-contribution`
4. Make your changes and add them: `git add .`
5. Commit your changes: `git commit -m "Add my contribution"`
6. Push the changes to your fork: `git push origin my-contribution`
7. Create a [pull request](https://docs.github.com/en/get-started/quickstart/creating-a-pull-request) to the Chess-Game main repository.

We'll review your pull request and work together to incorporate your changes into the project.