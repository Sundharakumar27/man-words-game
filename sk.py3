import random
def choose_word():
    words = ['meesho', 'powerrangers', 'leodass', 'programming', 'son', 'lion', 'roman', 'rockstar', 'eighteen', 'rockstar']
    return random.choice(words)

def display_word(word, guessed_letters):
    # Shows the word with underscores for unguessed letters
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def print_hangman(attempts):
    stages = [
        '''
        ----------
        |        |
        O        |
                 |
                 |
                 |
        =========
        ''',
        '''
        -----------
        |         |
        O         |
              O   |
             /|\  |
             /|\  |
         =========
        ''',
        '''
        ----------
        |        |
        O        |
            O    |
           /|\   |
           /|\   |
        =========
        ''',
        '''
        ----------
        |        |
        |        |
        O O      |
         /|\     |
         /|\     |
        =========
        ''',
        '''
        ----------
        |        |
        O        |
        O        |
       /|\       |
       /|\       |
        =========
        ''',
        '''
        ----------
        |        |
        O        |
       /|\       |
       /|\       |
                 |
        =========
        '''
    ]
    return stages[6 - attempts]
def play_game():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 5
    guessed_word = False
    print("Welcome to Hangman!")
    print("The word has been chosen. Let the game begin!\n")
    while attempts > 0 and not guessed_word:
        print(print_hangman(attempts))  
        print(f"\nWord to guess: {display_word(word_to_guess, guessed_letters)}")
        print(f"Attempts remaining: {attempts}")
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Oops! '{guess}' is not in the word.")
        if all(letter in guessed_letters for letter in word_to_guess):
            guessed_word = True
    if guessed_word:
        print(f"\nCongratulations! You've guessed the word: {word_to_guess}")
    else:
        print(f"\nSorry, you've run out of attempts. The word was: {word_to_guess}")

if __name__ == "__main__":
    play_game()
