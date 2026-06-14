import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../solutions"))

from sehmaluva_number_guessing_game import NumberGuessingGame


def get_game():
    """Helper to create fresh game instance for testing."""
    return NumberGuessingGame()


def test_calculate_score_easy_first_attempt():
    """Test score calculation for easy difficulty on first attempt.
    On the first attempt, the base score (1000) is not reduced
    and the easy multiplier is 1 so the score should be 1000.

    """
    game = get_game()
    easy_difficulty = game.difficulties[1]
    score = game.calculate_score(attempts=1, difficulty=easy_difficulty)
    assert score == 1000


def test_calculate_score_decreases_with_attempts():
    """Test that score decreases as attempts increase."""
    game = get_game()
    difficulty = game.difficulties[1]  #Easy
    score_1 = game.calculate_score(attempts=1, difficulty=difficulty)
    score_2 = game.calculate_score(attempts=2, difficulty=difficulty)
    assert score_2 < score_1


def test_calculate_score_hard_multiplier():
    """Test that hard difficulty applies higher multiplier."""
    game = get_game()
    easy = game.difficulties[1]
    hard = game.difficulties[3]
    #Compare scores for the same number of attempts
    # Hard should give more points because of the higher multiplier
    easy_score = game.calculate_score(attempts=1, difficulty=easy)
    hard_score = game.calculate_score(attempts=1, difficulty=hard)
    assert hard_score > easy_score


def test_provide_feedback_too_low():
    """Test feedback when guess is lower than secret number."""
    game = get_game()
    difficulty = game.difficulties[1]  # Easy
    feedback = game.provide_feedback(guess=10, secret=50, difficulty=difficulty)
    assert "Too low" in feedback


def test_provide_feedback_too_high():
    """Test feedback when guess is higher than secret number."""
    game = get_game()
    difficulty = game.difficulties[1]  #Easy
    feedback = game.provide_feedback(guess=80, secret=50, difficulty=difficulty)
    assert "Too high" in feedback


def test_provide_feedback_correct():
    """Test feedback when guess matches the secret number."""
    game = get_game()
    difficulty = game.difficulties[1]  #Easy
    feedback = game.provide_feedback(guess=50, secret=50, difficulty=difficulty)
    assert "CORRECT" in feedback


def test_generate_secret_number_within_range():
    """Test that the generated secret number is within the difficulty range."""
    game = get_game()
    difficulty = game.difficulties[2]  #Medium
    secret = game.generate_secret_number(difficulty)
    min_val = difficulty["range"][0]
    max_val = difficulty["range"][1]
    assert secret >= min_val
    assert secret <= max_val