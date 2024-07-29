import random
import json

class WordGuessGame:
    def __init__(self):
        self.words = {
            "easy": ["apple", "ball", "cat", "dog", "egg"],
            "medium": ["banana", "orange", "grapes", "mango", "peach"],
            "hard": ["pineapple", "strawberry", "blueberry", "raspberry", "watermelon"]
        }
        self.difficulty = None
        self.word = None
        self.masked_word = None
        self.attempts_left = None
        self.incorrect_guesses = 0
        self.correct_guesses = []
        self.max_attempts = {"easy": 10, "medium": 7, "hard": 5}
        self.score = 0
        self.leaderboard_file = "leaderboard.json"

    def select_difficulty(self):
        while True:
            self.difficulty = input("Select difficulty level (easy, medium, hard): ").lower()
            if self.difficulty in self.words:
                break
            else:
                print("Invalid difficulty level. Please choose again.")

    def select_word(self):
        self.word = random.choice(self.words[self.difficulty])
        self.masked_word = ["_" for _ in self.word]
        self.attempts_left = self.max_attempts[self.difficulty]

    def display_masked_word(self):
        print("Word to guess: " + " ".join(self.masked_word))
    
    def get_player_guess(self):
        while True:
            guess = input("Enter a letter to guess: ").lower()
            if len(guess) == 1 and guess.isalpha():
                return guess
            else:
                print("Invalid input. Please enter a single letter.")
    
    def update_masked_word(self, guess):
        if guess in self.word:
            self.correct_guesses.append(guess)
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.masked_word[i] = guess
        else:
            self.incorrect_guesses += 1
            self.attempts_left -= 1
            print(f"Incorrect guess! Attempts left: {self.attempts_left}")

    def check_win(self):
        return "_" not in self.masked_word
    
    def display_result(self, won):
        if won:
            print(f"Congratulations! You guessed the word: {self.word}")
        else:
            print(f"Game Over! The word was: {self.word}")
        self.calculate_score(won)
        self.update_leaderboard()

    def calculate_score(self, won):
        if won:
            self.score = self.attempts_left * 10
        else:
            self.score = 0
        print(f"Your score: {self.score}")

    def update_leaderboard(self):
        try:
            with open(self.leaderboard_file, 'r') as file:
                leaderboard = json.load(file)
        except FileNotFoundError:
            leaderboard = []
        
        player_name = input("Enter your name for the leaderboard: ")
        leaderboard.append({"name": player_name, "score": self.score, "difficulty": self.difficulty})
        leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)

        with open(self.leaderboard_file, 'w') as file:
            json.dump(leaderboard, file, indent=4)
        
        print("Leaderboard:")
        for entry in leaderboard:
            print(f"{entry['name']} - {entry['score']} (Difficulty: {entry['difficulty']})")

    def play(self):
        self.select_difficulty()
        self.select_word()

        while self.attempts_left > 0:
            self.display_masked_word()
            guess = self.get_player_guess()
            self.update_masked_word(guess)
            if self.check_win():
                self.display_result(True)
                break
        else:
            self.display_result(False)

if __name__ == "__main__":
    game = WordGuessGame()
    game.play()
