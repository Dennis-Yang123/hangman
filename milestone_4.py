# %%
import random



word_list = ["banana", "apple", "orange", "strawberry", "pineapple"]



class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_ "] * len(self.word)
        self.num_letters = len(set(self.word)) 
        self.list_of_guesses = []
        

    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print("Good guess!", guess, "is in the word.")
            for x in range(len(self.word)):
                if sorted(guess) == sorted(self.word):
                    self.word_guessed = [s for s in self.word if guess in s]
                    break
                else:
                    print("Hello World")  
            self.num_letters = self.num_letters - 1
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
                print("You already tried that letter!")
            
                
            else:
                self.check_guess(guess)
                self.list_of_guesses.extend(guess)
                break 

test = Hangman

# %%
