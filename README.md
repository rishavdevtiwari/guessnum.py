---

### Number Guessing Game

An interactive Python-based **Number Guessing Game** where players attempt to guess a randomly generated number between 1 and 100 within 10 attempts. The program provides feedback on how close the player is to the correct number and allows the user to continue playing after each match.

---

## Features

1. **Random Number Generation**  
   - The program generates a random number between 1 and 100 using the `random` library.

2. **Interactive Feedback**  
   - The program provides feedback such as "Too low," "Too high," or "You are close!" based on how far the guess is from the target number.

3. **Maximum Attempts**  
   - Players must guess the number within 10 attempts. If they fail, they are prompted to try again with a new random number.

4. **Continue/Exit Option**  
   - After each match, players can decide whether to continue playing or exit the game.

5. **Difficulty-Based Feedback**  
   - The game provides customized hints based on the difference between the guessed number and the target number.

---

## How to Play

1. **Run the Program**  
   - Start the program by executing the Python file.

2. **Follow Instructions**  
   - Guess a number between 1 and 100.
   - The program will provide feedback based on your guess.

3. **Win or Retry**  
   - Guess the correct number within 10 attempts to win.
   - If you fail, the game resets with a new random number.

4. **Continue or Exit**  
   - After each match, choose whether to play another round or quit.

---

## Prerequisites

- Python 3.x installed on your system.
- Basic understanding of how to run Python scripts.

---

## How to Run the Program

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/number-guessing-game.git
   ```

2. Navigate to the project directory:
   ```bash
   cd number-guessing-game
   ```

3. Run the Python file:
   ```bash
   python guessing_game.py
   ```

4. Follow the instructions displayed in the terminal.

---

## Example Gameplay

```plaintext
Welcome to the Number Guessing Game!
I have selected a random number between 1 and 100.
Try to guess it under 10 attempts!

Enter your guess: 50
Too low! You are far away from the number. Try again!

Enter your guess: 75
Still Too high! Just bit away from the number. Try again!

Enter your guess: 68
Congratulations! You've guessed the number 68 in 3 attempts!

Do you want to continue? (yes/no): yes
```

---

## Project Structure

```
├── randomnum.py    # Main Python file for the game
├── README.md           # Documentation file
```

---

## Limitations

1. The user input is validated for integer numbers but not for special cases like negative numbers or out-of-range guesses.
2. The game supports only single-player mode.

---

## About the Creator

This project was created by **[rishavdevtiwari]** as a fun and interactive way to practice Python programming. Feel free to contribute or provide feedback!

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it as per the terms of the license.

---

## Feedback & Contributions

Contributions, bug reports, and feature requests are welcome! If you have any suggestions or issues, please open an issue in the repository or submit a pull request.

---

## Contact

For any questions or feedback, you can reach out to me at:

- **GitHub Profile:** [rishavdevtiwari](https://github.com/rishavdevtiwari)
- **Email:** [rishavtiwari.ai@gmail.com]

---

<a href="https://github.com/rishavdevtiwari">©rishavdevtiwari</a>
