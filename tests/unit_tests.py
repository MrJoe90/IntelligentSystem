# Unit Tests for Sudoku Genetic Algorithm

# Update PYTHON Path (Source below)
""" Title: Relative imports in Python 3
Author: E-rich
Date: 10th Nov. 2021
Code version: 1.0
Availability:
https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
"""
from tests.test_cases import (answer_e)
from tests.test_cases import (initial_d, initial_e)
from tests.test_cases import (word_d, word_e)
import unittest
from tests.test_cases import (initial_a, initial_b, initial_c, initial_d)
from tests.test_cases import (word_a, word_b, word_c, word_d)
from src.genetic_sudoku import Sudoku
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import the Sudoku functions

# Import the test cases
# Import Testing package


# Unit Tests
class TestFloyd(unittest.TestCase):
    # Test correct index error message
    def test_sudoku_one(self):
        with self.assertRaises(ValueError):
            generations = 600
            Sudoku(generations, word_d, initial_d)

    # Currently unable to test correct output
    # def test_sudoku_two(self):
    #    generations = 20
    #    solution = Sudoku(generations, word_e, initial_e)
    #    print(solution)
    #    self.assertEqual(answer_e, solution)


if __name__ == '__main__':
    unittest.main()
