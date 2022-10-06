import random
from hangman_art import stages
from hangman_art import logo
from hangman_word import word_list
from turtle import right


chosen_word = random.choice(word_list)
actual_step = 6
number_of_lifes = 6
display = []
for _ in range(0, len(chosen_word)):
    display.append("_")
print(logo)
print("Secret: " + chosen_word)
print(display)
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if (guess in display):
        print("The letter " + guess + " is already chosen")
    
      
    for index, letter in enumerate(chosen_word):
        if guess == letter:
            display[index] = letter
    
    if (guess not in chosen_word):
        actual_step-=1
        number_of_lifes-=1
        print("Wrong, the letter " + guess + " is not in the word")
        
    print(stages[actual_step])
    print(display)
    if "_" not in display:
        print("You win")
        end_of_game = True
    elif number_of_lifes == 0:
        print("You loose")
        end_of_game = True