import random
from turtle import right

word_list = ["ardvard", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = []
for _ in range(0, len(chosen_word)):
    display.append("_")

print(display)


guess = input("Guess a letter: ").lower()

for index, letter in enumerate(chosen_word):
    if guess == letter:
        display[index] = letter

print(display)