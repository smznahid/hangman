import random
class Hangman:
    '''
    This class is used to create and play the classic game of Hangman.

    Attributes:
        word_list (list): this is a list of words that the computer will use to randomly select a word to guess.
        word (str): this is the word that the computer has chosen to be guessed.
        word_guessed (list): a list of letters of the word, with \"_\" being used as a placeholder if the letter has not been guessed yet.
        num_lives (int): this is the number of incorrect guesses (lives) the user will have to guess the word.
        num_letters (int): the number of unique letters in the word that haven't been guessed yet.
        list_of_guesses (list): a list of guesses that have already been tried.
    '''
    def __init__(self, word_list, num_lives=5):
        '''
        See help(Hangman) for a more accurate signature.
        '''
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_lives = num_lives
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        This method is used to check if the guess is within the word chosed by the computer.

        Args:
            guess (str): this is a single character guess that will be used to check if that character is in the word.
        
        Returns:
            None.
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
