# Hangman Game - Python
## Overview
This is a simple command-line implementation of the classic game **Hangman**. The game randomly selects a word from a predefined list, and the player has to guess the word by suggesting letters, with limited attempts. If the player runs out of attempts before correctly guessing the word, they lose. The game features a basic hangman visual with each incorrect guess.

## Features
- Random word selection from a list
- Dynamic display of the word with underscores for unguessed letters
- Hangman visual that updates with each incorrect guess
- Limited attempts for guessing letters
- Input validation to ensure that only single letters are guessed

## How to Play
1. The game will select a random word from a list.
2. You need to guess the letters of the word. For each wrong guess, an attempt is deducted.
3. You can keep track of the remaining attempts and the word’s progress as underscores and guessed letters.
4. You win if you can guess all the letters of the word correctly before running out of attempts.
5. If you run out of attempts, you lose, and the correct word is revealed.

## Requirements
- Python 3.x

## How to Run
1. Download or clone this repository to your local machine.
2. Open the terminal and navigate to the folder containing the Python file (`hangman_game.py`).
3. Run the following command:
   ```
   python hangman_game.py
   ```
4. Follow the on-screen instructions to play the game.

## Code Explanation
### 1. `choose_word()`:
- This function randomly selects a word from a predefined list of words.

### 2. `display_word(word, guessed_letters)`:
- This function displays the word with guessed letters visible and underscores for unguessed letters.

### 3. `print_hangman(attempts)`:
- This function displays the hangman image corresponding to the current number of remaining attempts.

### 4. `play_game()`:
- This is the main function that handles the game loop, input validation, and updates to the word display and hangman.

## Example Output

```
Welcome to Hangman!
The word has been chosen. Let the game begin!

----------

Word to guess: _ _ _ _ _
Attempts remaining: 5
Enter a letter: a

Good guess! 'a' is in the word.
----------

Word to guess: a _ _ _ _
Attempts remaining: 5
Enter a letter: b

Oops! 'b' is not in the word.
```

