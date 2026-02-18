# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. You'll create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Set up the basic game structure and implement word selection functionality from a predefined list.

#### Requirements
Completed program should:

- Define a list of words from which to randomly select
- Implement a function to randomly select a word at the start of each game
- Initialize game state including the word, guessed letters, and remaining attempts (typically 6 for Hangman)

### 🛠️ Display Game Progress

#### Description
Create functionality to show players their current progress and remaining attempts.

#### Requirements
Completed program should:

- Display the current word state using underscores for unguessed letters (e.g., `_ _ _ _`)
- Show correctly guessed letters in their positions
- Display remaining incorrect guesses
- Show all previously guessed letters

### 🛠️ Handle Player Input and Game Logic

#### Description
Implement the core game loop that accepts player guesses and updates the game state.

#### Requirements
Completed program should:

- Accept letter guesses from the player
- Check if guessed letters are in the word
- Track correct and incorrect guesses
- End the game when the word is guessed or attempts are exhausted
- Display win/lose messages with appropriate feedback
