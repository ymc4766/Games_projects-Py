import random

def choose_word():
    words = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "lemon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nAttempts left:", attempts)
        displayed_word = display_word(word, guessed_letters)
        print(displayed_word)

        if "_" not in displayed_word:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            print("Good guess!")
            guessed_letters.append(guess)
        else:
            print("Oops! That letter is not in the word.")
            attempts -= 1
            guessed_letters.append(guess)

    if attempts == 0:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()