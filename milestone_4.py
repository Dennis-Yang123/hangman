# %%
import random



word_list = ["banana", "apple", "orange", "strawberry", "pineapple"]
word = random.choice(word_list)


class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.list_of_guesses = list_of_guesses
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

    def ask_for_input():
        
        while True:
            guess = input("Please enter a guess that is a single character and alphabetical letter")
            if guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in list_of_guesses:
                print("You've already tried that letter!")
            elif len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
                
            else:
                abc.check_guess(guess)
                list_of_guesses.extend(guess)
                break
    
    def yoyo():
        print("Hello World")

abc = Hangman

# %%
