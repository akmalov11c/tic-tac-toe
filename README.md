
Noughts and Crosses Game

This project is a Python implementation of the classic "Noughts and Crosses" game, also known as Tic-Tac-Toe. 
The game allows a player to compete against an AI that makes strategic moves to try and win the game. 
The player's objective is to get three of their marks (either 'X' or 'O') in a row, column, or diagonal on the game board.

Features

  1. User Interface: Simple command-line interface for interaction.
  2. Player vs. AI: Play against an AI that employs basic strategy to compete.
  3. Leaderboard: Save and display scores of players in a leaderboard.
     
Files

  1. play_game.py: This file contains the main script for running the game. It interacts with the user, initiates gameplay, and manages the leaderboard.
  2. noughtsandcrosses.py: This module includes the core game logic, such as board initialization, player moves, AI moves, win/draw checks, etc.
     
How to Play

  1. Run the play_game.py script.
  2. Choose from the menu options:
    - Play the game
    - Save your score
    - Load and display the leaderboard
    - Quit the program
  4. During gameplay, input your moves by selecting the corresponding square number on the board.
  5. The AI will make its moves automatically.
  6. The game ends when one player wins, it's a draw, or the player quits.
     
Leaderboard

  - Scores are saved with the player's name in a JSON file (leaderboard.txt).
  - The leaderboard displays players' names and their scores, sorted in descending order of scores.
    
Future Improvements

  - Implement advanced AI algorithms for more challenging gameplay.
  - Enhance the user interface with graphical elements.
  - Add options for customizing game settings (board size, difficulty level, etc.).
    
Contribution

  - Contributions to the project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to submit a pull request.

Credits

  - This project was created by Sardor Akmalovich.
