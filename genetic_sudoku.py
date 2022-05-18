import threading
import random
from collections import namedtuple

Box = namedtuple('Box', "x y value")


class SudokuGeneticRepresentation:

    def __init__(self, words: list, initial_configuration: list):

        if len(words) > 4:
            raise TypeError("We only accept size 4x4 sudoku, sorry.")
        self._row_number = 4
        self._col_number = 4
        self._data = []
        self._position_fixed = initial_configuration
        for i in range(0, 4):
            self._data.append([random.choice(words) for j in range(0, 4)])
        # Assuming a correct input --another type error should be raised here.
        for element in initial_configuration:
            self._data[element.x][element.y] = element.value
        self._internal_use = []
        self._mapping_word_to_bit = {words[0]: (0, 0),
                                     words[1]: (0, 1),
                                     words[2]: (1, 0),
                                     words[3]: (1, 1),
                                     }
        for i in range(0, 4):
            self._internal_use.append(
                [self._mapping_word_to_bit[self._data[i][j]] for j in range(0, 4)])

    @property
    def data(self):
        return self._data

    @property
    def internal_use(self):
        return self._internal_use

    def __str__(self):
        return self._data.__str__()


class Sudoku(threading.Thread):
    def __init__(self, number_of_generation, words: list, initial: Box):
        threading.Thread.__init__(self)
        self._number_of_generation = number_of_generation
        self._sudoku = None
        self._poupolation = [SudokuGeneticRepresentation(
            words, initial) for i in range(0, 10)]

    def run(self):
        current_generation = 0

        while current_generation < self._number_of_generation:
            current_generation += 1

    def fitness_function(self):
        # Foreach element in the population
        pass

    def crossfunction(self):
        pass

    def mutation(self):
        pass


if __name__ == "__main__":

    words = ['a', 'b', 'c', 'd']
    initial = [Box(2, 0, 'c'),
               Box(1, 1, 'b'),
               Box(1, 3, 'a'),
               Box(2, 2, 'd')]

    sudoku_genitico = Sudoku(100, words, initial)
    sudoku_genitico.start()
