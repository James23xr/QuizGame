# QuizGame

Introduction

This Python application is a simple quiz game focused on software engineering topics. It features a question class that allows for the creation of quiz questions, each with multiple-choice options and an explanation for the correct answer. The game includes a timed mode and a leaderboard to track high scores.

Features

- Question Class: Handles the creation of quiz questions, options, answers, and explanations.
- Timed Mode: Option for players to answer each question within a set time limit.
- Leaderboard: Records and displays high scores, sorted by difficulty level.

Installation

No special installation is required, as the script uses standard Python libraries. Ensure that you have Python installed on your machine.

Usage

1. Starting the Game: Run the script using Python to start the game.
2. Selecting Difficulty: Choose between 'Easy' and 'Medium' difficulty levels.
3. Timed Mode: Decide if you want to enable timed mode for an added challenge.
4. Answering Questions: Answer multiple-choice questions by entering the option number.
5. Viewing Scores: After completing the quiz, your score is displayed and recorded on the leaderboard.

Files

- `main.py`: Contains the main game logic and classes for question handling and the leaderboard.
- `scores.txt`: Stores the leaderboard scores. Automatically created if not present.

Extending the Game

- **Adding Questions:** Add more questions to the `questions` list in the `quiz_game` function.
- **Customizing Timed Mode:** Adjust the time limit for timed mode in the `Question.ask` method.
- **Leaderboard Enhancements:** Modify the `Leaderboard` class for additional features like player names.

Notes

- The application is a basic implementation and can be extended in numerous ways.
- The current scope is limited to software engineering questions but can be expanded to other topics.
