# %%
while True:
    guess = input("Please enter a guess that is a single character and alphabetical letter")
    if guess.isalpha() == False:
        print("Invalid letter. Please, enter a single alphabetical character.")
    elif len(guess) == 1:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

# %%
