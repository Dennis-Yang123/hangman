# %%
import random



word_list = ["banana", "apple", "orange", "strawberry", "pineapple"]



class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word)) 
        self.list_of_guesses = []
        

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess!", guess, "is in the word.")
            wordlist = [a for a in self.word] # Write the word as a list
            for x in range(len(self.word)):
                if guess in wordlist:
                    self.word_guessed = [x if x == guess else "_" for x in wordlist]
                    
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives - 1
            print("Sorry,", guess, "is not in the word.")
            print("You have", self.num_lives, "lives left.")
        
        self.list_of_guesses = self.list_of_guesses.append(guess)
    
    
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
