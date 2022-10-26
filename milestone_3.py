# %%
import random

word_list = ["banana", "apple", "orange", "strawberry", "pineapple"]
word = random.choice(word_list)
while True:
    guess = input("Please enter a guess that is a single character and alphabetical letter")
    if guess.isalpha() == False:
        print("Invalid letter. Please, enter a single alphabetical character.")
    elif len(guess) == 1:
        if guess in word:
            print("Good guess!", guess, "is in the word.")
            
        else:
            print("Sorry", guess, "is not in the word.")
            
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")


# %%
