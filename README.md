Password Strength Checker 

A beginner-friendly cybersecurity project that evaluates password strength using Python. The program checks password length, character diversity, and a small list of common passwords, then provides suggestions for improving password security.

Project Overview :

Project Name: Password Strength Checker
Language: Python 3
Platform: Kali Linux, Linux, and other systems with Python 3
Concepts: Password security, regular expressions, input handling, and basic cybersecurity.

Features : 
Evaluates password length.
Checks for uppercase and lowercase letters.
Checks for numbers and special characters.
Flags selected common passwords.
Classifies passwords as Weak, Moderate, or Strong.
Provides suggestions for improving password strength.
Allows visible password input in the terminal.

Requirements : Python 3 , Python standard library (re)

 Installation and Working for Linux:

Clone this repository :
git clone <link of github you copied>

Open the project directory:
cd password-strength-checker

Run the program :
python3 password_checker.py

Installation and Working for Windows:

Install Python on Windows from official website.
Verify Python & its version after installation.
Create the file in notepad and save as .py filename.
Open CMD in the same folder and then execute : python filename.py
If you are using Python Launcher : py filename.py

Usage :
Run the Python program and enter a sample password when prompted.
The program displays a strength classification, a rule score, and suggestions for improvement.
Use invented test passwords rather than real account passwords.

How It Works :
re: Checks for different character categories.
len(): Measures password length.
Common password list: Flags selected predictable passwords.
Scoring rules: Assign points according to configured checks.
Feedback system: Provides recommendations for improvement.

Limitations :
Uses a simple rule-based scoring system.
Checks only a small, predefined list of common passwords.
Does not guarantee that a password is secure.
Does not check breached-password databases.
Does not estimate real-world password guessability.

Future Improvements :
Add a graphical user interface using Tkinter.
Add a visual strength meter.
Detect common patterns and repeated characters.
Add unit tests.
Integrate a privacy-preserving breached-password check.
Learning Outcomes
Python programming fundamentals.
Regular expressions.
Password security concepts.
Input validation and testing.
Basic cybersecurity application development.

*****SCREENSHOTS ATTACHED*****

Author :
https://github.com/sangramdora
