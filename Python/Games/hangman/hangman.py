import random as rand
from words import words
import string

# Made with help of https://youtu.be/8ext9G7xspg

def find_valid_word(words):
    word = rand.choice(words)

    while '-' in word or ' ' in word:
        word = rand.choice(words)
    return word.upper()

def hangman():
    word = find_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while word_letters and lives:
        print(f"you have {lives} lives left \n", "You have used these letters: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]

        print("Current word: ", ''.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in word")

        elif user_letter in used_letters:
            print("You have used this letter before. Try again")
        
        else:
            print("Invalid character. Try again")
    if not lives:
        return f"You lost. The word was {word}, Better luck next time!"
    return f"You guessed the word {word}!"

print(hangman())