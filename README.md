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
