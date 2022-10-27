# %%
import random



word_list = ["banana", "apple", "orange", "strawberry", "pineapple"]
word = random.choice(word_list)


class Hangman():
    def __init__(self, word_list, word, word_guessed, num_letters, list_of_guesses, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word = str
        self.word_guessed = word_guessed = str
        self.num_letters = num_letters = int
        self.list_of_guesses = list_of_guesses = list


# %%
