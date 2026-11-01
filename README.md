# ShadowFox Python Development & Sports Analytics Internship

This repository contains the complete code submissions and capstone project for the **ShadowFox Python Development Internship** (Track: Python Development & Data Analytics).

---

## 📌 Repository Structure

```text
├── Task-1-Fundamentals/
│   └── task1_fundamentals.py       # Variables, Numbers, Lists, Conditionals, Loops
├── Task-2-Hangman/
│   └── task2_hangman.py            # CLI Hangman Game (Finite State Machine)
├── Task-3-Cricket-Analytics/
│   ├── fielding_analysis.py        # Ball-by-ball IPL fielding metrics evaluation
│   └── match_data.csv              # Match dataset (Delhi Capitals - Arun Jaitley Stadium)
├── requirements.txt                # Python environment dependencies
└── README.md                       # Project documentation & summary
```

---

## 🚀 Task Overview

### Task 1: Python Fundamentals & Algorithmic Problem Solving
- **Variables & Precision:** Storing floating-point calculations ($\pi = \frac{22}{7}$), verifying keyword immutability (`for`), and Simple Interest calculation.
- **Numbers & Mensuration:** Octal string transformations (`format(145, 'o')`), circular pond surface area & fluid volume calculations, kinematics conversions.
- **Data Structures (Lists):** Roster operations on Justice League (element insertion, leader reassignments, slicing, alphabetical sorting).
- **Conditional Branching:** Body Mass Index (BMI) classifier and dictionary-based city/country lookup.
- **Control Loops:** Stochastic 6-sided die simulation and workout interval monitoring.

### Task 2: Interactive Application (Hangman Engine)
- Implementation of an interactive CLI-based word-guessing game.
- Built using Finite State Machine (FSM) mechanics:
  - Input sanitization (case normalization, alphabet validation).
  - Set-based guess tracking to prevent duplicate penalties.
  - Dynamic ASCII scaffold rendering based on remaining attempts.

### Task 3: Capstone – IPL Cricket Fielding Performance Analytics
A sports analytics framework modeling ball-by-ball defensive contributions for Delhi Capitals during an IPL T20 match at Arun Jaitley Stadium.

#### Performance Score (PS) Formulation:
$$\text{PS} = (CP \times 1) + (GT \times 1) + (C \times 3) - (DC \times 3) + (ST \times 3) + (RO \times 3) - (MRO \times 2) + (DH \times 2) + RS$$

#### Score Summary:
| Player Name | Position | CP (+1) | GT (+1) | C (+3) | DC (-3) | ST/RO (+3) | MRO (-2) | DH (+2) | RS | Performance Score (PS) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Yash Dhull** | Covers | 3 | 1 | 2 | 0 | 0 | 1 | 0 | +3 | **11** |
| **Axar Patel** | Point | 2 | 3 | 1 | 0 | 1 | 0 | 0 | 0 | **11** |
| **Rilee Rossouw** | Short Mid-Wicket | 2 | 1 | 1 | 0 | 0 | 0 | 1 | +2 | **10** |
| **Aman Khan** | Long Off | 4 | 1 | 0 | 0 | 1 | 0 | 0 | +1 | **9** |
| **Kuldeep Yadav** | Mid-Wicket | 3 | 0 | 1 | 1 | 0 | 0 | 1 | +4 | **9** |
| **Lalit Yadav** | Cover Point | 1 | 2 | 1 | 0 | 0 | 0 | 1 | -2 | **6** |
| **Phil Salt** | Wicketkeeper | 1 | 2 | 0 | 1 | 1 | 0 | 0 | -1 | **2** |

---

## 🛠️ Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/ShadowFox-Python-Internship.git
   cd ShadowFox-Python-Internship
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run individual modules:**
   ```bash
   python Task-1-Fundamentals/task1_fundamentals.py
   python Task-2-Hangman/task2_hangman.py
   python Task-3-Cricket-Analytics/fielding_analysis.py
   ```

---

## 👤 Author
- **Intern:** Aanya Badgaiyan
- **Role:** Python Development Intern
- **Program:** ShadowFox Virtual Internship
