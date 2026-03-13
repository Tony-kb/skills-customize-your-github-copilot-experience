
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a playable Hangman game in Python to practice loops, conditionals, string/list updates, and user input handling. By the end of this assignment, you will create a game loop that tracks progress and ends with clear win or loss conditions.

## 📝 Tasks

### 🛠️ Set Up the Hangman Game Data

#### Description
Create the core setup for your game, including a word list, random word selection, and the initial game state shown to the player.

#### Requirements
Completed program should:

- Define a list of at least 5 possible words.
- Randomly select one word at the start of each game.
- Create a display format for the hidden word (for example: `_ _ _ _`).
- Initialize a variable for remaining incorrect guesses.


### 🛠️ Implement the Guessing Loop

#### Description
Build the main game loop that asks the player for letter guesses, updates the word display, and tracks incorrect attempts.

#### Requirements
Completed program should:

- Prompt the player to enter one letter per turn.
- Reveal correctly guessed letters in all matching positions.
- Decrease remaining guesses for incorrect letters.
- Prevent duplicate guesses from being counted twice.
- Show the current word progress and guesses remaining after each turn.


### 🛠️ Add Game End Conditions and Messages

#### Description
Finish the game by checking win and loss conditions, then display an appropriate message for the result.

#### Requirements
Completed program should:

- End with a win when all letters in the word are revealed.
- End with a loss when remaining guesses reaches 0.
- Print a clear win or lose message at the end.
- Reveal the full word in the final message if the player loses.
- Include one example run in a code block showing input/output behavior.

Example run:

```text
Word: _ _ _ _
Guess a letter: a
Correct! Word: _ a _ _
Guess a letter: z
Incorrect. Guesses left: 5
...
You win! The word was: game
```
