# %%
import random

word_list = ["banana", "apple", "orange", "strawberry", "pineapple"]
num_lives = 5

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
            empty_list = []
            for index, letter in enumerate(list(self.word)):
                if letter == guess:
                    empty_list.append(index)
            
            for number in empty_list:
                self.word_guessed[number] = guess
    
            self.num_letters = self.num_letters - 1
           
        else:
            self.num_lives = self.num_lives - 1
            print( "Sorry,", guess, "is not in the word.")
            print("You have", self.num_lives, "lives left.")
        print(self.word_guessed)
        
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
                self.list_of_guesses.append(guess)
                break 
        

def play_game(word_list):
    game = Hangman(word_list, num_lives = 5)
    while True:
        if game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives == 0:
            print("You lost!")
            break
        else:
            print("Congratulations") 
            break  

if __name__ == "__main__":
    play_game(word_list)
# %%

