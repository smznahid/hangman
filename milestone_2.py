import random

word_list = ["apple", "kiwi", "pear", "strawberry", "tomato", "elderberry", "cherry"]
word = random.choice(word_list)


guess = input("Guess: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
