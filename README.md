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
└──
```