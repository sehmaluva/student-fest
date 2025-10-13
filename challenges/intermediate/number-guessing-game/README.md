# 🎯 Number Guessing Game

**Difficulty**: Intermediate  
**Estimated Time**: 45-60 minutes  
**Topics**: Random number generation, User input validation, Game logic, Loops, Conditional statements

## 📝 Challenge Description

Create an interactive **Number Guessing Game** that challenges players to guess a randomly generated number within a certain range. The game should provide feedback, track attempts, and offer different difficulty levels.

## 🎯 Requirements

Your game must include:

### Core Features
1. **Random Number Generation** - Generate a secret number between 1-100 (or configurable range)
2. **User Input** - Accept guesses from the user with input validation
3. **Feedback System** - Tell the user if their guess is too high, too low, or correct
4. **Attempt Tracking** - Count and display the number of attempts
5. **Win/Lose Conditions** - End game when number is guessed or maximum attempts reached

### Enhanced Features
6. **Difficulty Levels** - Easy (1-50), Medium (1-100), Hard (1-200)
7. **Score System** - Calculate score based on attempts and difficulty
8. **Play Again** - Option to play multiple rounds
9. **Statistics** - Track games played, win rate, average attempts
10. **Hints** (Optional) - Provide clues for hard mode

## 📊 Example Gameplay

```
🎯 Welcome to the Number Guessing Game!

Choose difficulty:
1. Easy (1-50)
2. Medium (1-100)
3. Hard (1-200)

Enter your choice: 2

I'm thinking of a number between 1 and 100...
Take a guess: 50
Too high! Try again: 25
Too low! Try again: 37
Too high! Try again: 31
Too low! Try again: 34
Too high! Try again: 32
Too low! Try again: 33

🎉 Congratulations! You guessed it in 7 attempts!
Your score: 850 points

Play again? (y/n): n

Thanks for playing!
Games played: 1
Win rate: 100%
Average attempts: 7.0
```

## 🛠️ Implementation Guidelines

### Language Options
You can implement this in **any programming language**. Popular choices:
- Python 🐍 (Great for beginners)
- JavaScript 🟨 (Web-based version)
- Java ☕ (Object-oriented approach)
- C++ ⚡ (Performance focused)
- Go 🔵 (Simple and efficient)

### Code Structure
```
yourusername_number_guessing_game.py
├── Main game loop
├── Difficulty selection
├── Number generation
├── Input validation
├── Guess checking
├── Score calculation
├── Statistics tracking
└── Play again logic
```

### Best Practices
- **Error Handling**: Handle invalid inputs gracefully
- **Code Comments**: Explain complex logic
- **Modular Design**: Break into functions/methods
- **Constants**: Use named constants for magic numbers
- **User Experience**: Clear prompts and feedback

## 🧪 Testing Your Solution

### Test Cases
1. **Valid Guesses**: Numbers within range
2. **Invalid Input**: Non-numeric input, out-of-range numbers
3. **Edge Cases**: Guess exactly minimum/maximum values
4. **Win Condition**: Correct guess on first try
5. **Lose Condition**: Exceed maximum attempts
6. **Difficulty Levels**: All three levels work correctly

### Manual Testing Checklist
- [ ] Game starts with difficulty selection
- [ ] Random number generates correctly for each difficulty
- [ ] Input validation rejects invalid entries
- [ ] Feedback messages are clear and helpful
- [ ] Attempt counter works accurately
- [ ] Score calculation is correct
- [ ] Play again feature works
- [ ] Statistics display properly

## 📁 Submission Format

### File Naming Convention
```
solutions/yourusername_number_guessing_game.ext
```

**Examples:**
- `solutions/alice_python_number_guessing_game.py`
- `solutions/bob_javascript_number_guessing_game.js`
- `solutions/charlie_java_NumberGuessingGame.java`

### Include in Your Submission
1. **Source Code**: Well-commented, readable code
2. **README**: Brief explanation of your implementation
3. **Test Results**: Screenshot or description of testing

## 🎨 Extra Challenges (Optional)

### Advanced Features
- **Timed Mode**: Guess within time limit
- **Multiplayer**: Two players take turns
- **AI Opponent**: Computer tries to guess your number
- **Save/Load**: Persist game statistics
- **GUI Version**: Desktop or web interface
- **Sound Effects**: Audio feedback for guesses

### Code Quality
- **Unit Tests**: Automated test suite
- **Documentation**: Detailed code documentation
- **Performance**: Optimize for speed
- **Security**: Input sanitization

## 💡 Hints & Tips

### Getting Started
1. Start with basic version (fixed range, no difficulty levels)
2. Add input validation early
3. Implement core game loop
4. Add difficulty levels
5. Enhance with scoring and statistics

### Common Pitfalls
- **Infinite Loops**: Always validate input before using
- **Off-by-One Errors**: Check range boundaries carefully
- **Random Seeding**: Ensure truly random numbers
- **Type Conversion**: Handle string-to-number conversion

### Learning Objectives
- **Random Number Generation**: Using language-specific random libraries
- **Input/Output**: Reading user input and displaying output
- **Control Flow**: Loops and conditional statements
- **Error Handling**: Graceful failure recovery
- **Modular Programming**: Breaking code into reusable functions

## 🏆 Achievement Unlocks

Complete this challenge to earn:
- 🧩 **Problem Solver** badge
- 🎯 **Game Developer** achievement
- 📊 **Intermediate Coder** recognition

## 🤝 Contributing Solutions

1. **Fork** this repository
2. **Create** your solution file in `solutions/`
3. **Test** thoroughly
4. **Commit** with descriptive message
5. **Pull Request** with explanation
6. **Earn** your badges! 🏅

---

**Happy coding! May the random numbers be in your favor! 🎲**