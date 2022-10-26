# %%
import random

word_list = ["banana", "apple", "orange", "strawberry", "pineapple"]
word = random.choice(word_list)

def check_guess(guess):
    guess.lower()
    if guess in word:
            print("Good guess!", guess, "is in the word.")
            
    else:
        print("Sorry", guess, "is not in the word.")


def ask_for_input():
    while True:
        guess = input("Please enter a guess that is a single character and alphabetical letter")
        if guess.isalpha() == False:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif len(guess) == 1:
            check_guess(guess)
                
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")    

ask_for_input()

# %%
