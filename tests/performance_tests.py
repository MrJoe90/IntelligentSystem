# Performance Tests for Sudoku Genetic Algorithm

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

# Import Testing package
import cProfile

# Test the performance of four random word puzzles
generations = 20
cProfile.run("Sudoku(generations, word_a, initial_a)")
cProfile.run("Sudoku(generations, word_b, initial_b)")
cProfile.run("Sudoku(generations, word_c, initial_c)")

# Test the performance difference for different number of generations

generations_one = 20
cProfile.run("Sudoku(generations_one, word_a, initial_a)")
generations_two = 30
cProfile.run("Sudoku(generations_two, word_a, initial_a)")
generations_three = 50
cProfile.run("Sudoku(generations_three, word_a, initial_a)")
generations_four = 10000
cProfile.run("Sudoku(generations_four, word_a, initial_a)")
