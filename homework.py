# Homework:
# In the lesson, we made a simple hangman game. But there is no way to lose, as there is no strikes.
# TODO: implement a strike system of 8 strikes. Once the player guesses the incorrect letter 8 times, they lose
# Some hints have been given to you in the file
# w3school python compiler sometimes doesn't work for user inputs. A website you can use for running the code is: https://www.online-python.com/

import random
word_list = ["lion","tiger","elephant","giraffe","zebra","kangaroo","koala","panda",
"penguin","dolphin","whale","shark","eagle","owl","wolf","fox","bear","cheetah","crocodile","gorilla"]
word = random.choice(word_list)
display = ["_"] * len(word)

# hint
strike_count = 8  # total strike count
current_strike = 0  # how many strikes the player currently has

while "_" in display and current_strike < 8:
    # ask player for a letter and see if it matches to any in the word
    print("Word is: ", end = "")
    for letter in display:
        print(letter, end = " ")

    print() # so that the "Enter the next letter" message begins with a new line
    letter = input("Enter the next letter: ")
    
    letter_found = False  # TODO: make this true if a letter is found. After the following "for loop", if
    # letter_found is false, increase the strike count. If letter_found is true, don't increase.
    for i in range(len(word)):
        if word[i] == letter:
            display[i] = letter

# TODO: only print the correct word if the player didn't lose
print("You got it!")
print("The word is " + word
      
for i in range(len(word)):
        if word[i] == letter:
            display[i] = letter
            letter_found = True



