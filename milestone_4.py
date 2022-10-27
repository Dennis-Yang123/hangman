# %%
import random



word_list = ["banana", "apple", "orange", "strawberry", "pineapple"]
word = random.choice(word_list)


class Hangman():
    def __init__(self, word_list, num_lives = 5, word, word_guessed, num_letters, list_of_guesses):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.list_of_guesses = list_of_guesses


# %%
