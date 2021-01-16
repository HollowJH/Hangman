import random
import string

words = ['python', 'java', 'kotlin', 'javascript']
chosen = random.choice(words)
word = ["-" for i in chosen]
tries = 9
guesses = []
al = string.ascii_lowercase
print("H A N G M A N")

while tries == 9:
    play = input("Type 'play' to play the game, 'exit' to quit: ")
    if play == "exit":
        tries = 0
        break
    elif play == "play":
        tries -= 1
        break


while tries != 0 and "-" in word:
    print()
    print("".join(word))
    guess = input("Input a letter: ")

    if guess in chosen and guess not in guesses:
        for i in range(len(chosen)):
            if chosen[i] == guess:
                word[i] = guess
    else:
        if len(guess) != 1:
            print("You should input a single letter")
        elif guess not in al:
            print("Please enter a lowercase English letter")
        elif guess in guesses:
            print("You've already guessed this letter")
        else:
            print("That letter doesn't appear in the word")
            tries -= 1
    guesses.append(guess)

if "".join(word) == chosen:
    print("You guessed the word!")
    print("You survived!")
elif "-" in word:
    print("You lost!")
