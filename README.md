# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

---
## Usage Instructions
- Firstly the computer will randomly select a word from a select list using the ```random``` module.
- After the word is selected the user will be prompted to make a one character guess that is alphabetical.
- Once the user has inputted a valid guess, the computer will then check the letter against its chosen word, to see if it is correct.
- If the guess is correct, it will display where the guess letter(s) was on the chosen word. If it was not correct it will tell you so and reduce your lives by one and then tell you how many lives you have left.
---
## File Structure
```
├── src
│   ├── hangman
│   │   ├── hangman_Template.py
│   ├── .gitignore
│   ├── README.md
│   ├── milestone_2.py
│   ├── milestone_3.py
│   ├── milestone_4.py
│   ├── milestone_5.py
└──
```
---
## More Information (Docstrings)
```
 |  Hangman(word_list, num_lives=5)
 |
 |  This class is used to create and play the classic game of Hangman.
 |
 |  Args:
 |      word_list (list): this is the argument for which words the computer can choose from.
 |      num_lives (int): this is the number of lives you can choose to have (default is 5)
 |
 |  Attributes:
 |      word_list (list): this is a list of words that the computer will use to randomly select a word to guess.
 |      word (str): this is the word that the computer has chosen to be guessed.
 |      word_guessed (list): a list of letters of the word, with "_" being used as a placeholder if the letter has  not been guessed yet.
 |      num_lives (int): this is the number of incorrect guesses (lives) the user will have to guess the word.
 |      num_letters (int): the number of unique letters in the word that haven't been guessed yet.
 |      list_of_guesses (list): a list of guesses that have already been tried.
 |
 |  Methods defined here:
 |
 |  __init__(self, word_list, num_lives=5)
 |      See help(Hangman) for a more accurate signature.
 |
 |  ask_for_input(self)
 |      This method is used to ask the user to give their guess and validates their guess to git the criterea that is needed for the game.
 |
 |      Returns:
 |          None.
 |
 |  check_guess(self, guess)
 |      This method is used to check if the guess is within the word chosed by the computer.
 |
 |      Args:
 |          guess (str): this is a single character guess that will be used to check if that character is in the word.
 |
 |      Returns:
 |          None.
 |
```