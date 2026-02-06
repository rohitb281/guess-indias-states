# 🗺️ Guess Indian States — Python Turtle Quiz Game

An interactive geography quiz game built with **Python Turtle graphics** and **Pandas**, where users guess Indian state names and see them placed on a map in real time.

The game tracks correct guesses and exports a list of missed states for further practice.

---

## 📌 Overview

This project displays an outline map of India and prompts the user to guess state names.  
When a correct state is entered, its name is written at the correct map coordinates using Turtle graphics.

If the user exits early, the program generates a CSV file of unguessed states for learning and revision.

---

## 🎯 Features

- Interactive text-input quiz
- India outline map visualization
- Correct state name placement using coordinates
- Progress counter (correct / total)
- Case-insensitive matching
- Missed states exported to CSV on exit
- Uses real coordinate mapping from dataset

---

## 🧠 Concepts Demonstrated

- Python Turtle graphics
- CSV data handling with Pandas
- Interactive user input loop
- Coordinate mapping
- Data filtering with DataFrames
- File export for missed answers
- Educational game design

---

## 🧱 Project Architecture
```
🗃️ guess-indian-states/
│
├── 🖼️ Outline-Map-of-India-with-States.gif # Background map image
├── 🐍 main.py # Game logic and input loop
├── 📊 states_data.csv # State names + coordinates
└── 📄 README.md
```

---

## 📊 Dataset

**states_data.csv** contains:

- State name
- X coordinate
- Y coordinate

These coordinates determine where the label appears on the map.

---

## ▶️ How to Run

### Clone repository

```bash
git clone https://github.com/rohitb281/guess-indias-states.git
cd guess-indias-states
```

### Install dependencies
```
pip install pandas
```

(Turtle is included with Python standard library.)

### Run the game
```
python main.py
```

---

## 🎮 How to Play
- Type a state name in the input box
- Correct answers appear on the map
- Progress is shown in the title bar
- Type Exit to quit early
- A file Missed states.csv will be created with remaining states

---

## 📁 Output File

When exiting early:
```
Missed states.csv
```

Contains all states not guessed — useful for revision.

---

## 🚀 Possible Improvements
- Add timer mode
- Add score persistence
- Add hints system
- Add difficulty levels
- Accept alternative spellings
- Add union territories
- Add sound effects

---

## 📄 License

Open for educational and portfolio use.

---

## 👤 Author

Rohit Bollapragada

GitHub: https://github.com/rohitb281





