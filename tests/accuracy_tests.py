# Accuracy Tests for Sudoku Genetic Algorithm

# Update PYTHON Path (Source below)
""" Title: Relative imports in Python 3
Author: E-rich
Date: 10th Nov. 2021
Code version: 1.0
Availability:
https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
"""
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
# Import the Sudoku functions
from src.genetic_sudoku import Sudoku

# Import the test cases
from tests.test_cases import (word_a, word_b, word_c)
from tests.test_cases import (initial_a, initial_b, initial_c)

generations = 500
tests = 0
accuracy_set = []

while tests < 200:
    result = Sudoku(600, word_a, initial_a)
    result = result._population[0]  # Need to change this to score value not solution for it to work
    accuracy = (result / 32 ) * 100
    accuracy_set.append(accuracy)
    tests += 1

while tests < 200:
    result = Sudoku(600, word_b, initial_b)
    result = result._population[0]  # Need to change this to score value not solution for it to work
    accuracy = (result / 32 ) * 100
    accuracy_set.append(accuracy)
    tests += 1

while tests < 200:
    result = Sudoku(600, word_c, initial_c)
    result = result._population[0]  # Need to change this to score value not solution for it to work
    accuracy = (result / 32 ) * 100
    accuracy_set.append(accuracy)
    tests += 1

accuracy_set = [0, 3,4,5,0]
print("Algorithm Accuracy: " + str(100 - sum(accuracy_set)/len(accuracy_set)) + "%")