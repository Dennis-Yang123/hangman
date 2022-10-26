# %%
import random





class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = list
        self.num_lives = int
        self.word = str
        self.word_guessed = str
        self.num_letters = int
        self.list_of_guesses = list
        self.guess = str
    def check_guess(self, guess):
        self.guess.lower()
        if self.guess in self.word:
            print("Good guess!", self.guess, "is in the word.")
            for x in self.word:
                    if x == self.guess:
                        break
                    else:
                        print("Hello World")
                
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
