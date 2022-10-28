# Hangman
## Milestone 2
The most time consuming part was getting GitHub to work and pushing changes to my repository.

### Task 1 & 2
For these tasks I had to create a list of my favourite fruits and choose a random fruit from the list which I have done by:

    import random

    word_list = ["Insert 5 favourite fruits"]

    random.choice(word_list)

I imported the random module and using the `random.choice()` function it picked a random fruit of the list.

### Task 3 
For this task I had to ask the user for input to enter a single character and assign the input to a variable called `guess`.

    guess = input("Please enter a single character")

### Task 4
For this task I had to check whether the user input was one character long and an alphabetical letter.

```python
if guess.isalpha() == False:
        print("Oops that is not a valid input.")
    elif len(guess) ==  1:
        print("Good guess!")
    else:
        print("Oops that is not a valid input. ")
```
I originally checked whether the user input was an alphabetical character using `isdigit()` but the task verification bot was not happy and suggested I use `is.aplha()` instead as you can see in the code above. 

Using if statements I checked whether the user input was either a number or alphabetical character. If it was a number it would print the fail statement otherwise it would move on to the next if statement. 

In the next if statement it checked whether the length of the now confirmed string was 1 and would print the successful message otherwise it would print the fail statement again.


## Milestone 3
### Task 3
In this task I had to create functions to check whether the user input for the guess is valid and in the randomly chosen word.

```python
def check_guess(guess):
    guess.lower()
    if guess in word:
            print("Good guess!", guess, "is in the word.")
            
    else:
        print("Sorry", guess, "is not in the word.")
```
For the `check_guess()` function I first turned the user's guess into lower case using `guess.lower()` then using if statements the function checked whether the guess was in the word.

```python
def ask_for_input():
    while True:
        guess = input("Please enter a guess that is a single character and alphabetical letter")
        if guess.isalpha() == False:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif len(guess) == 1:
            check_guess(guess)
            break
                
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")    
```
For the `ask_for_input()` function I used a while loop to iteratively check whether the user input is valid using if statements and breaking the loop when it was a valid guess.

## Milestone 4
### Task 1
This was probably the most challenging milestone yet. I was not familiar with classes so had to teach myself and google as much as possible.

```
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word)) 
        self.list_of_guesses = []
```
I originally tried to set `word, word_guessed, num_letters, list_of_guesses` as parameters in addittion to the two above but then realised that was not what the task was asking for and could have created them from the two parameters.

### Task 2
This task was pretty straightforward since it was similar to the previous milestone and was a matter of copying code and slightly editing it.

### Task 3
This was probably the most challenging task in the milestone. I was tasked to create a for loop to check if the letter is equal to the guess and replace the "_" in the `word_guessed` list.

```
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
```
The challenging part to this task was to create the for loop that would iteratively check the guess to the word and then replace the underscores in the `word_guessed` list in the correct order. I have done this with the following code 

```
self.word_guessed = [x if x == guess else "_" for x in wordlist]
```

### Task 4
For this task I as asked to add print statements when the user entered the wrong letter, reduce the number of lives by one and add the guess to the `list_of_guesses` list. This was a straightforward task.