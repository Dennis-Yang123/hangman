# %%
import random



word_list = ["banana", "apple", "orange", "strawberry", "pineapple"]
word = random.choice(word_list)


class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word)) 
        self.list_of_guesses = []
        

    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print("Good guess!", guess, "is in the word.")
                
        else:
            print("Sorry", guess, "is not in the word.")

    def ask_for_input(self):
        while True:
            guess = input("Please enter a guess that is a single character and alphabetical letter")
            if guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")

            elif len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")

            elif guess in self.list_of_guesses:
                print("You've already tried that letter!")
            
                
            else:
                self.check_guess(guess)
                self.list_of_guesses.extend(guess)
                break 

test = Hangman

# %%
