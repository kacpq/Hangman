from json import load
from random import choice

won = False

with open("words.json") as file:
    words = load(file)
word = choice(words)

missing_letter = ["⬚"]
answer = missing_letter * len(word)
incorrect_guesses = 7

while incorrect_guesses > 0:
    print(f"{''.join(answer)}\nGuess the word guessing letter-by-letter or type in the full word.")
    guess = input(f"You have {incorrect_guesses} incorrect guesses: ")

    guess.replace(" ", "").lower()
    if guess == word:
        won = True
        break
    elif guess in word and guess != "" and guess not in answer:
        guess = guess[:1]
        print(f"Nice! {guess.upper()} is a letter. All instances of {guess.upper()} have been filled in.")
        for letter in range(len(word)):
            if guess == word[letter]:
                answer[letter] = guess
    elif guess not in word and guess != "":
        print(f"Looks like {guess.upper()} isn't a letter or the word. You have lost an incorrect guess.")
        incorrect_guesses -= 1
    elif guess in answer:
        print("You have already guessed this letter. Try again.")
    else:
        print("Invalid Input. Try again.")

    if "".join(answer) == word:
        won = True
        break

if won:
    print(f"You've guessed the word, {word}! You win!")
else:
    print(f"You lost! The word was {word}. Better luck next time!")
