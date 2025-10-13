#!/usr/bin/env python3
"""
Number Guessing Game - Interactive Challenge Solution
Author: sehmaluva
Language: Python 3
Difficulty: Intermediate

A complete implementation of the Number Guessing Game challenge
with all required features and enhanced gameplay elements.
"""

import random
import json
import os
from datetime import datetime
from typing import Dict, List, Tuple, Optional


class NumberGuessingGame:
    """Interactive Number Guessing Game with multiple difficulty levels and statistics tracking."""

    def __init__(self):
        self.difficulties = {
            1: {
                "name": "Easy",
                "range": (1, 50),
                "max_attempts": 10,
                "points_multiplier": 1,
            },
            2: {
                "name": "Medium",
                "range": (1, 100),
                "max_attempts": 8,
                "points_multiplier": 1.5,
            },
            3: {
                "name": "Hard",
                "range": (1, 200),
                "max_attempts": 6,
                "points_multiplier": 2,
            },
        }

        self.stats_file = "game_statistics.json"
        self.stats = self.load_statistics()

    def load_statistics(self) -> Dict:
        """Load game statistics from file."""
        if os.path.exists(self.stats_file):
            try:
                with open(self.stats_file, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass

        # Default statistics
        return {
            "games_played": 0,
            "games_won": 0,
            "total_attempts": 0,
            "best_score": 0,
            "difficulty_stats": {
                diff["name"]: {"played": 0, "won": 0}
                for diff in self.difficulties.values()
            },
        }

    def save_statistics(self):
        """Save game statistics to file."""
        try:
            with open(self.stats_file, "w") as f:
                json.dump(self.stats, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save statistics: {e}")

    def get_valid_input(
        self,
        prompt: str,
        validator_func=None,
        error_msg: str = "Invalid input. Please try again.",
    ) -> str:
        """Get validated user input."""
        while True:
            try:
                user_input = input(prompt).strip()
                if validator_func and not validator_func(user_input):
                    print(error_msg)
                    continue
                return user_input
            except (EOFError, KeyboardInterrupt):
                print("\nGame interrupted. Thanks for playing!")
                exit(0)

    def select_difficulty(self) -> Dict:
        """Let user select game difficulty."""
        print("\n🎯 Choose your difficulty level:")
        for num, diff in self.difficulties.items():
            range_min, range_max = diff["range"]
            print(
                f"{num}. {diff['name']} ({range_min}-{range_max}, {diff['max_attempts']} attempts max)"
            )

        def validate_difficulty(choice: str) -> bool:
            return choice.isdigit() and int(choice) in self.difficulties

        choice = self.get_valid_input(
            "\nEnter your choice (1-3): ",
            validate_difficulty,
            "Please enter 1, 2, or 3.",
        )

        return self.difficulties[int(choice)]

    def generate_secret_number(self, difficulty: Dict) -> int:
        """Generate a random secret number for the given difficulty."""
        min_val, max_val = difficulty["range"]
        return random.randint(min_val, max_val)

    def get_guess(self, difficulty: Dict, attempts: int) -> Optional[int]:
        """Get and validate user's guess."""
        min_val, max_val = difficulty["range"]
        max_attempts = difficulty["max_attempts"]

        def validate_guess(guess_str: str) -> bool:
            if not guess_str.isdigit():
                return False
            guess = int(guess_str)
            return min_val <= guess <= max_val

        prompt = f"Guess #{attempts + 1}/{max_attempts} ({min_val}-{max_val}): "
        error_msg = f"Please enter a number between {min_val} and {max_val}."

        guess_input = self.get_valid_input(prompt, validate_guess, error_msg)
        return int(guess_input)

    def provide_feedback(self, guess: int, secret: int, difficulty: Dict) -> str:
        """Provide feedback on the user's guess."""
        if guess < secret:
            if difficulty["name"] == "Hard" and abs(guess - secret) <= 5:
                return "Too low! 🔥 You're very close!"
            return "Too low! Try a higher number."
        elif guess > secret:
            if difficulty["name"] == "Hard" and abs(guess - secret) <= 5:
                return "Too high! 🔥 You're very close!"
            return "Too high! Try a lower number."
        else:
            return "🎉 CORRECT! You guessed it!"

    def calculate_score(self, attempts: int, difficulty: Dict) -> int:
        """Calculate score based on attempts and difficulty."""
        max_attempts = difficulty["max_attempts"]
        multiplier = difficulty["points_multiplier"]

        # Base score decreases with more attempts
        base_score = max(100, 1000 - (attempts - 1) * 50)
        return int(base_score * multiplier)

    def play_round(self) -> Tuple[bool, int, int, Dict]:
        """Play a single round of the game."""
        print("\n" + "=" * 50)
        print("🎯 Welcome to the Number Guessing Game!")
        print("=" * 50)

        difficulty = self.select_difficulty()
        secret_number = self.generate_secret_number(difficulty)

        print(
            f"\nI'm thinking of a number between {difficulty['range'][0]} and {difficulty['range'][1]}..."
        )
        print(f"You have {difficulty['max_attempts']} attempts to guess it!")

        attempts = 0
        won = False

        while attempts < difficulty["max_attempts"]:
            guess = self.get_guess(difficulty, attempts)

            attempts += 1
            feedback = self.provide_feedback(guess, secret_number, difficulty)

            print(f"➤ {feedback}")

            if guess == secret_number:
                won = True
                break

        return won, attempts, secret_number, difficulty

    def show_results(
        self, won: bool, attempts: int, secret_number: int, difficulty: Dict
    ):
        """Display round results and update statistics."""
        print("\n" + "-" * 50)

        if won:
            score = self.calculate_score(attempts, difficulty)
            print(
                f"🎉 Congratulations! You guessed {secret_number} in {attempts} attempts!"
            )
            print(f"🏆 Your score: {score} points")

            # Update statistics
            self.stats["games_played"] += 1
            self.stats["games_won"] += 1
            self.stats["total_attempts"] += attempts
            self.stats["best_score"] = max(self.stats["best_score"], score)

            diff_name = difficulty["name"]
            self.stats["difficulty_stats"][diff_name]["played"] += 1
            self.stats["difficulty_stats"][diff_name]["won"] += 1

        else:
            print(f"😔 Game Over! The number was {secret_number}.")
            print(f"You used all {difficulty['max_attempts']} attempts.")

            # Update statistics for loss
            self.stats["games_played"] += 1
            self.stats["total_attempts"] += attempts
            diff_name = difficulty["name"]
            self.stats["difficulty_stats"][diff_name]["played"] += 1

        self.save_statistics()

    def show_statistics(self):
        """Display comprehensive game statistics."""
        if self.stats["games_played"] == 0:
            print("\n📊 No games played yet. Start playing to see your statistics!")
            return

        win_rate = (self.stats["games_won"] / self.stats["games_played"]) * 100
        avg_attempts = self.stats["total_attempts"] / self.stats["games_played"]

        print("\n📊 Your Game Statistics")
        print("=" * 40)
        print(f"Games Played: {self.stats['games_played']}")
        print(f"Games Won: {self.stats['games_won']}")
        print(f"Win Rate: {win_rate:.1f}%")
        print(f"Average Attempts: {avg_attempts:.1f}")
        print(f"Best Score: {self.stats['best_score']}")

        print("\n🎯 Difficulty Breakdown:")
        for diff_name, stats in self.stats["difficulty_stats"].items():
            if stats["played"] > 0:
                diff_win_rate = (stats["won"] / stats["played"]) * 100
                print(
                    f"  {diff_name}: {stats['won']}/{stats['played']} wins ({diff_win_rate:.1f}%)"
                )

    def play_again(self) -> bool:
        """Ask user if they want to play again."""
        response = self.get_valid_input(
            "\nPlay again? (y/n): ",
            lambda x: x.lower() in ["y", "n", "yes", "no"],
            "Please enter 'y' for yes or 'n' for no.",
        ).lower()

        return response in ["y", "yes"]

    def run(self):
        """Main game loop."""
        print("🎲 Number Guessing Game - Interactive Edition")
        print("🎯 Can you guess the secret number?")

        playing = True
        while playing:
            won, attempts, secret, difficulty = self.play_round()
            self.show_results(won, attempts, secret, difficulty)
            playing = self.play_again()

        print("\n" + "=" * 50)
        print("Thanks for playing the Number Guessing Game! 🎮")
        self.show_statistics()
        print("\nCome back soon for more challenges! 🌟")


def main():
    """Entry point for the game."""
    # Seed random number generator for better randomness
    random.seed()

    game = NumberGuessingGame()
    game.run()


if __name__ == "__main__":
    main()
