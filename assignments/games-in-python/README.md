# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman game in Python where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Set Up the Word Game

#### Description
Create the core game loop and prepare the list of possible words for the player to guess.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Track the number of incorrect guesses allowed
- Keep the secret word hidden at the start of the game

### 🛠️ Handle Player Guesses

#### Description
Accept letter guesses from the player and update the visible word progress after each turn.

#### Requirements
Completed program should:

- Accept one letter guess at a time
- Show the current word progress in underscore format, such as `_ _ _ _`
- Reveal correctly guessed letters in the appropriate positions
- Reduce the remaining attempts after incorrect guesses

### 🛠️ Finish the Game

#### Description
End the game when the player either guesses the word or runs out of attempts.

#### Requirements
Completed program should:

- Detect when the full word has been guessed
- Detect when the player has no attempts remaining
- Display a clear win message when the player succeeds
- Display a clear lose message when the player runs out of guesses
