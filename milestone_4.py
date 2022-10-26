# %%
import random


num_lives = 5
class Hangman:
    def __init__(self, word_list, num_lives, word, word_guessed, num_letters, list_of_guesses, guess):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.list_of_guesses = list_of_guesses
        self.guess = guess
    def check_guess(self, guess):
        self.guess.lower()
        if self.guess in self.word:
                print("Good guess!", self.guess, "is in the word.")
            
        else:
            print("Sorry", guess, "is not in the word.")

    def ask_for_input(self):
        while True:
            guess = input("Please enter a guess that is a single character and alphabetical letter")
            if guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self.guess in self.list_of_guesses:
                print("You've already tried that letter!")
            elif len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
                
            else:
                check_guess(guess)
                list_of_guesses.extend(guess)
                break


# %%
