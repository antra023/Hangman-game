import random

class Hangman:
    def __init__(self):
        self.categories = {
            "animals": ["cat", "dog", "elephant", "lion", "tiger"],
            "countries": ["usa", "canada", "mexico", "france", "germany"],
            "movies": ["star wars", "avengers", "inception", "matrix", "interstellar"]
        }
        self.difficulty_levels = {
            "easy": 6,
            "medium": 4,
            "hard": 2
        }
        self.word = ""
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.score = 100
        self.hint_used = False
        self.multiplayer = False
        self.player_turn = 1

    def choose_category(self):
        print("Choose a category:")
        for i, category in enumerate(self.categories.keys()):
            print(f"{i+1}. {category}")
        choice = int(input("Enter the number of your choice: "))
        self.word = random.choice(self.categories[list(self.categories.keys())[choice-1]])

    def choose_difficulty(self):
        print("Choose a difficulty level:")
        for i, difficulty in enumerate(self.difficulty_levels.keys()):
            print(f"{i+1}. {difficulty}")
        choice = int(input("Enter the number of your choice: "))
        self.incorrect_guesses = self.difficulty_levels[list(self.difficulty_levels.keys())[choice-1]]

    def play_game(self):
        self.choose_category()
        self.choose_difficulty()
        while True:
            self.display_word()
            self.display_hangman()
            if self.multiplayer:
                print(f"Player {self.player_turn}'s turn")
            guess = input("Guess a letter: ").lower()
            if guess in self.guessed_letters:
                print("You already guessed this letter!")
            elif guess in self.word:
                self.guessed_letters.append(guess)
                print("Correct!")
                self.score += 10
            else:
                self.incorrect_guesses -= 1
                self.guessed_letters.append(guess)
                print("Incorrect!")
                self.score -= 10
            if self.incorrect_guesses == 0:
                print("You lost! The word was " + self.word)
                break
            elif all(letter in self.guessed_letters for letter in self.word):
                print("You won! The word was " + self.word)
                break
            if self.multiplayer:
                self.player_turn = 2 if self.player_turn == 1 else 1

    def display_word(self):
        word_display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                word_display += letter + " "
            else:
                word_display += "_ "
        print(word_display)

    def display_hangman(self):
        hangman_graphics = [
            """
            +---+
            |   |
            |
            |
            |
            |
            =========""",
            """
            +---+
            |   |
            |   O
            |
            |
            |
            =========""",
            """
            +---+
            |   |
            |   O
            |   |
            |
            |
            =========""",
            """
            +---+
            |   |
            |   O
            |  /|
            |
            |
            =========""",
            """
            +---+
            |   |
            |   O
            |  /|\\
            |
            |
            =========""",
            """
            +---+
            |   |
            |   O
            |  /|\\
            |  /
            |
            =========""",
            """
            +---+
            |   |
            |   O
            |  /|\\
            |  / \\
            |
            ========="""
        ]
        print(hangman_graphics[6 - self.incorrect_guesses])

    def use_hint(self):
        if not self.hint_used:
            self.hint_used = True
            self.score -= 20
            print("Hint: The word is a " + self.word[0].upper() + " word.")
        else:
            print("You already used a hint!")

    def play_multiplayer(self):
        self.multiplayer = True
        self.play_game()

game = Hangman()
print("Welcome to Hangman!")
print("1. Single Player")
print("2. Multiplayer")
choice = int(input("Enter the number of your choice: "))
if choice == 1:
    game.play_game()
else:
    game.play_multiplayer()