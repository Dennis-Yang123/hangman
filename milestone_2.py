# %%
import random
word_list = ["banana", "apple", "orange", "strawberry", "pineapple"]
word = random.choice(word_list)
guess = input("Please enter a single character")

if guess.isdigit():
    print("Oops that is not a valid input.")
elif len(guess) ==  1:
    print("Good guess!")
else:
    print("Oops that is not a valid input. ")
 # %%