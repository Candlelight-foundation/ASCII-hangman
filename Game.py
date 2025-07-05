import random
import os

# --- Game Configuration ---
WORD_LIST = [
    "python", "programming", "developer", "computer", "algorithm",
    "keyboard", "monitor", "software", "hardware", "internet",
    "variable", "function", "string", "integer", "boolean",
    "framework", "database", "security", "network", "cloud"
]
MAX_INCORRECT_GUESSES = 6

# --- ASCII Hangman Art ---
HANGMAN_PICS = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

# --- Game Functions ---

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_word(word_list):
    """Selects a random word from the given list."""
    return random.choice(word_list).upper()

def display_game_state(word, guessed_letters, incorrect_guesses):
    """Displays the current state of the game: hangman, word, guessed letters."""
    clear_screen()
    print(HANGMAN_PICS[incorrect_guesses])
    print("\n--- Hangman ---")

    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    print(f"\nWord: {displayed_word}")

    guessed_str = ", ".join(sorted(list(guessed_letters)))
    print(f"Guessed letters: {guessed_str if guessed_str else 'None'}")
    print(f"Incorrect guesses left: {MAX_INCORRECT_GUESSES - incorrect_guesses}")
    print("-" * 20)

def get_player_guess(guessed_letters):
    """Gets a valid single letter guess from the player."""
    while True:
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        else:
            return guess

def play_hangman():
    """Main function to run the Hangman game."""
    word_to_guess = get_random_word(WORD_LIST)
    guessed_letters = set()
    incorrect_guesses = 0
    game_over = False

    while not game_over:
        display_game_state(word_to_guess, guessed_letters, incorrect_guesses)

        # Check for win condition
        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"\nCongratulations! You guessed the word: {word_to_guess}")
            game_over = True
            continue

        # Check for loss condition
        if incorrect_guesses >= MAX_INCORRECT_GUESSES:
            print("\nGame Over! You ran out of guesses.")
            print(f"The word was: {word_to_guess}")
            game_over = True
            continue

        guess = get_player_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

        input("\nPress Enter to continue...") # Pause for player to read message

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_hangman()
    else:
        print("Thanks for playing Hangman!")

# --- Start the game ---
if __name__ == "__main__":
    play_hangman()
