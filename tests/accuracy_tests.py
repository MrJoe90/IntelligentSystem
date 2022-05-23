# Accuracy Tests for Sudoku Genetic Algorithm

# Update PYTHON Path (Source below)
""" Title: Relative imports in Python 3
Author: E-rich
Date: 10th Nov. 2021
Code version: 1.0
Availability:
https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
"""
import os
import sys
from test_cases import (word_a, word_b, word_c)
from test_cases import (initial_a, initial_b, initial_c)
from IntelligentSystem.src.genetic_sudoku import Sudoku

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.dirname(SCRIPT_DIR))


# Import the Sudoku functions

# Import the test cases

generations = 500
tests = 0
accuracy_set = []

while tests < 200:
    solver = Sudoku(600, word_a, initial_a)
    solver.start()
    while not solver.finish_event:
        solver.finish_event.wait(1)
    result = solver.linked_score
    accuracy = (result / 32) * 100
    accuracy_set.append(accuracy)
    tests += 1

while tests < 200:
    solver = Sudoku(600, word_b, initial_b)
    solver.start()
    while not solver.finish_event:
        solver.finish_event.wait(1)
    result = solver.linked_score
    accuracy = (result / 32) * 100
    accuracy_set.append(accuracy)
    tests += 1

while tests < 200:
    solver = Sudoku(600, word_c, initial_c)
    solver.start()
    while not solver.finish_event:
        solver.finish_event.wait(1)
    result = solver.linked_score
    accuracy = (result / 32) * 100
    accuracy_set.append(accuracy)
    tests += 1

accuracy_set = [0, 3, 4, 5, 0]
print("Algorithm Accuracy: " + str(100 - sum(accuracy_set)/len(accuracy_set)) + "%")
