# IntelligentSystem

Intelligent System is a repository that contains a genetic algorithm for solving a four letter puzzle in the style of Sudoku.

For example, if provided with the four letter word "WORD" we can use this function to find a solution such that each column, row and subgrid only contains one of each letter.

|   |   |   |   |
|---|---|---|---|
| W | D | R | O |
| O | R | W | D |
| R | O | D | W |
| D | W | O | R |

The word must have a unique set of letters and can only be four letters long.

## Directory
The directory shows the location of files within this repositiory.
```
C:.
├───LICENSE
├───README.md
├───requirements.txt
├───app.py
│
├───src
│   └───genetic_sudoku.py
├───src
│   ├───brief.md
│   └───genetic_algorithm_psuedocode
│
└───tests
    ├───accuracy_tests.py
    ├───performance_tests.py
    ├───test_cases.py
    └───unit_tests.py
```

## Installation
Use the package manager [pip](https://pypi.org/project/pip/) to install the requirements.
```bash
pip install -r requirements.txt
```

## Genetic Sudoku Function
To use the function you need to import it into your script.
```python
from src.genetic_sudoku import Sudoku
```

## Example Application

The provided application in the app.py allows the user to input a four letter word and generate a solution.

To run the application, type the following into the terminal:
```bash
python app.py
```

The below shows an example session with the application.
![](https://i.imgur.com/j2SdBfI.gif)

## Testing
In order to ensure there are no detrimental changes to the genetic algorithm, the following tests can be run.

### Runnning Unit Tests
To run the unit tests use the following in the terminal for the test_cases.py file, or substitute with your own test cases.
```
python -m unittest tests/unit_tests.py
```

### Runnning Performance Tests
To run the performance tests use the following in the terminal for the test_cases.py file, or substitute with your own test cases.
```
python -m cProfile tests/performance_tests.py
```

### Runnning Accuracy Tests
To run the accuracy tests use the following in the terminal for the test_cases.py file, or substitute with your own test cases.
```
python tests/accuracy_tests.py
```

## Contributing
Pull requests permitted. When contributing please update the test directory as appropriate with any additional requirements. 